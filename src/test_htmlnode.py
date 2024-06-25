import unittest

from htmlnode import HTMLNode, LeafNode


class testHTMLNode(unittest.TestCase):

    def test_props_to_html_output(self):
        node = HTMLNode(tag="a",children=[],props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(),' href="https://www.google.com" target="_blank"')

    def test_props_to_html_output_when_no_props(self):
        node = HTMLNode(tag="p",children=[])
        self.assertEqual(node.props_to_html(), '')
 

    def test_leafNode_to_html_render(self):
        node = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        node3 = LeafNode(None,value='Just text here.')
        self.assertEqual(node.to_html(),'<p>This is a paragraph of text.</p>')
        self.assertEqual(node2.to_html(),'<a href="https://www.google.com">Click me!</a>')
        self.assertEqual(node3.to_html(),'Just text here.')

if __name__ == "__main__":
    unittest.main()