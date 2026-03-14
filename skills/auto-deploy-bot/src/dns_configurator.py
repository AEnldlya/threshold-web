"""DNS configurator - Configure DNS records and verify propagation."""

from typing import Dict, Any, List, Optional
import logging
import time
import dns.resolver
import dns.exception

logger = logging.getLogger(__name__)


class DNSConfigurator:
    """Manages DNS configuration and verification."""
    
    def __init__(self):
        """Initialize DNS configurator."""
        self.vercel_ips = [
            "76.76.19.165",
            "76.76.19.166",
            "76.76.19.167",
            "76.76.19.168"
        ]
    
    def get_vercel_records(self, project_name: str) -> List[Dict[str, str]]:
        """Get DNS records needed for Vercel deployment.
        
        Args:
            project_name: Vercel project name
        
        Returns:
            List of DNS records to configure
        """
        return [
            {
                "type": "CNAME",
                "name": "www",
                "value": "cname.vercel-dns.com",
                "ttl": 3600
            },
            {
                "type": "A",
                "name": "@",
                "value": "76.76.19.165",
                "ttl": 3600
            }
        ]
    
    def configure(
        self,
        domain: str,
        registrar: str,
        vercel_project: str
    ) -> Dict[str, Any]:
        """Configure DNS for a domain pointing to Vercel.
        
        Args:
            domain: Domain name
            registrar: Registrar name
            vercel_project: Vercel project name
        
        Returns:
            Configuration result
        """
        try:
            from registrar_manager import RegistrarManager
            
            records = self.get_vercel_records(vercel_project)
            manager = RegistrarManager()
            
            result = manager.set_dns_records(domain, registrar, records)
            
            if result.get("success"):
                logger.info(f"DNS configured for {domain}")
                # Start verification in background
                time.sleep(5)  # Wait before checking
                verify_result = self.verify_propagation(domain)
                return {
                    "success": True,
                    "domain": domain,
                    "records": records,
                    "verification": verify_result
                }
            else:
                return {
                    "success": False,
                    "error": result.get("error", "Configuration failed")
                }
        
        except Exception as e:
            logger.error(f"Error configuring DNS: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def verify_propagation(
        self,
        domain: str,
        max_attempts: int = 5,
        timeout: int = 30
    ) -> Dict[str, Any]:
        """Verify DNS propagation.
        
        Args:
            domain: Domain name
            max_attempts: Maximum verification attempts
            timeout: Timeout between attempts
        
        Returns:
            Verification result
        """
        for attempt in range(max_attempts):
            try:
                logger.info(f"Checking DNS propagation for {domain} (attempt {attempt + 1})")
                
                # Try to resolve domain
                answers = dns.resolver.resolve(domain, "A")
                
                if answers:
                    ips = [rdata.to_text() for rdata in answers]
                    
                    # Check if any Vercel IP is in results
                    vercel_ip_found = any(ip in self.vercel_ips for ip in ips)
                    
                    return {
                        "success": True,
                        "domain": domain,
                        "propagated": vercel_ip_found,
                        "ips": ips,
                        "attempt": attempt + 1,
                        "message": "DNS propagated" if vercel_ip_found else "DNS resolved but Vercel IP not found"
                    }
            
            except (dns.exception.DNSException, Exception) as e:
                logger.debug(f"DNS not yet propagated: {e}")
                
                if attempt < max_attempts - 1:
                    logger.info(f"Waiting {timeout}s before retry...")
                    time.sleep(timeout)
        
        return {
            "success": False,
            "domain": domain,
            "propagated": False,
            "message": "DNS did not propagate in time",
            "attempts": max_attempts
        }
    
    def get_current_records(self, domain: str) -> Dict[str, Any]:
        """Get current DNS records for a domain.
        
        Args:
            domain: Domain name
        
        Returns:
            Current DNS records
        """
        try:
            records = {
                "a_records": [],
                "cname_records": [],
                "mx_records": [],
                "txt_records": []
            }
            
            # Get A records
            try:
                a_answers = dns.resolver.resolve(domain, "A")
                records["a_records"] = [rdata.to_text() for rdata in a_answers]
            except dns.exception.DNSException:
                pass
            
            # Get CNAME records
            try:
                cname_answers = dns.resolver.resolve(f"www.{domain}", "CNAME")
                records["cname_records"] = [rdata.to_text() for rdata in cname_answers]
            except dns.exception.DNSException:
                pass
            
            # Get MX records
            try:
                mx_answers = dns.resolver.resolve(domain, "MX")
                records["mx_records"] = [rdata.to_text() for rdata in mx_answers]
            except dns.exception.DNSException:
                pass
            
            # Get TXT records
            try:
                txt_answers = dns.resolver.resolve(domain, "TXT")
                records["txt_records"] = [rdata.to_text() for rdata in txt_answers]
            except dns.exception.DNSException:
                pass
            
            return {
                "success": True,
                "domain": domain,
                "records": records
            }
        
        except Exception as e:
            logger.error(f"Error getting DNS records: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def check_ssl_certificate(self, domain: str) -> Dict[str, Any]:
        """Check SSL certificate status for domain.
        
        Args:
            domain: Domain name
        
        Returns:
            SSL certificate info
        """
        try:
            import ssl
            import socket
            
            context = ssl.create_default_context()
            conn = socket.create_connection((domain, 443), timeout=5)
            ssock = context.wrap_socket(conn, server_hostname=domain)
            
            cert = ssock.getpeercert()
            ssock.close()
            
            return {
                "success": True,
                "domain": domain,
                "has_certificate": True,
                "subject": cert.get("subject"),
                "issuer": cert.get("issuer"),
                "version": cert.get("version")
            }
        
        except (socket.gaierror, socket.timeout, ssl.SSLError) as e:
            logger.debug(f"SSL certificate error for {domain}: {e}")
            return {
                "success": False,
                "domain": domain,
                "has_certificate": False,
                "error": str(e)
            }
    
    def wait_for_propagation(
        self,
        domain: str,
        max_wait: int = 600
    ) -> Dict[str, Any]:
        """Wait for DNS to propagate and SSL to be ready.
        
        Args:
            domain: Domain name
            max_wait: Maximum wait time in seconds
        
        Returns:
            Ready status
        """
        start_time = time.time()
        
        while time.time() - start_time < max_wait:
            # Check DNS
            dns_result = self.verify_propagation(domain, max_attempts=1)
            if dns_result.get("propagated"):
                # Check SSL
                ssl_result = self.check_ssl_certificate(domain)
                if ssl_result.get("success"):
                    return {
                        "success": True,
                        "domain": domain,
                        "ready": True,
                        "wait_time": int(time.time() - start_time)
                    }
            
            wait_interval = min(30, max_wait - int(time.time() - start_time))
            if wait_interval > 0:
                time.sleep(wait_interval)
        
        return {
            "success": False,
            "domain": domain,
            "ready": False,
            "error": f"Domain did not become ready within {max_wait} seconds"
        }
