import unittest

from site_gen import extract_title

class testSiteGen(unittest.TestCase):
    
    def test_extract_title_valid(self):
        markdown = """# this is a title

the new lori ipsum is great.

## something something darkside

then there was sand, we hate sand.        
"""
        result = extract_title(markdown)
        expected = 'this is a title'
        self.assertEqual(result, expected)

    def test_extract_title_valid_leading_Spaces(self):
        markdown = """      # this is a title

the new lori ipsum is great.

## something something darkside

then there was sand, we hate sand.        
"""
        result = extract_title(markdown)
        expected = 'this is a title'
        self.assertEqual(result, expected)
        
    def test_extract_title_raises_error(self):
        markdown = """this is not a title

the new lori ipsum is great.

## something something darkside

then there was sand, we hate sand.        
"""
        with self.assertRaises(ValueError):
            extract_title(markdown)



if __name__ == "__main__":
    unittest.main()