#!/usr/bin/env python3
import os
import datetime
import sys

def check_root_directory():
    """Check if script is being run from the root directory of the website."""
    if not os.path.isdir("content/post"):
        print("Error: Script must be run from the root directory containing 'content/post'")
        print("Current directory:", os.getcwd())
        sys.exit(1)

def main():
    check_root_directory()
    # Prompt for file name
    file_name = input("Enter the file name (without .md): ").strip()
    if not file_name:
        print("File name cannot be empty.")
        return
    if not file_name.endswith('.md'):
        file_name = file_name + '.md'

    # Prompt for title
    title = input("Enter the post title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return

    today = datetime.date.today().strftime('%Y-%m-%d')
    frontmatter = f"""---
date: {today}
title: \"{title}\"
draft: true
tags: []
---\n\n"""

    directory = 'content/post/'
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, file_name)

    if os.path.exists(filepath):
        print(f"Error: {filepath} already exists.")
        return

    with open(filepath, 'w') as f:
        f.write(frontmatter)

    print(f"Created new post: {filepath}")

if __name__ == "__main__":
    main()
