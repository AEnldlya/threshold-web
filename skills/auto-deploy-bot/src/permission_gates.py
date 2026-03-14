"""Permission gates - Human approval workflow at each step."""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)


class PermissionGates:
    """Manages human approval gates for critical operations."""
    
    def __init__(self, approval_log_path: str = ".approval_log.json"):
        """Initialize permission gates.
        
        Args:
            approval_log_path: Path to store approval history
        """
        self.approval_log_path = Path(approval_log_path)
        self._ensure_log_exists()
    
    def _ensure_log_exists(self):
        """Ensure approval log file exists."""
        if not self.approval_log_path.exists():
            self.approval_log_path.write_text(json.dumps([], indent=2))
    
    def request_approval(
        self,
        action: str,
        details: Dict[str, Any],
        timeout: int = 300
    ) -> bool:
        """Request human approval for an action.
        
        Args:
            action: Action requiring approval (e.g., "deploy_to_vercel")
            details: Details about the action
            timeout: Approval timeout in seconds
        
        Returns:
            True if approved, False if denied or timed out
        """
        print(f"\n{'⏸️  APPROVAL REQUIRED'}")
        print(f"{'='*50}")
        print(f"Action: {action}")
        print(f"Details:")
        
        for key, value in details.items():
            if isinstance(value, (dict, list)):
                print(f"  {key}:")
                print(f"    {json.dumps(value, indent=6)}")
            else:
                print(f"  {key}: {value}")
        
        print(f"\nApprove this action? (yes/no)")
        
        response = input("> ").strip().lower()
        
        approved = response in ["yes", "y", "approve"]
        
        # Log the approval decision
        self._log_approval(action, details, approved)
        
        if approved:
            print(f"✅ Approved")
        else:
            print(f"❌ Denied")
        
        return approved
    
    def _log_approval(self, action: str, details: Dict[str, Any], approved: bool):
        """Log approval decision for audit trail.
        
        Args:
            action: Action name
            details: Action details
            approved: Whether it was approved
        """
        log_data = self.approval_log_path.read_text()
        approvals = json.loads(log_data)
        
        approval_record = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "details": details,
            "approved": approved
        }
        
        approvals.append(approval_record)
        
        self.approval_log_path.write_text(json.dumps(approvals, indent=2))
        logger.info(f"Logged approval: {action} = {approved}")
    
    def get_approval_history(self) -> list:
        """Get approval history from log."""
        log_data = self.approval_log_path.read_text()
        return json.loads(log_data)
    
    def get_approvals_for_action(self, action: str) -> list:
        """Get all approvals for a specific action.
        
        Args:
            action: Action name
        
        Returns:
            List of approval records for this action
        """
        history = self.get_approval_history()
        return [a for a in history if a["action"] == action]
    
    def check_auto_approve(
        self,
        action: str,
        cost: Optional[float] = None,
        auto_approve_threshold: Optional[float] = None
    ) -> bool:
        """Check if action should auto-approve based on thresholds.
        
        Args:
            action: Action name
            cost: Cost of the operation (for purchases)
            auto_approve_threshold: Cost threshold for auto-approval
        
        Returns:
            True if should auto-approve
        """
        if auto_approve_threshold is None:
            return False
        
        if cost is None:
            return False
        
        return cost <= auto_approve_threshold
    
    def prevent_double_spend(
        self,
        domain: str,
        registrar: str,
        hours_back: int = 24
    ) -> bool:
        """Check if domain was already purchased recently.
        
        Args:
            domain: Domain name
            registrar: Registrar name
            hours_back: How many hours back to check
        
        Returns:
            True if domain was already purchased, False otherwise
        """
        from datetime import datetime, timedelta
        
        history = self.get_approval_history()
        cutoff = datetime.now() - timedelta(hours=hours_back)
        
        for record in history:
            if record["action"] == "purchase_domain":
                record_time = datetime.fromisoformat(record["timestamp"])
                if record_time < cutoff:
                    continue
                
                details = record.get("details", {})
                if (details.get("domain") == domain and 
                    details.get("registrar") == registrar and
                    record["approved"]):
                    return True
        
        return False
    
    def get_total_cost_for_action(
        self,
        action: str,
        hours_back: int = 24
    ) -> float:
        """Get total cost for a type of action in the time window.
        
        Args:
            action: Action name
            hours_back: Hours to look back
        
        Returns:
            Total cost
        """
        from datetime import datetime, timedelta
        
        history = self.get_approval_history()
        cutoff = datetime.now() - timedelta(hours=hours_back)
        total = 0.0
        
        for record in history:
            if record["action"] == action:
                record_time = datetime.fromisoformat(record["timestamp"])
                if record_time < cutoff:
                    continue
                
                details = record.get("details", {})
                cost = details.get("cost") or details.get("total") or 0
                if record["approved"]:
                    total += float(cost)
        
        return total


class AutoApprovalConfig:
    """Configuration for auto-approval rules."""
    
    def __init__(self):
        """Initialize auto-approval config."""
        self.rules = {
            "deploy_vercel": False,           # Always ask
            "search_domain": False,           # Always ask
            "buy_domain_under": 15.0,        # Auto-buy if <$15/year
            "configure_dns": True,            # Auto-configure
            "batch_deploy_under": 100.0      # Auto-batch if <$100 total
        }
    
    def should_auto_approve(
        self,
        action: str,
        cost: Optional[float] = None
    ) -> bool:
        """Check if action should auto-approve.
        
        Args:
            action: Action name
            cost: Cost if applicable
        
        Returns:
            True if should auto-approve
        """
        if action == "deploy_vercel":
            return self.rules["deploy_vercel"]
        elif action == "search_domain":
            return self.rules["search_domain"]
        elif action == "buy_domain":
            if cost is None:
                return False
            threshold = self.rules.get("buy_domain_under", 15.0)
            return cost <= threshold
        elif action == "configure_dns":
            return self.rules["configure_dns"]
        elif action == "batch_deploy":
            if cost is None:
                return False
            threshold = self.rules.get("batch_deploy_under", 100.0)
            return cost <= threshold
        
        return False
    
    def set_rule(self, action: str, value: Any):
        """Set an auto-approval rule.
        
        Args:
            action: Action name
            value: Rule value
        """
        self.rules[action] = value
    
    def get_rule(self, action: str) -> Any:
        """Get an auto-approval rule.
        
        Args:
            action: Action name
        
        Returns:
            Rule value or None
        """
        return self.rules.get(action)
