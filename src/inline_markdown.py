from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    outputNodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            outputNodes.append(node)
            continue
        split_nodes = []
        split_text = node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise ValueError(f"Invalid Markdown Syntax in {node.text}")
        for x in range(len(split_text)):
            #print(f"\n{split_text[x]}")
            if split_text[x] == "":
                continue
            if x % 2 == 0:
                split_nodes.append(TextNode(split_text[x],text_type_text))
            else:
                split_nodes.append(TextNode(split_text[x],text_type))
        outputNodes.extend(split_nodes)   
    return outputNodes