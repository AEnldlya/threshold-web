"""Batch processor - Handle multiple website deployments."""

from typing import List, Dict, Any
import logging
from state_manager import StateManager
from permission_gates import PermissionGates

logger = logging.getLogger(__name__)


class BatchProcessor:
    """Processes batch deployments of multiple websites."""
    
    def __init__(self):
        """Initialize batch processor."""
        self.permissions = PermissionGates()
    
    def process_batch(
        self,
        websites: List[Dict[str, str]],
        require_approval: bool = True,
        batch_approval: bool = False
    ) -> Dict[str, Any]:
        """Process batch deployment.
        
        Args:
            websites: List of website configs
            require_approval: Require approval
            batch_approval: Approve batch or individual items
        
        Returns:
            Batch processing result
        """
        batch_id = self._generate_batch_id()
        state = StateManager(batch_id)
        
        print(f"\n📦 Batch Processing ({len(websites)} websites)")
        print(f"   Batch ID: {batch_id}")
        
        # Show summary
        total_cost = self._estimate_batch_cost(websites)
        print(f"   Estimated Cost: ${total_cost:.2f}")
        
        if require_approval:
            if batch_approval:
                # Single approval for entire batch
                approved = self.permissions.request_approval(
                    action="batch_deploy",
                    details={
                        "batch_id": batch_id,
                        "website_count": len(websites),
                        "estimated_cost": total_cost
                    }
                )
                if not approved:
                    return {
                        "success": False,
                        "status": "cancelled",
                        "batch_id": batch_id
                    }
            else:
                # Individual approval for each website
                for website in websites:
                    approved = self.permissions.request_approval(
                        action="batch_website_deploy",
                        details={
                            "website_id": website.get("website_id"),
                            "business_name": website.get("business_name")
                        }
                    )
                    if not approved:
                        website["approved"] = False
                    else:
                        website["approved"] = True
        
        # Process each website
        results = []
        successful = 0
        failed = 0
        
        for i, website in enumerate(websites, 1):
            print(f"\n{'='*50}")
            print(f"Website {i}/{len(websites)}: {website.get('business_name')}")
            print('='*50)
            
            if batch_approval == False and not website.get("approved", True):
                print("⏭️  Skipped by user")
                results.append({
                    "website_id": website.get("website_id"),
                    "status": "skipped"
                })
                continue
            
            result = self._deploy_single(website)
            results.append(result)
            
            if result.get("success"):
                successful += 1
                print(f"✅ Success")
            else:
                failed += 1
                print(f"❌ Failed: {result.get('error')}")
        
        # Save batch results
        state.save_step("batch_complete", {
            "websites": len(websites),
            "successful": successful,
            "failed": failed
        })
        
        print(f"\n{'='*50}")
        print(f"BATCH COMPLETE")
        print('='*50)
        print(f"✅ Successful: {successful}")
        print(f"❌ Failed: {failed}")
        
        return {
            "success": True,
            "batch_id": batch_id,
            "websites_processed": len(websites),
            "successful": successful,
            "failed": failed,
            "results": results,
            "total_cost": total_cost
        }
    
    def _deploy_single(self, website: Dict[str, str]) -> Dict[str, Any]:
        """Deploy a single website.
        
        Args:
            website: Website config
        
        Returns:
            Deployment result
        """
        try:
            # Placeholder for actual deployment logic
            # In real implementation, would call vercel_manager, etc.
            
            website_id = website.get("website_id")
            business_name = website.get("business_name")
            
            logger.info(f"Deploying {website_id}: {business_name}")
            
            return {
                "success": True,
                "website_id": website_id,
                "business_name": business_name,
                "status": "deployed",
                "url": f"https://{website_id}.vercel.app"
            }
        
        except Exception as e:
            logger.error(f"Error deploying website: {e}")
            return {
                "success": False,
                "website_id": website.get("website_id"),
                "error": str(e)
            }
    
    def _estimate_batch_cost(self, websites: List[Dict[str, str]]) -> float:
        """Estimate total cost for batch.
        
        Args:
            websites: List of websites
        
        Returns:
            Total estimated cost
        """
        # Base cost per domain
        domain_cost = 8.99
        privacy_cost = 2.99
        
        return len(websites) * (domain_cost + privacy_cost)
    
    def _generate_batch_id(self) -> str:
        """Generate unique batch ID.
        
        Returns:
            Batch ID
        """
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"batch_{timestamp}"
    
    def get_batch_status(self, batch_id: str) -> Dict[str, Any]:
        """Get status of a batch.
        
        Args:
            batch_id: Batch ID
        
        Returns:
            Batch status
        """
        state = StateManager(batch_id)
        return state.get_status()
    
    def resume_batch(self, batch_id: str) -> Dict[str, Any]:
        """Resume a partially completed batch.
        
        Args:
            batch_id: Batch ID
        
        Returns:
            Resume result
        """
        state = StateManager(batch_id)
        status = state.get_status()
        
        print(f"📦 Resuming batch {batch_id}")
        print(f"   Completed steps: {len(status['completed_steps'])}")
        
        return {
            "success": True,
            "batch_id": batch_id,
            "status": status
        }
