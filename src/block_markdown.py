import re
from typing import List

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


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
        return block_type_ordered_list
    if is_unordered_list(block):
        return block_type_unordered_list
    return block_type_paragraph

def is_heading(block: str) -> bool:
    if block[0:2] == '# ':
        return True
    if block[0:3] == '## ':
        return True
    if block[0:4] == '### ':
        return True
    if block[0:5] == '#### ':
        return True
    if block[0:6] == '##### ':
        return True
    if block[0:7] == '###### ':
        return True
    return False

def is_code(block: str) -> bool:
    if block[0:3] == "```":
        if block[-3:] == "```":
            return True
    return False

def is_quote(block: str) -> bool:
    lines = block.split("\n")
    for line in lines:
        if line[0:1] != ">":
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
    pattern = r"^\b(\d*)\. "
    order_start = 1
    for line in lines:
        order_value = re.findall(pattern,line)
        if len(order_value) <= 0:
            return False
        if int(order_value[0]) != order_start:
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
        if line[0:2] != "* " and line[0:2] != "- ":
            return False
    return True


