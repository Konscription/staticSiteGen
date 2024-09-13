from typing import List

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


