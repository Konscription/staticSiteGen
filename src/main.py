from site_gen import generate_page, generate_pages_recursive
from file_system_utilities import copy_static_dir

def main():
    source = r"./static/"
    destination = r"./public/"
    markdown_path = r"./content/index.md"
    template_path = r"./template.html"
    gen_dest_path = r"./public/index.html"
    
    copy_static_dir(source, destination) #deletes destination, then recreates and copys from source
    
    #generate_page(markdown_path, template_path, gen_dest_path)
    generate_pages_recursive("./content/",template_path,"./public/")

main()
