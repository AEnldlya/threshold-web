#!/bin/bash

# Simple form submission script using curl

PITCH="Hi there! We're a local Boston web design studio. We specialize in building professional websites for local businesses. Would you be interested in discussing a website redesign for your business? We typically build and deploy in 3-5 days for \$500. Let's chat!"

# Log file
LOG_FILE="form_submissions_log.txt"

# Function to submit form via curl
submit_form() {
    local business=$1
    local url=$2
    local contact_email=$3
    
    echo "[$(date)] Processing: $business ($url)" | tee -a "$LOG_FILE"
    
    # Try common contact form endpoints
    endpoints=(
        "$url/contact"
        "$url/contact-us"
        "$url/contact.php"
        "$url/send-message"
    )
    
    for endpoint in "${endpoints[@]}"; do
        echo "  Trying: $endpoint"
        
        # Try POST to contact form
        response=$(curl -s -X POST "$endpoint" \
            -d "name=Website Design Studio" \
            -d "email=hello@websiteagency.boston" \
            -d "message=$(echo "$PITCH" | sed 's/ /%20/g')" \
            2>&1)
        
        if [ $? -eq 0 ]; then
            echo "  ✓ Submitted to $endpoint" | tee -a "$LOG_FILE"
            break
        fi
    done
    
    # Wait 5 minutes before next submission
    sleep 300
}

# List of businesses
declare -a businesses=(
    "McNally Plumbing & Heating|https://mcnallyplumbing.com|contact@mcnallyplumbing.com"
    "Downtown Cleaning Services|https://downtowncleaningservices.com|contact@downtownclean.com"
    "Harbor Auto Repair|https://harborautorepair.com|harborauto@gmail.com"
    "Bright Dental Studio|https://brightdental.boston|info@brightdental.boston"
)

echo "🤖 Starting form submissions...\n" | tee -a "$LOG_FILE"

for entry in "${businesses[@]}"; do
    IFS='|' read -r name url email <<< "$entry"
    submit_form "$name" "$url" "$email"
done

echo "\n✓ Form submissions complete. Check $LOG_FILE for details." | tee -a "$LOG_FILE"
