#!/bin/bash
# Auto-push script for new-web repository
# Usage: ./auto-push.sh "commit message"

REPO_URL="https://github.com/SkiRacer69/new-web.git"
COMMIT_MSG="${1:-Update website files}"

cd /home/clawdbot/.openclaw/workspace

# Add all changes
git add -A

# Check if there are changes to commit
if git diff --cached --quiet; then
    echo "No changes to commit"
    exit 0
fi

# Commit
git commit -m "$COMMIT_MSG"

# Push (requires GitHub token setup)
# To enable automatic push, run:
# git config --global credential.helper store
# Then manually push once and enter credentials
git push new-web main

echo "✅ Changes pushed to $REPO_URL"