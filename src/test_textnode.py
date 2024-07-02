import unittest

from textnode import *


class testTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_neq_url(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold", "https://www.test.com")
        self.assertNotEqual(node, node2)

    def test_neq_text_type(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italics")
        self.assertNotEqual(node, node2)

    def test_neq_text(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is another text node", "bold")
        self.assertNotEqual(node, node2)

    def test_url_is_None(self):
        node = TextNode("This is a text node", "bold")
        self.assertIsNone(node.url)

    def test_url_is_not_None(self):
        node = TextNode("This is a text node", "bold", "http://www.testing.com")
        self.assertIsNotNone(node.url)

    def test_empty_text(self):
        node = TextNode("","bold")
        self.assertEqual(node.text, "")
    
    def test_empty_text_and_type(self):
        node = TextNode("","")
        self.assertEqual(node.text,"")
        self.assertEqual(node.text_type,"")


    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        expected = [TextNode("This is text with a ", text_type_text),
                    TextNode("code block", text_type_code),
                    TextNode(" word", text_type_text)]
        self.assertEqual(new_nodes,expected)

    def test_split_nodes_delimiter_bold(self):
        node = TextNode("This is text with a **bold** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        expected = [TextNode("This is text with a ", text_type_text),
                    TextNode("bold", text_type_bold),
                    TextNode(" word", text_type_text)]
        self.assertEqual(new_nodes,expected)

    def test_split_nodes_delimiter_raises_error(self):
        node = TextNode("This is text with a **missing ending delimiter", text_type_text)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", text_type_bold)

if __name__ == "__main__":
    unittest.main()