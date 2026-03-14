#!/usr/bin/env python3
"""
Auto-Deploy Bot - Automated deployment and domain purchase with permission gates.

This CLI tool automates the process of deploying websites to Vercel and purchasing
affordable domains, with human approval gates at each critical step.
"""

import argparse
import json
import sys
import os
from pathlib import Path
from typing import Optional, Dict, Any

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))
sys.path.insert(0, str(Path(__file__).parent / "registrars"))

from src.permission_gates import PermissionGates
from src.vercel_manager import VercelManager
from src.domain_searcher import DomainSearcher
from src.registrar_manager import RegistrarManager
from src.state_manager import StateManager
from src.dns_configurator import DNSConfigurator
from src.batch_processor import BatchProcessor


def load_env():
    """Load environment variables from .env file."""
    from dotenv import load_dotenv
    env_path = Path(__file__).parent / ".env"
    if env_path.exists():
        load_dotenv(env_path)


def deploy_with_approval(args):
    """Deploy to Vercel with human approval gate."""
    load_env()
    
    permissions = PermissionGates()
    vercel = VercelManager()
    state = StateManager(args.website_id)
    
    print(f"\n🚀 Deploy {args.website_id} to Vercel")
    print(f"   Project: {args.vercel_project_name}")
    print(f"   Path: {args.project_path}")
    
    if args.require_approval:
        approved = permissions.request_approval(
            action="deploy_to_vercel",
            details={
                "project": args.vercel_project_name,
                "path": args.project_path,
                "timeout": args.deployment_timeout
            }
        )
        if not approved:
            print("❌ Deployment cancelled by user.")
            return {"success": False, "status": "cancelled"}
    
    print("\n⏳ Deploying to Vercel...")
    result = vercel.deploy(
        project_name=args.vercel_project_name,
        project_path=args.project_path,
        timeout=args.deployment_timeout
    )
    
    if result["success"]:
        state.save_step("deployed", result)
        print(f"✅ Deployed to: {result['preview_url']}")
        return {
            "success": True,
            "status": "deployed",
            "preview_url": result["preview_url"],
            "deployment_time": result.get("deployment_time", 0)
        }
    else:
        print(f"❌ Deployment failed: {result.get('error', 'Unknown error')}")
        return {"success": False, "error": result.get("error")}


def search_cheapest_domain(args):
    """Search for cheapest domain across registrars."""
    load_env()
    
    permissions = PermissionGates()
    searcher = DomainSearcher()
    state = StateManager(args.website_id)
    
    if args.require_approval:
        approved = permissions.request_approval(
            action="search_domain",
            details={
                "business_name": args.business_name,
                "business_type": args.business_type,
                "max_price": args.max_price
            }
        )
        if not approved:
            print("❌ Domain search cancelled.")
            return {"success": False, "status": "cancelled"}
    
    print(f"\n🔍 Searching for domains for {args.business_name}...")
    print(f"   Type: {args.business_type}")
    print(f"   Max Price: ${args.max_price}/year")
    
    options = searcher.search(
        business_name=args.business_name,
        business_type=args.business_type,
        preferred_tlds=args.preferred_tld,
        max_price=args.max_price,
        registrars=args.registrars
    )
    
    if options:
        print(f"\n✅ Found {len(options)} available domains:\n")
        for i, opt in enumerate(options[:5], 1):
            print(f"  {i}. {opt['domain']}")
            print(f"     Price: ${opt['price']:.2f}/year")
            print(f"     Registrar: {opt['registrar']}")
        
        state.save_step("domains_searched", {"options": options})
        
        return {
            "success": True,
            "options": options[:5],
            "cheapest": options[0]["domain"],
            "cheapest_price": options[0]["price"]
        }
    else:
        print("❌ No domains found matching criteria.")
        return {"success": False, "error": "No domains found"}


def buy_domain_with_approval(args):
    """Purchase domain with approval gate."""
    load_env()
    
    permissions = PermissionGates()
    registrar = RegistrarManager()
    state = StateManager(args.domain.replace(".", "_"))
    
    print(f"\n💰 Buy {args.domain}")
    print(f"   Registrar: {args.registrar}")
    print(f"   Years: {args.years}")
    
    # Get price first
    price_result = registrar.check_price(args.domain, args.registrar)
    price = price_result.get("price", 0) if price_result.get("success") else 0
    
    print(f"   Price: ${price:.2f}/year")
    if args.privacy_protection:
        print(f"   Privacy: Enabled (+$2.99/year)")
    
    total = price + (2.99 if args.privacy_protection else 0)
    total *= args.years
    print(f"   Total: ${total:.2f}")
    
    if args.require_approval:
        approved = permissions.request_approval(
            action="purchase_domain",
            details={
                "domain": args.domain,
                "registrar": args.registrar,
                "price": price,
                "total": total,
                "privacy": args.privacy_protection
            }
        )
        if not approved:
            print("❌ Purchase cancelled.")
            return {"success": False, "status": "cancelled"}
    
    print(f"\n⏳ Purchasing {args.domain}...")
    result = registrar.purchase_domain(
        domain=args.domain,
        registrar=args.registrar,
        years=args.years,
        auto_renew=args.auto_renew,
        privacy=args.privacy_protection
    )
    
    if result.get("success"):
        state.save_step("domain_purchased", result)
        print(f"✅ Purchased: {args.domain}")
        return {
            "success": True,
            "domain": args.domain,
            "registrar": args.registrar,
            "cost": total
        }
    else:
        print(f"❌ Purchase failed: {result.get('error', 'Unknown error')}")
        return {"success": False, "error": result.get("error")}


def configure_domain_dns(args):
    """Configure DNS for domain to point to Vercel."""
    load_env()
    
    permissions = PermissionGates()
    dns = DNSConfigurator()
    state = StateManager(args.domain.replace(".", "_"))
    
    print(f"\n🔗 Configure DNS for {args.domain}")
    print(f"   Pointing to: {args.vercel_project}")
    print(f"   Registrar: {args.registrar}")
    
    # Get DNS records
    records = dns.get_vercel_records(args.vercel_project)
    print(f"\n   DNS Records:")
    for record in records:
        print(f"   - {record['type']} {record['name']}: {record['value']}")
    
    if args.require_approval:
        approved = permissions.request_approval(
            action="configure_dns",
            details={
                "domain": args.domain,
                "records": records,
                "vercel_project": args.vercel_project
            }
        )
        if not approved:
            print("❌ DNS configuration cancelled.")
            return {"success": False, "status": "cancelled"}
    
    print(f"\n⏳ Configuring DNS...")
    result = dns.configure(
        domain=args.domain,
        registrar=args.registrar,
        vercel_project=args.vercel_project
    )
    
    if result.get("success"):
        state.save_step("dns_configured", result)
        print(f"✅ DNS configured")
        print(f"   Domain will be live in 30-60 minutes")
        return {
            "success": True,
            "domain": args.domain,
            "status": "configured"
        }
    else:
        print(f"❌ DNS configuration failed: {result.get('error', 'Unknown error')}")
        return {"success": False, "error": result.get("error")}


def deploy_and_buy_complete(args):
    """Full workflow: deploy to Vercel, search domains, buy, configure DNS."""
    load_env()
    
    state = StateManager(args.website_id)
    print(f"\n🚀 Complete Deployment for {args.website_id}")
    print(f"   Business: {args.business_name}")
    print(f"   Type: {args.business_type}")
    print(f"   Max Domain Price: ${args.max_domain_price}/year")
    
    # Step 1: Deploy to Vercel
    print(f"\n{'='*50}")
    print("STEP 1: Deploy to Vercel")
    print('='*50)
    
    class DeployArgs:
        pass
    
    deploy_args = DeployArgs()
    deploy_args.website_id = args.website_id
    deploy_args.project_path = args.project_path
    deploy_args.vercel_project_name = args.business_name.lower().replace(" ", "-")
    deploy_args.deployment_timeout = 300
    deploy_args.require_approval = args.require_approval_at_each_step
    
    deploy_result = deploy_with_approval(deploy_args)
    if not deploy_result.get("success"):
        return {"success": False, "error": "Deployment failed"}
    
    preview_url = deploy_result.get("preview_url")
    state.save_step("step1_deployed", {"preview_url": preview_url})
    
    # Step 2: Search for domains
    print(f"\n{'='*50}")
    print("STEP 2: Search for Domains")
    print('='*50)
    
    search_args = DeployArgs()
    search_args.website_id = args.website_id
    search_args.business_name = args.business_name
    search_args.business_type = args.business_type
    search_args.max_price = args.max_domain_price
    search_args.preferred_tld = [".com", ".io", ".co"]
    search_args.registrars = ["namecheap", "porkbun"]
    search_args.require_approval = args.require_approval_at_each_step
    
    search_result = search_cheapest_domain(search_args)
    if not search_result.get("success"):
        return {"success": False, "error": "Domain search failed"}
    
    cheapest_domain = search_result.get("cheapest")
    cheapest_price = search_result.get("cheapest_price")
    state.save_step("step2_domains_searched", {
        "cheapest": cheapest_domain,
        "price": cheapest_price
    })
    
    # Step 3: Buy domain
    print(f"\n{'='*50}")
    print("STEP 3: Purchase Domain")
    print('='*50)
    
    buy_args = DeployArgs()
    buy_args.domain = cheapest_domain
    buy_args.registrar = "namecheap"
    buy_args.years = 1
    buy_args.auto_renew = args.auto_renew_domain
    buy_args.privacy_protection = True
    buy_args.require_approval = args.require_approval_at_each_step
    
    buy_result = buy_domain_with_approval(buy_args)
    if not buy_result.get("success"):
        return {"success": False, "error": "Domain purchase failed"}
    
    state.save_step("step3_domain_purchased", buy_result)
    
    # Step 4: Configure DNS
    print(f"\n{'='*50}")
    print("STEP 4: Configure DNS")
    print('='*50)
    
    dns_args = DeployArgs()
    dns_args.domain = cheapest_domain
    dns_args.registrar = "namecheap"
    dns_args.vercel_project = deploy_args.vercel_project_name
    dns_args.require_approval = False  # Auto-configure after purchase approval
    
    dns_result = configure_domain_dns(dns_args)
    if not dns_result.get("success"):
        return {"success": False, "error": "DNS configuration failed"}
    
    state.save_step("step4_dns_configured", dns_result)
    
    # Success!
    print(f"\n{'='*50}")
    print("✅ DEPLOYMENT COMPLETE!")
    print('='*50)
    print(f"\n📍 Website URL: {cheapest_domain}")
    print(f"🔗 Vercel URL: {preview_url}")
    print(f"💰 Domain Cost: ${cheapest_price:.2f}/year")
    print(f"\n⏳ Live in 30-60 minutes at {cheapest_domain}")
    
    return {
        "success": True,
        "domain": cheapest_domain,
        "vercel_url": preview_url,
        "domain_cost": cheapest_price,
        "total_cost": cheapest_price
    }


def batch_deploy_with_domains(args):
    """Deploy multiple websites with domain purchases."""
    load_env()
    
    processor = BatchProcessor()
    print(f"\n📦 Batch Deployment ({len(args.websites)} websites)")
    
    results = processor.process_batch(
        websites=args.websites,
        require_approval=args.require_approval,
        batch_approval=args.batch_approval
    )
    
    return results


def deployment_status(args):
    """Check status of deployments."""
    state = StateManager(args.website_id)
    status = state.get_status()
    
    print(f"\n📊 Deployment Status for {args.website_id}")
    print(json.dumps(status, indent=2))
    
    return status


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Auto-Deploy Bot - Deploy to Vercel and buy domains with approval gates"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # deploy_with_approval command
    deploy_parser = subparsers.add_parser("deploy_with_approval", help="Deploy to Vercel with approval")
    deploy_parser.add_argument("--website-id", required=True, help="Website ID")
    deploy_parser.add_argument("--project-path", required=True, help="Path to project")
    deploy_parser.add_argument("--vercel-project-name", required=True, help="Vercel project name")
    deploy_parser.add_argument("--deployment-timeout", type=int, default=300, help="Deployment timeout in seconds")
    deploy_parser.add_argument("--require-approval", action="store_true", default=True, help="Require approval")
    deploy_parser.set_defaults(func=deploy_with_approval)
    
    # search_cheapest_domain command
    search_parser = subparsers.add_parser("search_cheapest_domain", help="Search for cheapest domains")
    search_parser.add_argument("--website-id", required=True, help="Website ID")
    search_parser.add_argument("--business-name", required=True, help="Business name")
    search_parser.add_argument("--business-type", required=True, help="Business type")
    search_parser.add_argument("--max-price", type=float, default=50, help="Max domain price")
    search_parser.add_argument("--preferred-tld", nargs="+", default=[".com", ".io"], help="Preferred TLDs")
    search_parser.add_argument("--registrars", nargs="+", default=["namecheap", "porkbun"], help="Registrars to search")
    search_parser.add_argument("--require-approval", action="store_true", default=True, help="Require approval")
    search_parser.set_defaults(func=search_cheapest_domain)
    
    # buy_domain_with_approval command
    buy_parser = subparsers.add_parser("buy_domain_with_approval", help="Purchase domain with approval")
    buy_parser.add_argument("--domain", required=True, help="Domain to buy")
    buy_parser.add_argument("--registrar", default="namecheap", help="Registrar to use")
    buy_parser.add_argument("--years", type=int, default=1, help="Years to register")
    buy_parser.add_argument("--auto-renew", action="store_true", default=True, help="Auto-renew")
    buy_parser.add_argument("--privacy-protection", action="store_true", default=True, help="Privacy protection")
    buy_parser.add_argument("--require-approval", action="store_true", default=True, help="Require approval")
    buy_parser.set_defaults(func=buy_domain_with_approval)
    
    # configure_domain_dns command
    dns_parser = subparsers.add_parser("configure_domain_dns", help="Configure DNS for domain")
    dns_parser.add_argument("--domain", required=True, help="Domain to configure")
    dns_parser.add_argument("--registrar", default="namecheap", help="Registrar")
    dns_parser.add_argument("--vercel-project", required=True, help="Vercel project name")
    dns_parser.add_argument("--require-approval", action="store_true", default=True, help="Require approval")
    dns_parser.set_defaults(func=configure_domain_dns)
    
    # deploy_and_buy_complete command
    complete_parser = subparsers.add_parser("deploy_and_buy_complete", help="Full deployment workflow")
    complete_parser.add_argument("--website-id", required=True, help="Website ID")
    complete_parser.add_argument("--project-path", required=True, help="Path to project")
    complete_parser.add_argument("--business-name", required=True, help="Business name")
    complete_parser.add_argument("--business-type", required=True, help="Business type")
    complete_parser.add_argument("--max-domain-price", type=float, default=50, help="Max domain price")
    complete_parser.add_argument("--auto-renew-domain", action="store_true", default=True, help="Auto-renew domain")
    complete_parser.add_argument("--require-approval-at-each-step", action="store_true", default=True, help="Require approval at each step")
    complete_parser.set_defaults(func=deploy_and_buy_complete)
    
    # batch_deploy_with_domains command
    batch_parser = subparsers.add_parser("batch_deploy_with_domains", help="Deploy multiple websites")
    batch_parser.add_argument("--websites-json", required=True, help="JSON file with website list")
    batch_parser.add_argument("--require-approval", action="store_true", default=True, help="Require approval")
    batch_parser.add_argument("--batch-approval", action="store_true", default=False, help="Batch approval mode")
    batch_parser.set_defaults(func=batch_deploy_with_domains)
    
    # deployment_status command
    status_parser = subparsers.add_parser("deployment_status", help="Check deployment status")
    status_parser.add_argument("--website-id", required=True, help="Website ID")
    status_parser.set_defaults(func=deployment_status)
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    result = args.func(args)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
