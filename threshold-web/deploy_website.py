#!/usr/bin/env python3
"""
Automatic Website Deployment to Netlify
Deploy website folder to temporary or permanent domain
"""

import os
import sys
import json
import subprocess
from datetime import datetime

NETLIFY_TOKEN = open('/home/clawdbot/.openclaw/workspace/.netlify_token').read().strip()
WORKSPACE = '/home/clawdbot/.openclaw/workspace'
DEPLOYMENTS_LOG = f'{WORKSPACE}/deployments_log.json'

def load_deployments_log():
    """Load deployment history"""
    if os.path.exists(DEPLOYMENTS_LOG):
        with open(DEPLOYMENTS_LOG, 'r') as f:
            return json.load(f)
    return {'deployments': []}

def save_deployments_log(log):
    """Save deployment history"""
    with open(DEPLOYMENTS_LOG, 'w') as f:
        json.dump(log, f, indent=2)

def deploy_to_temp_url(site_folder, site_name):
    """
    Deploy website to temporary Netlify URL
    
    Args:
        site_folder: Path to website folder (e.g., /path/to/bob-plumbing-site/)
        site_name: Site name (e.g., bob-plumbing-temp)
    
    Returns:
        Temporary URL (e.g., https://bob-plumbing-temp.netlify.app)
    """
    
    print()
    print("=" * 70)
    print(f"DEPLOYING TO TEMPORARY URL")
    print("=" * 70)
    print()
    print(f"Site folder: {site_folder}")
    print(f"Site name: {site_name}")
    print()
    
    if not os.path.exists(site_folder):
        print(f"✗ ERROR: Folder not found: {site_folder}")
        return None
    
    try:
        print("Deploying to Netlify...")
        
        # Deploy using netlify CLI
        result = subprocess.run([
            'netlify', 'deploy',
            '--auth', NETLIFY_TOKEN,
            '--dir', site_folder,
            '--site', site_name,
            '--prod'  # Make it production deployment
        ], capture_output=True, text=True, timeout=300)
        
        if result.returncode == 0:
            # Extract URL from output
            output = result.stdout
            print(output)
            
            # Temporary URL format
            temp_url = f"https://{site_name}.netlify.app"
            
            print()
            print("=" * 70)
            print("✓ DEPLOYMENT SUCCESSFUL")
            print("=" * 70)
            print(f"Temporary URL: {temp_url}")
            print()
            
            # Log deployment
            log = load_deployments_log()
            log['deployments'].append({
                'date': datetime.now().isoformat(),
                'type': 'temp',
                'site_name': site_name,
                'folder': site_folder,
                'url': temp_url,
                'status': 'active'
            })
            save_deployments_log(log)
            
            return temp_url
        else:
            print(f"✗ Deployment failed:")
            print(result.stderr)
            return None
    
    except subprocess.TimeoutExpired:
        print("✗ Deployment timeout (took longer than 5 minutes)")
        return None
    except Exception as e:
        print(f"✗ Deployment error: {e}")
        return None

def deploy_to_permanent(site_folder, site_id):
    """
    Deploy website to permanent domain
    
    Args:
        site_folder: Path to website folder
        site_id: Netlify site ID (from account)
    
    Returns:
        Boolean (success/failure)
    """
    
    print()
    print("=" * 70)
    print(f"DEPLOYING TO PERMANENT DOMAIN")
    print("=" * 70)
    print()
    print(f"Site folder: {site_folder}")
    print(f"Site ID: {site_id}")
    print()
    
    if not os.path.exists(site_folder):
        print(f"✗ ERROR: Folder not found: {site_folder}")
        return False
    
    try:
        print("Deploying to Netlify (permanent)...")
        
        result = subprocess.run([
            'netlify', 'deploy',
            '--auth', NETLIFY_TOKEN,
            '--dir', site_folder,
            '--site-id', site_id,
            '--prod'
        ], capture_output=True, text=True, timeout=300)
        
        if result.returncode == 0:
            output = result.stdout
            print(output)
            
            print()
            print("=" * 70)
            print("✓ PERMANENT DEPLOYMENT SUCCESSFUL")
            print("=" * 70)
            print()
            
            # Log deployment
            log = load_deployments_log()
            log['deployments'].append({
                'date': datetime.now().isoformat(),
                'type': 'permanent',
                'site_id': site_id,
                'folder': site_folder,
                'status': 'active'
            })
            save_deployments_log(log)
            
            return True
        else:
            print(f"✗ Deployment failed:")
            print(result.stderr)
            return False
    
    except subprocess.TimeoutExpired:
        print("✗ Deployment timeout")
        return False
    except Exception as e:
        print(f"✗ Deployment error: {e}")
        return False

def delete_temp_site(site_id):
    """
    Delete temporary site if customer doesn't pay
    
    Args:
        site_id: Netlify site ID
    
    Returns:
        Boolean (success/failure)
    """
    
    print()
    print("=" * 70)
    print(f"DELETING TEMPORARY SITE")
    print("=" * 70)
    print()
    print(f"Site ID: {site_id}")
    print()
    
    try:
        print("Deleting site from Netlify...")
        
        result = subprocess.run([
            'netlify', 'delete-site',
            '--auth', NETLIFY_TOKEN,
            '--site-id', site_id
        ], capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0:
            print("✓ SITE DELETED")
            print()
            
            # Log deletion
            log = load_deployments_log()
            for deployment in log['deployments']:
                if deployment.get('site_id') == site_id:
                    deployment['status'] = 'deleted'
            save_deployments_log(log)
            
            return True
        else:
            print(f"✗ Deletion failed:")
            print(result.stderr)
            return False
    
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 deploy_website.py temp <folder> <site-name>")
        print("    Deploy to temporary URL")
        print()
        print("  python3 deploy_website.py permanent <folder> <site-id>")
        print("    Deploy to permanent domain")
        print()
        print("  python3 deploy_website.py delete <site-id>")
        print("    Delete temporary site if no payment")
        print()
        print("Examples:")
        print("  python3 deploy_website.py temp ./bob-plumbing-site bob-plumbing-temp")
        print("  python3 deploy_website.py permanent ./bob-plumbing-site abc123def456")
        print("  python3 deploy_website.py delete temp-site-id")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == 'temp':
        if len(sys.argv) < 4:
            print("Error: Need folder and site name")
            print("Usage: python3 deploy_website.py temp <folder> <site-name>")
            sys.exit(1)
        
        folder = sys.argv[2]
        site_name = sys.argv[3]
        deploy_to_temp_url(folder, site_name)
    
    elif command == 'permanent':
        if len(sys.argv) < 4:
            print("Error: Need folder and site ID")
            print("Usage: python3 deploy_website.py permanent <folder> <site-id>")
            sys.exit(1)
        
        folder = sys.argv[2]
        site_id = sys.argv[3]
        deploy_to_permanent(folder, site_id)
    
    elif command == 'delete':
        if len(sys.argv) < 3:
            print("Error: Need site ID")
            print("Usage: python3 deploy_website.py delete <site-id>")
            sys.exit(1)
        
        site_id = sys.argv[2]
        delete_temp_site(site_id)
    
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
