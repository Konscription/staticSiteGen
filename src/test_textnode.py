import unittest

from textnode import TextNode


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


if __name__ == "__main__":
    unittest.main()