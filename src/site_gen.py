import os
import shutil
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
    """Generate an HTML page from markdown using a template html and a markdown file. 
    write the resulting file to destination.

    Args:
        from_path (str): source path to markdown file
        template_path (str): path to template html file
        dest_path (str): path to destination html file
    """    
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    markdown = read_file(from_path)
    template_html = read_file(template_path)
    
    html_string = markdown_to_html_node(markdown).to_html()  
    title = extract_title(markdown)
    
    new_html = template_html.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
    
    write_file(new_html, dest_path)
    
def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str) -> None:
        
        content_dirs = os.listdir(dir_path_content)
        for entry in content_dirs:
            full_path = os.path.join(dir_path_content,entry)
            if os.path.isfile(full_path):
                dest_path = os.path.join(dest_dir_path,entry.replace(".md",".html"))
                if entry.endswith(".md"):
                    generate_page(full_path,template_path, dest_path)
                
            elif os.path.isdir(full_path):
                new_dest_dir_path = os.path.join(dest_dir_path,entry)                
                generate_pages_recursive(full_path, template_path, new_dest_dir_path)

        
