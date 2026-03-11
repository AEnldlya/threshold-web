#!/bin/bash

# Create a ZIP file
zip -r site.zip index.html

# Upload to Netlify using API
# This requires a NETLIFY_AUTH_TOKEN
echo "To deploy to Netlify, you can:"
echo ""
echo "Option 1: Visit https://app.netlify.com/drop"
echo "And drag & drop the site.zip file"
echo ""
echo "Option 2: Use Netlify CLI with authentication:"
echo "netlify deploy --prod --dir=."
echo ""
echo "Files are ready in: /home/clawdbot/.openclaw/workspace/haplink-deploy/"
