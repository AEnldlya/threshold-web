"""Vercel deployment manager."""

import subprocess
import json
import time
from typing import Dict, Any, Optional
import logging
import os

logger = logging.getLogger(__name__)


class VercelManager:
    """Manages Vercel deployments."""
    
    def __init__(self, vercel_token: Optional[str] = None):
        """Initialize Vercel manager.
        
        Args:
            vercel_token: Vercel API token (from env if not provided)
        """
        self.vercel_token = vercel_token or os.getenv("VERCEL_TOKEN")
        if not self.vercel_token:
            logger.warning("VERCEL_TOKEN not set. Some operations may fail.")
    
    def deploy(
        self,
        project_name: str,
        project_path: str,
        timeout: int = 300,
        prod: bool = True
    ) -> Dict[str, Any]:
        """Deploy project to Vercel.
        
        Args:
            project_name: Vercel project name
            project_path: Local path to project
            timeout: Deployment timeout in seconds
            prod: Deploy to production or preview
        
        Returns:
            Deployment result with status and URLs
        """
        try:
            # Check if project path exists
            import os
            if not os.path.isdir(project_path):
                return {
                    "success": False,
                    "error": f"Project path not found: {project_path}"
                }
            
            # Build deployment command
            cmd = ["vercel", "deploy", "--yes"]
            
            if not prod:
                cmd.append("--preview")
            
            env = os.environ.copy()
            if self.vercel_token:
                env["VERCEL_TOKEN"] = self.vercel_token
            
            # Run deployment
            start_time = time.time()
            result = subprocess.run(
                cmd,
                cwd=project_path,
                capture_output=True,
                text=True,
                timeout=timeout,
                env=env
            )
            deployment_time = int(time.time() - start_time)
            
            if result.returncode != 0:
                return {
                    "success": False,
                    "error": result.stderr or "Deployment failed"
                }
            
            # Parse output for deployment URL
            output = result.stdout
            preview_url = self._extract_url(output)
            
            if not preview_url:
                return {
                    "success": False,
                    "error": "Could not extract deployment URL"
                }
            
            logger.info(f"Deployed to {preview_url}")
            
            return {
                "success": True,
                "status": "deployed",
                "project_name": project_name,
                "preview_url": preview_url,
                "prod_url": preview_url if prod else None,
                "deployment_time": deployment_time,
                "timestamp": time.time()
            }
        
        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "error": f"Deployment timeout after {timeout} seconds"
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def _extract_url(self, output: str) -> Optional[str]:
        """Extract deployment URL from vercel CLI output.
        
        Args:
            output: CLI output
        
        Returns:
            Deployment URL or None
        """
        # Look for https:// URL in output
        import re
        urls = re.findall(r'https://[^\s]+\.vercel\.app[^\s]*', output)
        if urls:
            return urls[0]
        
        # Fallback: look for any https URL
        urls = re.findall(r'https://[^\s]+', output)
        if urls:
            return urls[0]
        
        return None
    
    def get_project_info(self, project_name: str) -> Dict[str, Any]:
        """Get Vercel project information.
        
        Args:
            project_name: Vercel project name
        
        Returns:
            Project information
        """
        try:
            cmd = ["vercel", "projects", "list", "--json"]
            
            env = os.environ.copy()
            if self.vercel_token:
                env["VERCEL_TOKEN"] = self.vercel_token
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                env=env
            )
            
            if result.returncode != 0:
                return {"success": False, "error": result.stderr}
            
            projects = json.loads(result.stdout)
            
            # Find project by name
            for project in projects.get("projects", []):
                if project.get("name") == project_name:
                    return {
                        "success": True,
                        "project": project
                    }
            
            return {
                "success": False,
                "error": f"Project not found: {project_name}"
            }
        
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def add_custom_domain(
        self,
        project_name: str,
        domain: str
    ) -> Dict[str, Any]:
        """Add custom domain to Vercel project.
        
        Args:
            project_name: Vercel project name
            domain: Domain to add
        
        Returns:
            Result with domain configuration
        """
        try:
            cmd = ["vercel", "domains", "add", domain, project_name]
            
            env = os.environ.copy()
            if self.vercel_token:
                env["VERCEL_TOKEN"] = self.vercel_token
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                env=env
            )
            
            if result.returncode != 0:
                return {
                    "success": False,
                    "error": result.stderr or "Failed to add domain"
                }
            
            return {
                "success": True,
                "domain": domain,
                "project": project_name
            }
        
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def get_deployment_status(
        self,
        project_name: str,
        deployment_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Get deployment status.
        
        Args:
            project_name: Vercel project name
            deployment_id: Specific deployment ID (optional)
        
        Returns:
            Deployment status
        """
        try:
            if deployment_id:
                cmd = ["vercel", "deployments", deployment_id]
            else:
                cmd = ["vercel", "deployments", project_name]
            
            cmd.append("--json")
            
            env = os.environ.copy()
            if self.vercel_token:
                env["VERCEL_TOKEN"] = self.vercel_token
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                env=env
            )
            
            if result.returncode != 0:
                return {
                    "success": False,
                    "error": result.stderr
                }
            
            deployment = json.loads(result.stdout)
            
            return {
                "success": True,
                "status": deployment.get("state"),
                "url": deployment.get("url"),
                "created_at": deployment.get("createdAt"),
                "updated_at": deployment.get("updatedAt")
            }
        
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def rollback_deployment(
        self,
        project_name: str,
        deployment_id: str
    ) -> Dict[str, Any]:
        """Rollback to a previous deployment.
        
        Args:
            project_name: Vercel project name
            deployment_id: Deployment ID to rollback to
        
        Returns:
            Rollback result
        """
        try:
            cmd = ["vercel", "deployments", "promote", deployment_id, "--yes"]
            
            env = os.environ.copy()
            if self.vercel_token:
                env["VERCEL_TOKEN"] = self.vercel_token
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                env=env
            )
            
            if result.returncode != 0:
                return {
                    "success": False,
                    "error": result.stderr
                }
            
            return {
                "success": True,
                "message": f"Promoted deployment {deployment_id}"
            }
        
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
