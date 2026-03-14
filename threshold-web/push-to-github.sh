#!/bin/bash
# Push threshold-web to GitHub
# Run this script in the threshold-web directory

REPO_URL="https://github.com/SkiRacer69/new-web.git"

echo "Setting up git..."
git init
git add .
git commit -m "Initial commit: Threshold Web upgraded"

echo "Adding remote..."
git remote add origin $REPO_URL

echo "Pushing to GitHub..."
git push -u origin main --force

echo "Done! Check your repo at: $REPO_URL"
