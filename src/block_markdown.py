import re
from typing import List,Tuple
from htmlnode import HTMLNode

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

def markdown_to_html_node(markdown: str) -> HTMLNode:
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
    blocks = markdown_to_blocks(markdown)
    
    for block in blocks:
        block_type = block_to_block_type(block)
        
        
        
def block_to_htmlnode(block: str, block_type: str) -> HTMLNode:
    if block_type == block_type_paragraph:
        return HTMLNode("p",None,text_to_children(block))
    if block_type == block_type_heading:
        tag, value = get_heading_info(block)
        return HTMLNode(tag,None,text_to_children(value))
    if block_type == block_type_quote:
        tag, value = get_quote_info(block)
        return HTMLNode(tag,None,text_to_children(value))
    if block_type == block_type_code:
        tag, value = get_code_info(block)
        return HTMLNode("pre",None,[HTMLNode(tag,value)])
    if block_type == block_type_ulist:
        tag, value = get_ulist_info(block)
    if block_type == block_type_olist:
        pass
   
def text_to_children(text: str) -> List[HTMLNode]:
    pass   
 
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
    return tag, block[3:-3]

def get_ulist_info(block: str) -> Tuple[str,str]:
    pass

def get_olist_info(block: str) -> Tuple[str,str]:
    pass