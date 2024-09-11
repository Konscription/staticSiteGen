import unittest

from markdown_util import *


class TestMarkdownUtil(unittest.TestCase):

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
    
if __name__ == "__main__":
    unittest.main()