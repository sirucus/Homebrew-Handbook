import os
import re

# Configuration
INPUT_FILE = 'bulk_import.txt'
DELIMITER = '###FILE:'

def sanitize_filename(name):
    """Removes illegal characters from filenames."""
    name = name.strip()
    return re.sub(r'[\\/*?:"<>|]', "", name)

def split_markdown():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found.")
        return

    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    current_file = None
    file_content = []
    file_count = 0

    for line in lines:
        if line.startswith(DELIMITER):
            # If we have a file open, save it before starting a new one
            if current_file:
                with open(f"{current_file}.md", 'w', encoding='utf-8') as out:
                    out.writelines(file_content)
                file_count += 1
                print(f"Created: {current_file}.md")

            # Reset for the new file
            raw_name = line.replace(DELIMITER, "").strip()
            current_file = sanitize_filename(raw_name)
            file_content = [] # Reset content buffer
        else:
            # If we are currently inside a file block, add the line
            if current_file:
                file_content.append(line)

    # Save the very last file found
    if current_file and file_content:
        with open(f"{current_file}.md", 'w', encoding='utf-8') as out:
            out.writelines(file_content)
        file_count += 1
        print(f"Created: {current_file}.md")

    print(f"--- Complete! Split {file_count} items. ---")

if __name__ == "__main__":
    split_markdown()