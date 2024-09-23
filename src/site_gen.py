from file_system_utilities import read_file, write_file
from block_markdown import markdown_to_html_node

def extract_title(markdown: str) -> str:
    """pulls the h1 header from the markdown passed to the function.
    if there is no h1 header, an exception is raised.

    Args:
        markdown (str): markdown formated string
        
    Raises:
        ValueError: No title header found in passed arg.
        
    Returns:
        str: the h1 header text without the #  or leading white space.
    """
    lines = markdown.split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith("# "):
            return line[2:]
    raise ValueError("Error: No title header found.")

def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    markdown = read_file(from_path)
    template_html = read_file(template_path)
    
    html_string = markdown_to_html_node(markdown).to_html()  
    title = extract_title(markdown)
    
    new_html = template_html.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
    
    write_file(new_html, dest_path)
    
    

        