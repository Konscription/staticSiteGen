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
        
    def text_extract_markdown_images_does_not_find_links(self):
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        expected = []
        self.assertEqual(result,expected)

if __name__ == "__main__":
    unittest.main()