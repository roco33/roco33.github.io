#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import re
from datetime import datetime

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def extract_title_and_content(markdown_content):
    lines = markdown_content.strip().split('\n')
    if lines and lines[0].startswith('#'):
        title = lines[0].lstrip('#').strip()
        content_lines = lines[1:]
    else:
        title = "每日思考：认知与理解"
        content_lines = lines
    
    # Remove empty lines at the beginning
    while content_lines and not content_lines[0].strip():
        content_lines.pop(0)
    
    # Convert to HTML paragraphs
    html_content = ""
    for line in content_lines:
        if line.strip():
            html_content += f"<p>{line.strip()}</p>"
    
    return title, html_content

def main():
    if len(sys.argv) != 4:
        print("Usage: generate_article_literary.py <draft_file> <template_file> <output_file>")
        sys.exit(1)
    
    draft_file = sys.argv[1]
    template_file = sys.argv[2]
    output_file = sys.argv[3]
    
    # Get current date info
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    datetime_str = now.strftime("%Y-%m-%dT04:00:00+08:00")
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    date_path = f"{year}/{month}/{day}"
    
    # Read draft content
    draft_content = read_file(draft_file)
    title, html_content = extract_title_and_content(draft_content)
    
    # Read template
    template_content = read_file(template_file)
    
    # Replace placeholders
    result = template_content
    result = result.replace("{{TITLE}}", title)
    result = result.replace("{{CONTENT}}", html_content)
    result = result.replace("{{DATE}}", date_str)
    result = result.replace("{{DATETIME}}", datetime_str)
    result = result.replace("{{DATE_PATH}}", date_path)
    result = result.replace("{{YEAR}}", year)
    
    # For now, use fixed values for description and keywords
    result = result.replace("{{DESCRIPTION}}", "AI生成的深度思考文章")
    result = result.replace("{{KEYWORDS}}", "哲学,认知,知识")
    
    # Count posts and tags (simplified - you might want to make this more dynamic)
    result = result.replace("{{POST_COUNT}}", "2")
    result = result.replace("{{TAG_COUNT}}", "5")
    
    # Write output
    write_file(output_file, result)
    print(f"Generated literary-style article: {output_file}")

if __name__ == "__main__":
    main()