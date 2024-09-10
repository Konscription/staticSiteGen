import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

#function extract_markdown_images(text) 
# takes raw markdown text 
# returns a list of tuples. 
# - Each tuple should contain the alt text 
# and the URL of any markdown images.
#
# regex = r"!\[(.*?)\]\((.*?)\)"
#
# text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
# print(extract_markdown_images(text))
# [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
def extract_markdown_images(text):
    image_regex = r"!\[(.*?)\]\((.*?)\)"
    return re.findall(image_regex, text)

def extract_markdown_links(text):
    links_regex = r"(?<!!)\[(.*?)\]\((.*?)\)"
    return re.findall(links_regex, text)
