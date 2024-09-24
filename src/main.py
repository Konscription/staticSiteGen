from site_gen import generate_page, generate_pages_recursive
from file_system_utilities import copy_static_dir

def main():
    source = r"./static/"
    destination = r"./public/"
    markdown_path = r"./content/"
    template_path = r"./template.html"
    gen_dest_path = r"./public/"
    
    copy_static_dir(source, destination) 
    generate_pages_recursive(markdown_path,template_path,gen_dest_path)

main()
