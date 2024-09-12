from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)


def markdown_to_blocks(markdown):
    segments = markdown.split("\n\n")
    output = []
    for segment in segments:
        if segment != "":
            segment = segment.strip()
            output.append(segment)
    return output