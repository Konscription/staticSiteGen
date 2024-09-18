from textnode import TextNode
from file_system_utilities import copy_dir
#IMPORT AND USE IT
#In Python, if you want to use code from one file in another, you need to import it. In main.py, import the TextNode class from textnode.py:
#
#from textnode import TextNode
#
#Next, create a main() function that creates a new TextNode object with some dummy values. Print the object, and make sure it looks like you'd expect. 
# #For example, my code printed:
#
#TextNode(This is a text node, bold, https://www.boot.dev)
#
def main():
    #node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    #print(node)  
    source = r"./static/"
    destination = r"./public/"    
    copy_dir(source, destination)

main()
