#!/usr/bin/env python3
import os
import datetime
import re
import sys

def check_root_directory():
    """Check if script is being run from the root directory of the website."""
    if not os.path.isdir("content/soc"):
        print("Error: Script must be run from the root directory containing 'content/soc'")
        print("Current directory:", os.getcwd())
        sys.exit(1)
    print("Running from correct root directory")

def get_next_post_number(directory='content/soc/'):
    """Get the next post number in hexadecimal sequence."""
    # List all files in the directory
    try:
        files = os.listdir(directory)
    except FileNotFoundError:
        os.makedirs(directory, exist_ok=True)
        return "0001"
    
    # Filter for markdown files with hex pattern
    hex_files = [f for f in files if re.match(r'^[0-9A-F]+\.md$', f)]
    
    if not hex_files:
        return "0001"
    
    # Extract numbers and find the highest
    max_num = 0
    for filename in hex_files:
        hex_part = filename.split('.')[0]
        try:
            num = int(hex_part, 16)
            max_num = max(max_num, num)
        except ValueError:
            continue
    
    # Generate next number
    next_num = max_num + 1
    next_hex = format(next_num, '04X')  # Format as 4-digit hex
    
    return next_hex

def create_post():
    """Create a new post with the next number and today's date."""
    # First check if we're in the right directory
    check_root_directory()
    
    next_hex = get_next_post_number()
    today = datetime.date.today().strftime('%Y-%m-%d')
    
    # Create content with frontmatter
    content = f"""---
date: {today}
---
"""
    
    # Create the file
    directory = 'content/soc/'
    os.makedirs(directory, exist_ok=True)
    
    filename = f"{next_hex}.md"
    filepath = os.path.join(directory, filename)
    
    with open(filepath, 'w') as f:
        f.write(content)
    
    print(f"Created new post: {filepath}")
    print(f"Next post number: {next_hex}")

if __name__ == "__main__":
    create_post()