import re


def format_content(content):
    # Define a regular expression pattern to identify headings
    heading_pattern = re.compile(r'\*\*([^*]+)\*\*')
    
    # Replace each heading with a new line after it
    formatted_content = heading_pattern.sub(r'\n\n\1 ', content)

    return formatted_content
