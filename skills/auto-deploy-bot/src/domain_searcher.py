"""Domain searcher - Find affordable domains across registrars."""

import re
from typing import List, Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)


class DomainSearcher:
    """Searches for affordable domains across registrars."""
    
    def __init__(self):
        """Initialize domain searcher."""
        self.tld_preferences = {
            ".com": 1,
            ".io": 2,
            ".co": 3,
            ".net": 4,
            ".org": 5,
            ".app": 6
        }
    
    def search(
        self,
        business_name: str,
        business_type: str,
        preferred_tlds: List[str] = None,
        max_price: float = 50.0,
        registrars: List[str] = None
    ) -> List[Dict[str, Any]]:
        """Search for domains.
        
        Args:
            business_name: Business name
            business_type: Type of business
            preferred_tlds: Preferred TLDs in order
            max_price: Maximum price per year
            registrars: List of registrars to search
        
        Returns:
            List of domain options sorted by price
        """
        if preferred_tlds is None:
            preferred_tlds = [".com", ".io", ".co"]
        
        if registrars is None:
            registrars = ["namecheap", "porkbun"]
        
        # Generate domain suggestions
        suggestions = self._generate_suggestions(business_name, business_type)
        
        # Check availability and price for each suggestion
        options = []
        for domain in suggestions:
            for registrar in registrars:
                result = self._check_domain(domain, registrar, max_price)
                if result and result.get("available"):
                    options.append(result)
        
        # Sort by price
        options.sort(key=lambda x: x["price"])
        
        # Add rank
        for i, opt in enumerate(options):
            opt["rank"] = i + 1
        
        return options
    
    def _generate_suggestions(
        self,
        business_name: str,
        business_type: str
    ) -> List[str]:
        """Generate domain name suggestions.
        
        Args:
            business_name: Business name
            business_type: Type of business
        
        Returns:
            List of suggested domain names
        """
        suggestions = []
        
        # Clean business name
        clean_name = business_name.lower().strip()
        clean_name = re.sub(r'[^a-z0-9]', '', clean_name)
        
        # Clean business type
        clean_type = business_type.lower().strip()
        clean_type = re.sub(r'[^a-z0-9]', '', clean_type)
        
        # Variations
        variations = [
            clean_name,
            clean_name + clean_type,
            clean_type + clean_name,
        ]
        
        # Add TLD variations for each
        for tld in [".com", ".io", ".co", ".net", ".app"]:
            for var in variations:
                if len(var) >= 3:
                    suggestions.append(var + tld)
        
        return suggestions
    
    def _check_domain(
        self,
        domain: str,
        registrar: str,
        max_price: float
    ) -> Optional[Dict[str, Any]]:
        """Check domain availability and price.
        
        Args:
            domain: Domain name
            registrar: Registrar name
            max_price: Maximum acceptable price
        
        Returns:
            Domain info if available, None otherwise
        """
        # Import registrar module
        try:
            if registrar == "namecheap":
                from namecheap_api import NamecheapAPI
                api = NamecheapAPI()
                return api.check_domain(domain, max_price)
            elif registrar == "porkbun":
                from porkbun_api import PorkbunAPI
                api = PorkbunAPI()
                return api.check_domain(domain, max_price)
            elif registrar == "godaddy":
                from godaddy_api import GoDaddyAPI
                api = GoDaddyAPI()
                return api.check_domain(domain, max_price)
            else:
                # Default mock response
                return {
                    "domain": domain,
                    "available": True,
                    "price": 12.99,
                    "registrar": registrar
                }
        except Exception as e:
            logger.debug(f"Error checking domain {domain} on {registrar}: {e}")
            return None
    
    def rank_options(
        self,
        options: List[Dict[str, Any]],
        business_name: str
    ) -> List[Dict[str, Any]]:
        """Rank domain options by quality metrics.
        
        Args:
            options: List of domain options
            business_name: Business name for matching
        
        Returns:
            Ranked list of options
        """
        clean_name = business_name.lower().strip()
        clean_name = re.sub(r'[^a-z0-9]', '', clean_name)
        
        # Score each option
        scored = []
        for opt in options:
            score = self._score_domain(opt["domain"], clean_name)
            opt["quality_score"] = score
            scored.append(opt)
        
        # Sort by price, then by quality
        scored.sort(key=lambda x: (x["price"], -x["quality_score"]))
        
        return scored
    
    def _score_domain(self, domain: str, business_name: str) -> float:
        """Score a domain based on quality metrics.
        
        Args:
            domain: Domain name
            business_name: Business name
        
        Returns:
            Quality score (0-100)
        """
        score = 50.0  # Base score
        
        # Bonus for exact match
        if business_name in domain.lower():
            score += 30
        
        # Bonus for .com TLD
        if domain.endswith(".com"):
            score += 15
        
        # Bonus for shorter domain
        domain_part = domain.replace(".com", "").replace(".io", "").replace(".co", "")
        if len(domain_part) < 15:
            score += 5
        
        # Bonus for pronounceable (no hyphens, numbers)
        if "-" not in domain and not any(c.isdigit() for c in domain_part):
            score += 5
        
        return min(score, 100)
    
    def get_best_option(
        self,
        options: List[Dict[str, Any]]
    ) -> Optional[Dict[str, Any]]:
        """Get the best domain option.
        
        Args:
            options: List of domain options
        
        Returns:
            Best option or None
        """
        if not options:
            return None
        
        # Return cheapest
        return min(options, key=lambda x: x["price"])
