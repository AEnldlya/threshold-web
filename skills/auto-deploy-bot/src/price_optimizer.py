"""Price optimizer - Compare prices and find best deals."""

from typing import Dict, List, Any, Optional
import logging

logger = logging.getLogger(__name__)


class PriceOptimizer:
    """Optimizes pricing across registrars."""
    
    def __init__(self):
        """Initialize price optimizer."""
        # Base prices for different registrars (sample data)
        self.base_prices = {
            "namecheap": {
                ".com": 8.88,
                ".io": 48.88,
                ".co": 19.88,
                ".net": 10.87,
                ".app": 14.88
            },
            "porkbun": {
                ".com": 8.74,
                ".io": 45.00,
                ".co": 19.00,
                ".net": 10.74,
                ".app": 14.00
            },
            "godaddy": {
                ".com": 12.99,
                ".io": 59.99,
                ".co": 24.99,
                ".net": 13.99,
                ".app": 19.99
            },
            "route53": {
                ".com": 12.00,
                ".io": 50.00,
                ".co": 20.00,
                ".net": 12.00,
                ".app": 15.00
            }
        }
        
        # Additional costs
        self.privacy_protection_cost = 2.99
        self.auto_renew_cost = 0.0  # Usually free
    
    def compare_prices(
        self,
        domain: str,
        registrars: List[str] = None,
        years: int = 1
    ) -> Dict[str, Any]:
        """Compare prices across registrars.
        
        Args:
            domain: Domain name
            registrars: List of registrars to compare
            years: Number of years
        
        Returns:
            Price comparison
        """
        if registrars is None:
            registrars = list(self.base_prices.keys())
        
        # Extract TLD from domain
        tld = self._get_tld(domain)
        
        prices = {}
        for registrar in registrars:
            if registrar in self.base_prices:
                base_price = self.base_prices[registrar].get(tld, 12.99)
                total_price = base_price * years
                
                prices[registrar] = {
                    "registrar": registrar,
                    "domain": domain,
                    "tld": tld,
                    "base_price": base_price,
                    "years": years,
                    "total_price": total_price
                }
        
        # Sort by price
        sorted_prices = sorted(
            prices.values(),
            key=lambda x: x["total_price"]
        )
        
        return {
            "domain": domain,
            "tld": tld,
            "years": years,
            "prices": sorted_prices,
            "cheapest": sorted_prices[0] if sorted_prices else None,
            "savings": self._calculate_savings(sorted_prices)
        }
    
    def calculate_total_cost(
        self,
        domain: str,
        registrar: str,
        years: int = 1,
        privacy: bool = False,
        auto_renew: bool = True
    ) -> Dict[str, float]:
        """Calculate total cost for domain registration.
        
        Args:
            domain: Domain name
            registrar: Registrar name
            years: Number of years
            privacy: Include privacy protection
            auto_renew: Include auto-renewal
        
        Returns:
            Cost breakdown
        """
        tld = self._get_tld(domain)
        
        if registrar not in self.base_prices:
            return {"error": f"Unknown registrar: {registrar}"}
        
        base_price = self.base_prices[registrar].get(tld, 12.99)
        domain_cost = base_price * years
        
        costs = {
            "domain_base": base_price,
            "years": years,
            "subtotal": domain_cost,
            "privacy_protection": 0.0,
            "auto_renew": 0.0,
            "total": domain_cost
        }
        
        if privacy:
            privacy_cost = self.privacy_protection_cost * years
            costs["privacy_protection"] = privacy_cost
            costs["total"] += privacy_cost
        
        if auto_renew:
            # Auto-renewal is usually free
            costs["auto_renew"] = self.auto_renew_cost
        
        return costs
    
    def find_cheapest_alternative(
        self,
        domain: str,
        max_price: float,
        registrars: List[str] = None
    ) -> Optional[Dict[str, Any]]:
        """Find cheapest alternative if domain exceeds max price.
        
        Args:
            domain: Original domain
            max_price: Maximum acceptable price
            registrars: List of registrars to check
        
        Returns:
            Cheapest option or None
        """
        comparison = self.compare_prices(domain, registrars)
        
        cheapest = comparison.get("cheapest")
        
        if cheapest and cheapest["total_price"] <= max_price:
            return cheapest
        
        return None
    
    def get_renewal_cost(
        self,
        domain: str,
        registrar: str,
        years: int = 1
    ) -> Dict[str, float]:
        """Get renewal cost for domain.
        
        Args:
            domain: Domain name
            registrar: Registrar name
            years: Number of years
        
        Returns:
            Renewal cost breakdown
        """
        tld = self._get_tld(domain)
        
        if registrar not in self.base_prices:
            return {"error": f"Unknown registrar: {registrar}"}
        
        base_price = self.base_prices[registrar].get(tld, 12.99)
        renewal_cost = base_price * years
        
        return {
            "domain": domain,
            "registrar": registrar,
            "base_price": base_price,
            "years": years,
            "renewal_cost": renewal_cost
        }
    
    def batch_cost_estimate(
        self,
        domains: List[str],
        registrar: str = "namecheap",
        privacy: bool = True
    ) -> Dict[str, Any]:
        """Estimate batch cost for multiple domains.
        
        Args:
            domains: List of domain names
            registrar: Registrar to use
            privacy: Include privacy protection
        
        Returns:
            Batch cost estimate
        """
        items = []
        total = 0.0
        
        for domain in domains:
            cost = self.calculate_total_cost(
                domain,
                registrar,
                years=1,
                privacy=privacy
            )
            
            item_total = cost.get("total", 0)
            total += item_total
            
            items.append({
                "domain": domain,
                "cost": item_total,
                "breakdown": cost
            })
        
        return {
            "items": items,
            "item_count": len(domains),
            "subtotal": total,
            "discount": 0.0,
            "total": total,
            "registrar": registrar,
            "privacy_included": privacy
        }
    
    def _get_tld(self, domain: str) -> str:
        """Extract TLD from domain.
        
        Args:
            domain: Domain name
        
        Returns:
            TLD (e.g., ".com")
        """
        parts = domain.split(".")
        if len(parts) >= 2:
            return "." + parts[-1]
        return ".com"
    
    def _calculate_savings(
        self,
        prices: List[Dict[str, Any]]
    ) -> Dict[str, float]:
        """Calculate savings between registrars.
        
        Args:
            prices: List of price data
        
        Returns:
            Savings information
        """
        if len(prices) < 2:
            return {"savings": 0, "percentage": 0}
        
        cheapest = prices[0]["total_price"]
        most_expensive = prices[-1]["total_price"]
        
        savings = most_expensive - cheapest
        percentage = (savings / most_expensive * 100) if most_expensive > 0 else 0
        
        return {
            "cheapest": cheapest,
            "most_expensive": most_expensive,
            "savings": savings,
            "savings_percentage": percentage,
            "cheapest_registrar": prices[0]["registrar"],
            "most_expensive_registrar": prices[-1]["registrar"]
        }
