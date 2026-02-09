#!/bin/bash

# Daily Reflection Blog Post Publisher - Literary Edition
# This script handles the complete publishing workflow for daily reflection posts with literary styling

set -e

echo "Starting daily reflection publish workflow (Literary Edition)..."

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

# Generate HTML file using Python template engine with literary styling
python3 /home/admin/clawd/scripts/generate_article_literary.py \
    "/home/admin/clawd/daily_reflection_draft.md" \
    "/home/admin/clawd/scripts/article_template_literary.html" \
    "$POST_DIR/index.html"

echo "✓ Created post directory structure"
echo "✓ Generated HTML article with literary styling"

# Update homepage with literary design
echo "Updating homepage..."
cp /home/admin/clawd/index.html.new /home/admin/clawd/index.html

# Clean up draft
rm -f "/home/admin/clawd/daily_reflection_draft.md"

echo "✓ Daily reflection published successfully!"
echo "Post URL: https://roco33.github.io/$YEAR/$MONTH/$DAY/daily-reflection/"

exit 0