"""Registrar manager - Unified interface for all domain registrars."""

from typing import Dict, Any, Optional
import logging
import os

logger = logging.getLogger(__name__)


class RegistrarManager:
    """Manages interactions with domain registrars."""
    
    def __init__(self):
        """Initialize registrar manager."""
        self.registrars = {
            "namecheap": self._get_namecheap_instance(),
            "porkbun": self._get_porkbun_instance(),
            "godaddy": self._get_godaddy_instance(),
            "route53": self._get_route53_instance()
        }
    
    def _get_namecheap_instance(self):
        """Get Namecheap API instance."""
        try:
            from namecheap_api import NamecheapAPI
            return NamecheapAPI(
                api_key=os.getenv("NAMECHEAP_API_KEY"),
                api_user=os.getenv("NAMECHEAP_API_USER")
            )
        except ImportError:
            logger.warning("Namecheap API not available")
            return None
    
    def _get_porkbun_instance(self):
        """Get Porkbun API instance."""
        try:
            from porkbun_api import PorkbunAPI
            return PorkbunAPI(
                api_key=os.getenv("PORKBUN_API_KEY"),
                secret_key=os.getenv("PORKBUN_SECRET_API_KEY")
            )
        except ImportError:
            logger.warning("Porkbun API not available")
            return None
    
    def _get_godaddy_instance(self):
        """Get GoDaddy API instance."""
        try:
            from godaddy_api import GoDaddyAPI
            return GoDaddyAPI(
                api_key=os.getenv("GODADDY_API_KEY"),
                api_secret=os.getenv("GODADDY_API_SECRET")
            )
        except ImportError:
            logger.warning("GoDaddy API not available")
            return None
    
    def _get_route53_instance(self):
        """Get Route53 API instance."""
        try:
            from route53_api import Route53API
            return Route53API(
                access_key=os.getenv("AWS_ACCESS_KEY_ID"),
                secret_key=os.getenv("AWS_SECRET_ACCESS_KEY")
            )
        except ImportError:
            logger.warning("Route53 API not available")
            return None
    
    def check_availability(self, domain: str, registrar: str) -> Dict[str, Any]:
        """Check domain availability.
        
        Args:
            domain: Domain name
            registrar: Registrar name
        
        Returns:
            Availability info
        """
        if registrar not in self.registrars:
            return {
                "success": False,
                "error": f"Unknown registrar: {registrar}"
            }
        
        api = self.registrars.get(registrar)
        if not api:
            return {
                "success": False,
                "error": f"Registrar not configured: {registrar}"
            }
        
        try:
            return api.check_availability(domain)
        except Exception as e:
            logger.error(f"Error checking availability on {registrar}: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def check_price(self, domain: str, registrar: str) -> Dict[str, Any]:
        """Check domain price.
        
        Args:
            domain: Domain name
            registrar: Registrar name
        
        Returns:
            Price info
        """
        if registrar not in self.registrars:
            return {
                "success": False,
                "error": f"Unknown registrar: {registrar}"
            }
        
        api = self.registrars.get(registrar)
        if not api:
            return {
                "success": False,
                "error": f"Registrar not configured: {registrar}"
            }
        
        try:
            return api.check_price(domain)
        except Exception as e:
            logger.error(f"Error checking price on {registrar}: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def purchase_domain(
        self,
        domain: str,
        registrar: str,
        years: int = 1,
        auto_renew: bool = True,
        privacy: bool = True,
        email: Optional[str] = None
    ) -> Dict[str, Any]:
        """Purchase a domain.
        
        Args:
            domain: Domain name
            registrar: Registrar name
            years: Number of years to register
            auto_renew: Enable auto-renewal
            privacy: Enable privacy protection
            email: Email for domain contact
        
        Returns:
            Purchase confirmation
        """
        if registrar not in self.registrars:
            return {
                "success": False,
                "error": f"Unknown registrar: {registrar}"
            }
        
        api = self.registrars.get(registrar)
        if not api:
            return {
                "success": False,
                "error": f"Registrar not configured: {registrar}"
            }
        
        try:
            logger.info(f"Purchasing {domain} on {registrar}")
            return api.purchase_domain(
                domain=domain,
                years=years,
                auto_renew=auto_renew,
                privacy=privacy,
                email=email
            )
        except Exception as e:
            logger.error(f"Error purchasing domain on {registrar}: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def set_dns_records(
        self,
        domain: str,
        registrar: str,
        records: list
    ) -> Dict[str, Any]:
        """Set DNS records for a domain.
        
        Args:
            domain: Domain name
            registrar: Registrar name
            records: List of DNS records
        
        Returns:
            Configuration result
        """
        if registrar not in self.registrars:
            return {
                "success": False,
                "error": f"Unknown registrar: {registrar}"
            }
        
        api = self.registrars.get(registrar)
        if not api:
            return {
                "success": False,
                "error": f"Registrar not configured: {registrar}"
            }
        
        try:
            logger.info(f"Setting DNS records for {domain} on {registrar}")
            return api.set_dns_records(domain, records)
        except Exception as e:
            logger.error(f"Error setting DNS records on {registrar}: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def get_dns_records(self, domain: str, registrar: str) -> Dict[str, Any]:
        """Get DNS records for a domain.
        
        Args:
            domain: Domain name
            registrar: Registrar name
        
        Returns:
            DNS records
        """
        if registrar not in self.registrars:
            return {
                "success": False,
                "error": f"Unknown registrar: {registrar}"
            }
        
        api = self.registrars.get(registrar)
        if not api:
            return {
                "success": False,
                "error": f"Registrar not configured: {registrar}"
            }
        
        try:
            return api.get_dns_records(domain)
        except Exception as e:
            logger.error(f"Error getting DNS records on {registrar}: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def get_supported_registrars(self) -> list:
        """Get list of supported registrars.
        
        Returns:
            List of registrar names
        """
        return list(self.registrars.keys())
    
    def get_configured_registrars(self) -> list:
        """Get list of configured registrars.
        
        Returns:
            List of configured registrar names
        """
        return [
            name for name, api in self.registrars.items() if api is not None
        ]
