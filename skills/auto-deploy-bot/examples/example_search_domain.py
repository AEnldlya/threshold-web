#!/usr/bin/env python3
"""
Example 2: Search for affordable domains across registrars.

This example demonstrates how to search for domain names
based on business name and get pricing from multiple registrars.
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from src.domain_searcher import DomainSearcher
from src.price_optimizer import PriceOptimizer
from src.permission_gates import PermissionGates


def search_domain_example():
    """Example: Search for domains."""
    
    # Initialize components
    searcher = DomainSearcher()
    optimizer = PriceOptimizer()
    permissions = PermissionGates()
    
    # Business details
    business_name = "Summer Street Hair Salon"
    business_type = "Salon"
    max_price = 50.0
    
    print("\n" + "="*60)
    print("EXAMPLE 2: Search for Affordable Domains")
    print("="*60)
    
    # Step 1: Request permission to search
    print(f"\n🔍 Domain Search Details:")
    print(f"   Business: {business_name}")
    print(f"   Type: {business_type}")
    print(f"   Max Price: ${max_price:.2f}/year")
    print(f"   Preferred TLDs: .com, .io, .co")
    
    approved = permissions.request_approval(
        action="search_domain",
        details={
            "business_name": business_name,
            "business_type": business_type,
            "max_price": max_price
        }
    )
    
    if not approved:
        print("\n❌ Domain search cancelled")
        return {"success": False}
    
    # Step 2: Search for domains (simulated)
    print("\n⏳ Searching for domains...")
    
    # Simulate search results
    options = [
        {
            "domain": "summerstassalon.com",
            "price": 8.88,
            "registrar": "namecheap",
            "available": True
        },
        {
            "domain": "summerstreethouse.com",
            "price": 10.87,
            "registrar": "namecheap",
            "available": True
        },
        {
            "domain": "summerhaircuts.io",
            "price": 48.88,
            "registrar": "namecheap",
            "available": True
        },
        {
            "domain": "summerstassalon.io",
            "price": 45.00,
            "registrar": "porkbun",
            "available": True
        },
        {
            "domain": "summerstudio.co",
            "price": 19.88,
            "registrar": "namecheap",
            "available": True
        }
    ]
    
    # Filter by max price
    affordable = [o for o in options if o["price"] <= max_price]
    
    if affordable:
        print(f"\n✅ Found {len(affordable)} affordable domains:\n")
        
        for i, opt in enumerate(affordable[:5], 1):
            print(f"  {i}. {opt['domain']}")
            print(f"     Price: ${opt['price']:.2f}/year")
            print(f"     Registrar: {opt['registrar']}")
        
        # Show price comparison
        print(f"\n💰 Price Comparison:")
        comparison = optimizer.compare_prices(affordable[0]["domain"])
        print(f"   Cheapest: ${comparison['cheapest']['total_price']:.2f}")
        
        # Show best option
        best = affordable[0]
        print(f"\n🏆 Best Option:")
        print(f"   Domain: {best['domain']}")
        print(f"   Price: ${best['price']:.2f}/year")
        
        # Calculate cost with extras
        cost = optimizer.calculate_total_cost(
            domain=best["domain"],
            registrar=best["registrar"],
            years=1,
            privacy=True
        )
        print(f"   With Privacy: ${cost['total']:.2f}/year")
        
        return {
            "success": True,
            "options": affordable,
            "cheapest": best["domain"],
            "price": best["price"]
        }
    else:
        print(f"\n❌ No affordable domains found")
        return {"success": False}


if __name__ == "__main__":
    result = search_domain_example()
    print(f"\n📋 Result: {result}")
