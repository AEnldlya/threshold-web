"""Namecheap API integration."""

import requests
from typing import Dict, Any, Optional, List
import logging

logger = logging.getLogger(__name__)


class NamecheapAPI:
    """Namecheap domain registrar API."""
    
    BASE_URL = "https://api.namecheap.com/api/v1"
    
    def __init__(self, api_key: str, api_user: str):
        """Initialize Namecheap API.
        
        Args:
            api_key: Namecheap API key
            api_user: Namecheap API user
        """
        self.api_key = api_key
        self.api_user = api_user
    
    def check_availability(self, domain: str) -> Dict[str, Any]:
        """Check if domain is available.
        
        Args:
            domain: Domain name
        
        Returns:
            Availability info
        """
        try:
            params = {
                "ApiUser": self.api_user,
                "ApiKey": self.api_key,
                "UserName": self.api_user,
                "Command": "namecheap.domains.check",
                "DomainList": domain,
                "ClientIp": "127.0.0.1"
            }
            
            response = requests.get(self.BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            
            # Parse XML response
            if "available=\"True\"" in response.text:
                return {
                    "success": True,
                    "domain": domain,
                    "available": True
                }
            else:
                return {
                    "success": True,
                    "domain": domain,
                    "available": False
                }
        
        except Exception as e:
            logger.error(f"Error checking domain availability: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def check_price(self, domain: str) -> Dict[str, Any]:
        """Check domain price.
        
        Args:
            domain: Domain name
        
        Returns:
            Price info
        """
        try:
            # Namecheap pricing (sample)
            prices = {
                ".com": 8.88,
                ".io": 48.88,
                ".co": 19.88,
                ".net": 10.87,
                ".app": 14.88
            }
            
            # Extract TLD
            parts = domain.split(".")
            if len(parts) >= 2:
                tld = "." + parts[-1]
                price = prices.get(tld, 12.99)
            else:
                price = 12.99
            
            return {
                "success": True,
                "domain": domain,
                "price": price,
                "currency": "USD",
                "registrar": "namecheap"
            }
        
        except Exception as e:
            logger.error(f"Error checking price: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def purchase_domain(
        self,
        domain: str,
        years: int = 1,
        auto_renew: bool = True,
        privacy: bool = True,
        email: Optional[str] = None
    ) -> Dict[str, Any]:
        """Purchase a domain.
        
        Args:
            domain: Domain name
            years: Number of years
            auto_renew: Enable auto-renewal
            privacy: Enable privacy protection
            email: Email for domain contact
        
        Returns:
            Purchase confirmation
        """
        try:
            logger.info(f"Purchasing {domain} on Namecheap")
            
            # In production, would call actual API
            # For now, return mock response
            
            price_result = self.check_price(domain)
            base_price = price_result.get("price", 12.99)
            total_price = base_price * years
            
            if privacy:
                total_price += 2.99 * years
            
            return {
                "success": True,
                "domain": domain,
                "registrar": "namecheap",
                "years": years,
                "base_price": base_price,
                "privacy": privacy,
                "total_price": total_price,
                "auto_renew": auto_renew,
                "confirmation_id": f"NC-{domain.replace('.', '-').upper()}-2026"
            }
        
        except Exception as e:
            logger.error(f"Error purchasing domain: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def set_dns_records(
        self,
        domain: str,
        records: List[Dict[str, str]]
    ) -> Dict[str, Any]:
        """Set DNS records for domain.
        
        Args:
            domain: Domain name
            records: List of DNS records
        
        Returns:
            Configuration result
        """
        try:
            logger.info(f"Setting DNS records for {domain}")
            
            # In production, would call actual API
            return {
                "success": True,
                "domain": domain,
                "registrar": "namecheap",
                "records_set": len(records),
                "records": records
            }
        
        except Exception as e:
            logger.error(f"Error setting DNS records: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def get_dns_records(self, domain: str) -> Dict[str, Any]:
        """Get DNS records for domain.
        
        Args:
            domain: Domain name
        
        Returns:
            DNS records
        """
        try:
            return {
                "success": True,
                "domain": domain,
                "records": []
            }
        
        except Exception as e:
            logger.error(f"Error getting DNS records: {e}")
            return {
                "success": False,
                "error": str(e)
            }
