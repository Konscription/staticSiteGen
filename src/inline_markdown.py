import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
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

def split_nodes_image(old_nodes):
    outputNodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            outputNodes.append(node)
            continue
        running_text = node.text
        split_images = extract_markdown_images(running_text)
        if len(split_images) == 0:
            outputNodes.append(node)
            continue
        
        for image in split_images:
            sections = running_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                outputNodes.append(TextNode(sections[0], text_type_text))
            outputNodes.append(TextNode(image[0],text_type_image,image[1]))
            running_text = sections[1]
        if running_text != "":
            outputNodes.append(TextNode(running_text, text_type_text))
    return outputNodes          

def split_nodes_link(old_nodes):
    outputNodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            outputNodes.append(node)
            continue
        running_text = node.text
        split_links = extract_markdown_links(running_text)
        if len(split_links) == 0:
            outputNodes.append(node)
            continue
        
        for link in split_links:
            sections = running_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                outputNodes.append(TextNode(sections[0], text_type_text))
            outputNodes.append(TextNode(link[0],text_type_link,link[1]))
            running_text = sections[1]
        if running_text != "":
            outputNodes.append(TextNode(running_text, text_type_text))
    return outputNodes 

def extract_markdown_images(text):
    image_regex = r"!\[(.*?)\]\((.*?)\)"
    return re.findall(image_regex, text)

def extract_markdown_links(text):
    links_regex = r"(?<!!)\[(.*?)\]\((.*?)\)"
    return re.findall(links_regex, text)

def text_to_textnodes(text):    
    output_list = [TextNode(text,text_type_text)]
    if "**" in text:#bold in text
        output_list = split_nodes_delimiter(output_list,'**',text_type_bold)
    if "*" in text:#italic in text
        output_list = split_nodes_delimiter(output_list,'*',text_type_italic)
    if "`" in text:#code in text
        output_list = split_nodes_delimiter(output_list,'`',text_type_code)
    if "![" in text:#image in text
        output_list = split_nodes_image(output_list)
    if "[" in text:#link in text
        output_list = split_nodes_link(output_list)
    return output_list
    
        