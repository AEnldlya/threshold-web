#!/usr/bin/env python3
"""
Example 4: Batch deployment of multiple websites.

This example shows how to deploy multiple websites at once
with batch approval to save time when deploying several sites.
"""

import sys
from pathlib import Path
import json

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from src.batch_processor import BatchProcessor
from src.permission_gates import PermissionGates
from src.price_optimizer import PriceOptimizer


def batch_deployment_example():
    """Example: Deploy multiple websites."""
    
    # Initialize components
    processor = BatchProcessor()
    permissions = PermissionGates()
    optimizer = PriceOptimizer()
    
    # Multiple websites to deploy
    websites = [
        {
            "website_id": "salon-1",
            "business_name": "Sunshine Hair Studio",
            "business_type": "Salon"
        },
        {
            "website_id": "salon-2",
            "business_name": "Elite Haircuts",
            "business_type": "Salon"
        },
        {
            "website_id": "salon-3",
            "business_name": "Modern Beauty Salon",
            "business_type": "Salon"
        }
    ]
    
    print("\n" + "="*60)
    print("EXAMPLE 4: Batch Deployment")
    print("="*60)
    
    # Calculate batch cost
    total_cost = 0.0
    for website in websites:
        cost = optimizer.calculate_total_cost(
            domain=f"{website['website_id']}.com",
            registrar="namecheap",
            years=1,
            privacy=True
        )
        total_cost += cost["total"]
    
    print(f"\n📦 Batch Deployment Summary:")
    print(f"   Websites: {len(websites)}")
    print(f"   Estimated Cost: ${total_cost:.2f}")
    print(f"   Cost per Website: ${total_cost/len(websites):.2f}")
    
    # Show websites
    print(f"\n📋 Websites to Deploy:")
    for i, website in enumerate(websites, 1):
        print(f"   {i}. {website['business_name']} ({website['business_type']})")
    
    # Request approval for batch
    approved = permissions.request_approval(
        action="batch_deploy",
        details={
            "websites": len(websites),
            "estimated_cost": total_cost,
            "business_types": list(set(w["business_type"] for w in websites))
        }
    )
    
    if not approved:
        print("\n❌ Batch deployment cancelled")
        return {"success": False}
    
    # Process each website
    print(f"\n{'='*60}")
    print("Processing Websites")
    print('='*60)
    
    results = []
    successful = 0
    failed = 0
    
    for i, website in enumerate(websites, 1):
        website_id = website["website_id"]
        business_name = website["business_name"]
        
        print(f"\n[{i}/{len(websites)}] {business_name}")
        
        # Simulate deployment
        result = {
            "website_id": website_id,
            "business_name": business_name,
            "status": "deployed",
            "vercel_url": f"https://{website_id}.vercel.app",
            "domain": f"{website_id}.com",
            "cost": optimizer.calculate_total_cost(
                f"{website_id}.com",
                "namecheap",
                years=1,
                privacy=True
            )["total"]
        }
        
        print(f"   ✅ Deployed to {result['vercel_url']}")
        print(f"   💰 Domain cost: ${result['cost']:.2f}")
        
        results.append(result)
        successful += 1
    
    # Summary
    print(f"\n{'='*60}")
    print("BATCH COMPLETE!")
    print('='*60)
    
    print(f"\n📊 Results:")
    print(f"   ✅ Successful: {successful}")
    print(f"   ❌ Failed: {failed}")
    print(f"   💰 Total Cost: ${total_cost:.2f}")
    
    print(f"\n🌐 Live Websites:")
    for result in results:
        print(f"   • {result['business_name']}")
        print(f"     Domain: {result['domain']}")
        print(f"     URL: {result['vercel_url']}")
    
    return {
        "success": True,
        "batch_id": f"batch_{len(websites)}_websites",
        "websites_deployed": len(websites),
        "total_cost": total_cost,
        "results": results
    }


if __name__ == "__main__":
    result = batch_deployment_example()
    print(f"\n📋 Result: {result}")
