block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def markdown_to_blocks(markdown):
    segments = markdown.split("\n\n")
    output = []
    for segment in segments:
        if segment != "":
            segment = segment.strip()
            output.append(segment)
    return output

def block_to_block_type(block):
    if is_heading(block):
        return block_type_heading
    if is_code(block):
        return block_type_code
    if is_quote(block):
        return block_type_quote
    return block_type_paragraph

def is_heading(block):
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

def is_code(block):
    if block[0:3] == "```":
        if block[-3:] == "```":
            return True
    return False

def is_quote(block):
    lines = block.split("\n")
    for line in lines:
        if line[0:1] != ">":
            return False
    return True

def is_unordered_list(block):
    pass

def is_ordered_list(block):
    pass
