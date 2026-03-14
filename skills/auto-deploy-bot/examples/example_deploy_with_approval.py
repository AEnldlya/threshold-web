#!/usr/bin/env python3
"""
Example 1: Simple deployment to Vercel with approval gate.

This example shows how to deploy a website to Vercel
with human approval before the deployment happens.
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from src.vercel_manager import VercelManager
from src.permission_gates import PermissionGates
from src.state_manager import StateManager


def deploy_with_approval_example():
    """Example: Deploy website with approval."""
    
    # Initialize components
    permissions = PermissionGates()
    vercel = VercelManager()
    state = StateManager("example-deployment")
    
    # Website details
    website_id = "my-website-2026"
    project_path = "/workspace/my-website"
    vercel_project_name = "my-website"
    
    print("\n" + "="*60)
    print("EXAMPLE 1: Deploy to Vercel with Approval")
    print("="*60)
    
    # Step 1: Request approval
    print(f"\n📋 Deployment Details:")
    print(f"   Website ID: {website_id}")
    print(f"   Project Path: {project_path}")
    print(f"   Vercel Project: {vercel_project_name}")
    
    approved = permissions.request_approval(
        action="deploy_to_vercel",
        details={
            "project": vercel_project_name,
            "path": project_path,
            "timeout": 300
        }
    )
    
    if not approved:
        print("\n❌ Deployment cancelled by user")
        return {"success": False}
    
    # Step 2: Deploy
    print("\n⏳ Deploying to Vercel...")
    result = vercel.deploy(
        project_name=vercel_project_name,
        project_path=project_path,
        timeout=300
    )
    
    if result.get("success"):
        preview_url = result.get("preview_url")
        state.save_step("deployed", result)
        
        print(f"\n✅ Deployment Successful!")
        print(f"   URL: {preview_url}")
        print(f"   Time: {result.get('deployment_time', 0)}s")
        
        # Get status
        status = state.get_status()
        print(f"\n📊 Workflow Status:")
        print(f"   Status: {status['status']}")
        print(f"   Steps Completed: {len(status['completed_steps'])}")
        
        return {"success": True, "url": preview_url}
    else:
        print(f"\n❌ Deployment Failed: {result.get('error')}")
        return {"success": False}


if __name__ == "__main__":
    result = deploy_with_approval_example()
    print(f"\n📋 Result: {result}")
