import unittest
from inline_markdown import *

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word", text_type_text),
            ],
            new_nodes,)

    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text)
            ], 
            new_nodes,)

    def test_split_nodes_delimiter_bold(self):
        node = TextNode("This is text with a **bold** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bold", text_type_bold),
                TextNode(" word", text_type_text)
            ],
            new_nodes,)

    def test_split_nodes_delimiter_raises_error(self):
        node = TextNode("This is text with a **missing ending delimiter", text_type_text)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", text_type_bold)

    def test_delim_bold_double(self):
        node = TextNode("This is text with a **bolded** word and **another**", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,)

    def test_delim_bold_multiword(self):
        node = TextNode("This is text with a **bolded word** and **another**", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded word", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,)

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
            new_nodes,)

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("bold", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("italic", text_type_italic),
            ],
            new_nodes,)

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ],
            new_nodes,)


    def test_extract_markdown_images_finds_matches(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertListEqual(result,expected)

    def test_extract_markdown_images_does_not_find_matches(self):
        text = "this is `code` markdown"
        result = extract_markdown_images(text)
        expected = []
        self.assertEqual(result,expected)
        
    def test_extract_markdown_images_does_not_find_links(self):
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        expected = []
        self.assertEqual(result,expected)
        
    def test_extract_markdown_images_Mixed_links_and_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif")]
        self.assertEqual(result,expected)
    
    
    def test_extract_markdown_link_finds_matches(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(text)
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(result,expected)
        
    def test_extract_markdown_link_does_not_find_matches(self):
        text = "this is `code` markdown"
        result = extract_markdown_links(text)
        expected = []
        self.assertEqual(result,expected)
    
    def test_extract_markdown_link_does_not_find_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_links(text)
        expected = []
        self.assertEqual(result,expected)
    
    def test_extract_markdown_link_mixed_links_and_images(self):
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_links(text)
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif")]
        self.assertEqual(result,expected)


    def test_split_nodes_image_has_images(self):
        node = TextNode(
            "This is text with a image ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            text_type_text,)
        result = split_nodes_image([node])
        expected = [
            TextNode("This is text with a image ", text_type_text),
            TextNode("rick roll", text_type_image, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", text_type_text),
            TextNode("obi wan", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"),]
        self.assertListEqual(result,expected)

    def test_split_nodes_image_has_no_images(self):
        node = TextNode(
            "This is text with a image [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            text_type_text,)
        result = split_nodes_image([node])
        expected = [TextNode(
            "This is text with a image [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            text_type_text,)]
        self.assertListEqual(result,expected)   
        
    def test_split_nodes_image_just_one_image(self):
        node = TextNode("![rick roll](https://i.imgur.com/aKaOqIh.gif)",text_type_text)
        result = split_nodes_image([node])
        expected = [TextNode("rick roll", text_type_image, "https://i.imgur.com/aKaOqIh.gif")]
        self.assertListEqual(result,expected)
        
    def test_split_nodes_image_trailing_text(self):
        node = TextNode("![rick roll](https://i.imgur.com/aKaOqIh.gif) rolled",text_type_text)
        result = split_nodes_image([node])
        expected = [TextNode("rick roll", text_type_image, "https://i.imgur.com/aKaOqIh.gif"),
                    TextNode(" rolled",text_type_text)]
        self.assertListEqual(result,expected)
    
    def test_split_nodes_image_no_alt_text_image(self):
        node = TextNode("![](https://i.imgur.com/aKaOqIh.gif)",text_type_text)
        result = split_nodes_image([node])
        expected = [TextNode("", text_type_image, "https://i.imgur.com/aKaOqIh.gif")]
        self.assertListEqual(result,expected)
    

if __name__ == "__main__":
    unittest.main()