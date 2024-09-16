import re
from typing import List,Tuple
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ulist = "unordered_list"
block_type_olist = "ordered_list"


def markdown_to_blocks(markdown: str) -> List[str]:
    """takes a raw Markdown string (representing a full document)
    as input and returns a list of "block" strings.

    Args:
        markdown (str): a full document of markdown text

    Returns:
        List[str]: returns a list of string block's
    """    
    segments = markdown.split("\n\n")
    output = []
    for segment in segments:
        if segment != "":
            segment = segment.strip()
            output.append(segment)
    return output

def block_to_block_type(block: str) -> str:
    """given a block of markdown text and determine what type of block it is.
        support for 6 types of markdown blocks:
            paragraph
            heading
            code
            quote
            unordered_list
            ordered_list
    Args:
        block (str): tring of block markdown text

    Returns:
        str: returns a string representing the type of markdown block text given
            e.g.(paragraph,heading,code,quote,unordered_list,ordered_list)
    """    
    if is_heading(block):
        return block_type_heading
    if is_code(block):
        return block_type_code
    if is_quote(block):
        return block_type_quote
    if is_ordered_list(block):
        return block_type_olist
    if is_unordered_list(block):
        return block_type_ulist
    return block_type_paragraph

def is_heading(block: str) -> bool:
    if (
        block.startswith('# ') or
        block.startswith('## ') or
        block.startswith('### ') or
        block.startswith('#### ') or
        block.startswith('##### ') or
        block.startswith('###### ')
        ):
        return True
    return False

def is_code(block: str) -> bool:
    if block.startswith("```"):
        if block.endswith("```"):
            return True
    return False

def is_quote(block: str) -> bool:
    lines = block.split("\n")
    for line in lines:
        if not line.startswith(">"):
            return False
    return True

def is_ordered_list(block: str) -> bool:
    """Every line in an ordered list block must start 
    with a number followed by a . character and a space. 
    The number must start at 1 and increment by 1 for each line.

    Args:
        block (str): input string of a block of markdown text.

    Returns:
        bool: return true if each line is an number sequence starting with 1 
            otherwise returns false
    """
    lines = block.split("\n")
    order_start = 1
    for line in lines:
        if not line.startswith(f"{order_start}. "):
            return False
        order_start += 1
    return True

def is_unordered_list(block: str) -> bool:
    """Every line in an unordered list block must start 
        with a * or - character, followed by a space.
        
    Args:
        block (str): input string of a block of markdown text.

    Returns:
        bool: return true if all lines start with '* ' or '- '
                otherwise returns false
    """
    lines = block.split("\n")
    for line in lines:
        if not line.startswith("* ") and not line.startswith("- "):
            return False
    return True

    #split markdown into blocks
    #loop over each block
    #   determine the type of block
    #   based on the type of block, create a new HTMLNode with proper data
    #   assign the proper child HTMLNode objects to the block node. 
    #       created a shared text_to_children(text) function that works for all block 
    #           types takes a string of text and returns a list of HTMLNodes that 
    #           represent the inline markdown using previously created functions
    #make all the block nodes Children under a single parent HTML node (which should 
    #   just be a div) and return it.
    
def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        children.append(block_to_htmlnode(block,block_type))
    return ParentNode("div", children)
        

def block_to_htmlnode(block: str, block_type: str) -> HTMLNode:
    return_node = None
    match block_type:         
        case "heading":
            tag, value = get_heading_info(block)
            return_node = ParentNode(tag,text_to_children(value))
        case "quote":
            tag, value = get_quote_info(block)
            return_node = ParentNode(tag,text_to_children(value))
        case "code":
            tag, value = get_code_info(block)
            return_node = ParentNode("pre",[LeafNode(tag,value)])
        case "unordered_list":
            tag, children = get_ulist_info(block)
            return_node = ParentNode(tag,children)
        case "ordered_list":
            tag, children = get_olist_info(block)
            return_node = ParentNode(tag,children)
        case _:
            return_node = ParentNode("p",text_to_children(block))
    return return_node
   
def text_to_children(text: str) -> List[HTMLNode]:
    return [text_node_to_html_node(node) for node in text_to_textnodes(text)]

def get_heading_info(block: str) -> Tuple[str,str]:
    regex_pattern = r"^#{1,6} "
    matches = re.findall(regex_pattern,block)
    if len(matches) > 1 or len(matches) < 1:
        print("Issue with Heading Syntax")
    return f"h{matches[0].count('#')}",block[len(matches[0]):]

def get_quote_info(block: str) -> Tuple[str,str]:
    tag = "blockquote"
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line[1:])
    value = "\n".join(new_lines)
    return tag, value
    
def get_code_info(block: str) -> Tuple[str,str]:
    tag = "code"
    return tag, block.lstrip().rstrip()[3:-3]

def get_ulist_info(block: str) -> Tuple[str,List[ParentNode]]:
    tag = "ul"
    list_nodes = []
    lines = block.split('\n')
    for line in lines:
        list_nodes.append(ParentNode("li",text_to_children(line.lstrip()[2:])))
    return tag, list_nodes

def get_olist_info(block: str) -> Tuple[str,List[ParentNode]]:
    tag = "ol"
    list_nodes = []
    order_start = 1
    lines = block.split('\n')
    for line in lines:
        order = f"{order_start}. "
        list_nodes.append(ParentNode("li",text_to_children(line.lstrip()[len(order)])))
        order_start += 1
    return tag, list_nodes