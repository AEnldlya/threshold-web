#!/usr/bin/env python3
"""
Example 3: Complete deployment workflow - Deploy + Search + Buy + Configure.

This example demonstrates the full automated workflow:
1. Deploy to Vercel
2. Search for affordable domains
3. Buy cheapest domain
4. Configure DNS to point to Vercel
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from src.vercel_manager import VercelManager
from src.domain_searcher import DomainSearcher
from src.registrar_manager import RegistrarManager
from src.dns_configurator import DNSConfigurator
from src.permission_gates import PermissionGates
from src.state_manager import StateManager
from src.price_optimizer import PriceOptimizer


def complete_deployment_workflow():
    """Example: Complete deployment workflow."""
    
    # Initialize all components
    permissions = PermissionGates()
    vercel = VercelManager()
    searcher = DomainSearcher()
    registrar = RegistrarManager()
    dns = DNSConfigurator()
    optimizer = PriceOptimizer()
    state = StateManager("complete-workflow-example")
    
    # Configuration
    website_id = "summer-hair-salon-2026"
    business_name = "Summer Street Hair Salon"
    business_type = "Salon"
    project_path = "/workspace/summer-hair-salon"
    vercel_project = business_name.lower().replace(" ", "-")
    max_domain_price = 50.0
    
    print("\n" + "="*60)
    print("EXAMPLE 3: Complete Deployment Workflow")
    print("="*60)
    
    # STEP 1: Deploy to Vercel
    print(f"\n{'='*60}")
    print("STEP 1: Deploy to Vercel")
    print('='*60)
    
    print(f"\n🚀 Deploying {business_name}...")
    print(f"   Project: {vercel_project}")
    print(f"   Path: {project_path}")
    
    approved = permissions.request_approval(
        action="deploy_to_vercel",
        details={"project": vercel_project, "path": project_path}
    )
    
    if not approved:
        print("❌ Cancelled by user")
        return {"success": False}
    
    # Deploy (simulated)
    preview_url = f"https://{vercel_project}.vercel.app"
    state.save_step("deployed", {"preview_url": preview_url})
    print(f"✅ Deployed to: {preview_url}")
    
    # STEP 2: Search for domains
    print(f"\n{'='*60}")
    print("STEP 2: Search for Domains")
    print('='*60)
    
    print(f"\n🔍 Searching for domains...")
    print(f"   Business: {business_name}")
    print(f"   Type: {business_type}")
    print(f"   Max Price: ${max_domain_price:.2f}/year")
    
    approved = permissions.request_approval(
        action="search_domain",
        details={
            "business_name": business_name,
            "business_type": business_type,
            "max_price": max_domain_price
        }
    )
    
    if not approved:
        print("❌ Cancelled by user")
        return {"success": False}
    
    # Simulated domain options
    options = [
        {
            "domain": "summerstassalon.com",
            "price": 8.88,
            "registrar": "namecheap"
        },
        {
            "domain": "summerstreethouse.com",
            "price": 10.87,
            "registrar": "namecheap"
        },
        {
            "domain": "summerhaircuts.io",
            "price": 48.88,
            "registrar": "namecheap"
        }
    ]
    
    cheapest_option = options[0]
    print(f"✅ Found {len(options)} affordable domains")
    print(f"   Cheapest: {cheapest_option['domain']} (${cheapest_option['price']:.2f}/year)")
    
    state.save_step("domains_searched", {
        "options": options,
        "cheapest": cheapest_option["domain"]
    })
    
    # STEP 3: Buy domain
    print(f"\n{'='*60}")
    print("STEP 3: Purchase Domain")
    print('='*60)
    
    cost = optimizer.calculate_total_cost(
        domain=cheapest_option["domain"],
        registrar=cheapest_option["registrar"],
        years=1,
        privacy=True
    )
    
    print(f"\n💰 Purchasing {cheapest_option['domain']}")
    print(f"   Base Price: ${cost['subtotal']:.2f}")
    print(f"   Privacy Protection: ${cost['privacy_protection']:.2f}")
    print(f"   Total: ${cost['total']:.2f}")
    
    approved = permissions.request_approval(
        action="purchase_domain",
        details={
            "domain": cheapest_option["domain"],
            "registrar": cheapest_option["registrar"],
            "price": cost["total"],
            "privacy": True
        }
    )
    
    if not approved:
        print("❌ Cancelled by user")
        return {"success": False}
    
    print(f"✅ Purchased: {cheapest_option['domain']}")
    state.save_step("domain_purchased", {
        "domain": cheapest_option["domain"],
        "cost": cost["total"],
        "registrar": cheapest_option["registrar"]
    })
    
    # STEP 4: Configure DNS
    print(f"\n{'='*60}")
    print("STEP 4: Configure DNS")
    print('='*60)
    
    print(f"\n🔗 Configuring DNS for {cheapest_option['domain']}")
    print(f"   Pointing to: {vercel_project}")
    
    dns_records = dns.get_vercel_records(vercel_project)
    print(f"\n   DNS Records:")
    for record in dns_records:
        print(f"   - {record['type']} {record['name']}: {record['value']}")
    
    approved = permissions.request_approval(
        action="configure_dns",
        details={
            "domain": cheapest_option["domain"],
            "vercel_project": vercel_project,
            "records": dns_records
        }
    )
    
    if not approved:
        print("❌ Cancelled by user")
        return {"success": False}
    
    print(f"✅ DNS configured")
    state.save_step("dns_configured", {"domain": cheapest_option["domain"]})
    
    # SUCCESS!
    print(f"\n{'='*60}")
    print("✅ DEPLOYMENT COMPLETE!")
    print('='*60)
    
    print(f"\n🎉 Your website is ready!")
    print(f"\n📍 Domain: {cheapest_option['domain']}")
    print(f"🔗 Vercel URL: {preview_url}")
    print(f"💰 Domain Cost: ${cost['total']:.2f}/year")
    print(f"\n⏳ The domain will be live in 30-60 minutes")
    
    # Show timeline
    timeline = state.get_timeline()
    print(f"\n📊 Timeline:")
    for event in timeline:
        print(f"   ✓ {event['step']}")
    
    return {
        "success": True,
        "domain": cheapest_option["domain"],
        "vercel_url": preview_url,
        "cost": cost["total"],
        "status": "live_in_30_60_minutes"
    }


if __name__ == "__main__":
    result = complete_deployment_workflow()
    print(f"\n📋 Result: {result}")
