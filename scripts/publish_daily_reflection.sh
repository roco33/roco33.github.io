#!/bin/bash

# Daily Reflection Blog Post Publisher
# This script handles the complete publishing workflow for daily reflection posts

set -e

echo "Starting daily reflection publish workflow..."

# Get current date
DATE=$(date +"%Y-%m-%d")
YEAR=$(date +"%Y")
MONTH=$(date +"%m")
DAY=$(date +"%d")

echo "Date: $DATE"

# Check if draft exists
if [ ! -f "/home/admin/clawd/daily_reflection_draft.md" ]; then
    echo "Error: No draft file found!"
    exit 1
fi

# Create post directory structure
POST_DIR="/home/admin/clawd/$YEAR/$MONTH/$DAY/daily-reflection"
echo "Post directory: $POST_DIR"

mkdir -p "$POST_DIR"

# Move draft to post directory
cp "/home/admin/clawd/daily_reflection_draft.md" "$POST_DIR/index.md"
echo "✓ Created post directory structure"
echo "✓ Moved draft to post directory"

# Update homepage
echo "Updating homepage..."
/home/admin/clawd/scripts/update_homepage.sh

# Clean up draft
rm -f "/home/admin/clawd/daily_reflection_draft.md"

echo "✓ Daily reflection published successfully!"
echo "Post URL: https://roco33.github.io/$YEAR/$MONTH/$DAY/daily-reflection/"

exit 0