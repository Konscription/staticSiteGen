import unittest
from block_markdown import *

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

class TestBlockMarkdown(unittest.TestCase):
    
    def test_markdown_to_blocks(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

        result = markdown_to_blocks(markdown)
        expected = [
            "# This is a heading",
            """This is a paragraph of text. It has some **bold** and *italic* words inside of it.""",
            """* This is the first list item in a list block
* This is a list item
* This is another list item""",
        ]
        self.assertListEqual(result,expected)
        
        
    def test_markdown_to_blocks_extra_lines(self):
        markdown = """ first line


last line"""
        result = markdown_to_blocks(markdown)
        expected = [
            "first line",
            "last line",
        ]
        self.assertListEqual(result,expected)
        
    