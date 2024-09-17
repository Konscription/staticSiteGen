import unittest
from block_markdown import *

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
          
    
    def test_block_to_block_type_heading1(self):
        block = "# heading"
        result = block_to_block_type(block)
        expected = block_type_heading
        self.assertEqual(result,expected)
        
    def test_block_to_block_type_heading2(self):
        block = "## heading"
        result = block_to_block_type(block)
        expected = block_type_heading
        self.assertEqual(result,expected)

    def test_block_to_block_type_heading3(self):
        block = "### heading"
        result = block_to_block_type(block)
        expected = block_type_heading
        self.assertEqual(result,expected)
        
    def test_block_to_block_type_heading4(self):
        block = "#### heading"
        result = block_to_block_type(block)
        expected = block_type_heading
        self.assertEqual(result,expected)
        
    def test_block_to_block_type_heading5(self):
        block = "##### heading"
        result = block_to_block_type(block)
        expected = block_type_heading
        self.assertEqual(result,expected)
        
    def test_block_to_block_type_heading6(self):
        block = "###### heading"
        result = block_to_block_type(block)
        expected = block_type_heading
        self.assertEqual(result,expected)
        
    def test_block_to_block_type_heading7_fail(self):
        block = "####### heading"
        result = block_to_block_type(block)
        expected = block_type_paragraph
        self.assertEqual(result,expected)
        
    def test_block_to_block_type_code(self):
        block = """``` def main():
        print("hello world")```"""
        result = block_to_block_type(block)
        expected = block_type_code
        self.assertEqual(result,expected)

    def test_block_to_block_type_quote(self):
        block = """>I'm a dude
>playing a dude
>dressed as another dude."""
        result = block_to_block_type(block)
        expected = block_type_quote
        self.assertEqual(result,expected)
        
    def test_block_to_block_type_quote_fail(self):
        block = """>I'm a dude
 playing a dude
>dressed as another dude."""
        result = block_to_block_type(block)
        expected = block_type_paragraph
        self.assertEqual(result,expected)
        
    def test_block_to_block_type_ordered_list(self):
        block = """1. first
2. second
3. third
4. forth
5. fith"""
        result = block_to_block_type(block)
        expected = block_type_olist
        self.assertEqual(result,expected)        
    
    def test_block_to_block_type_ordered_list_fail(self):
        block = """1. first
2. second
 third
4. forth
5. fith"""
        result = block_to_block_type(block)
        expected = block_type_paragraph
        self.assertEqual(result,expected)        
     
    def test_block_to_block_type_unordered_list_asterisk(self):
        block = """* eggs
* bacon
* flour
* grapes
* milk"""
        result= block_to_block_type(block)
        expected = block_type_ulist
        self.assertEqual(result,expected)
        
    def test_block_to_block_type_unordered_list_dash(self):
        block = """- eggs
- bacon
- flour
- grapes
- milk"""
        result= block_to_block_type(block)
        expected = block_type_ulist
        self.assertEqual(result,expected)
 
    def test_block_to_block_type_unordered_list_mixed(self):
        block = """* eggs
- bacon
* flour
- grapes
* milk"""
        result= block_to_block_type(block)
        expected = block_type_ulist
        self.assertEqual(result,expected)
 
    def test_block_to_block_type_unordered_list_fail(self):
        block = """eggs
- bacon
* flour
- grapes
* milk"""
        result= block_to_block_type(block)
        expected = block_type_paragraph
        self.assertEqual(result,expected)
        
        
    def test_get_heading_info(self):
        block1 = "# heading"
        block2 = "## heading"
        block3 = "### heading"
        block4 = "#### heading"
        block5 = "##### heading"
        block6 = "###### heading"
        result1 = get_heading_info(block1)
        result2 = get_heading_info(block2)
        result3 = get_heading_info(block3)
        result4 = get_heading_info(block4)
        result5 = get_heading_info(block5)
        result6 = get_heading_info(block6)
        expected1 = "h1","heading"
        expected2 = "h2","heading"
        expected3 = "h3","heading"
        expected4 = "h4","heading"
        expected5 = "h5","heading"
        expected6 = "h6","heading"
        self.assertEqual(result1,expected1)
        self.assertEqual(result2,expected2)
        self.assertEqual(result3,expected3)
        self.assertEqual(result4,expected4)
        self.assertEqual(result5,expected5)
        self.assertEqual(result6,expected6)

    def test_get_quote_info(self):
        block = """>quote
>quote2
>quote3"""
        result = get_quote_info(block)
        expected = "blockquote","""quote
quote2
quote3"""
        self.assertEqual(result,expected)
        
    def test_get_code_info(self):
        block = """```
def code_block():
    print("hello world")
```"""
        result = get_code_info(block)
        expected = "code", """
def code_block():
    print("hello world")
"""
        self.assertEqual(result,expected)
        
    def test_get_ulist_info(self):
        block = """* item1
* item2
* item3
* item4"""
        result = get_ulist_info(block)
        expected = "ul", [ParentNode("li",[LeafNode(None,"item1")]),
                          ParentNode("li",[LeafNode(None,"item2")]),
                          ParentNode("li",[LeafNode(None,"item3")]),
                          ParentNode("li",[LeafNode(None,"item4")])]
        self.assertEqual(result,expected)
        
    def test_get_ulist_info_embeded_markdown(self):
        block = """* *item1* with extra text
* **item2**
* item3
* item4"""
        result = get_ulist_info(block)
        expected = "ul", [ParentNode("li",[LeafNode("i","item1"),LeafNode(None," with extra text")]),
                          ParentNode("li",[LeafNode("b","item2")]),
                          ParentNode("li",[LeafNode(None,"item3")]),
                          ParentNode("li",[LeafNode(None,"item4")])]
        self.assertEqual(result,expected)
        
    def test_get_olist_info(self):
        block = """1. item1
2. item2
3. item3
4. item4"""
        result = get_olist_info(block)
        expected = "ol", [ParentNode("li",[LeafNode(None,"item1")]),
                          ParentNode("li",[LeafNode(None,"item2")]),
                          ParentNode("li",[LeafNode(None,"item3")]),
                          ParentNode("li",[LeafNode(None,"item4")])
                        ]
        self.assertEqual(result,expected)
        
    def test_get_olist_info_embeded_markdown(self):
        block = """1. *item1* with extra text
2. **item2**
3. item3
4. item4"""
        result = get_olist_info(block)
        expected = "ol", [ParentNode("li",[LeafNode("i","item1"),LeafNode(None," with extra text")]),
                          ParentNode("li",[LeafNode("b","item2")]),
                          ParentNode("li",[LeafNode(None,"item3")]),
                          ParentNode("li",[LeafNode(None,"item4")])]
        self.assertEqual(result,expected)
        

    def test_text_to_children(self):
        text = "The **big** red dog ran *away* from tom."
        result = text_to_children(text)
        expected = [LeafNode(None,"The "),
                    LeafNode("b","big"),
                    LeafNode(None, " red dog ran "),
                    LeafNode("i","away"),
                    LeafNode(None," from tom.")
                    ]
        self.assertEqual(result,expected)
       

    def test_block_to_htmlnode_heading(self):
        block = "## heading2"
        result = block_to_htmlnode(block, block_type_heading)
        expected = ParentNode("h2",[LeafNode(None,"heading2")])
        self.assertEqual(result,expected)
    
    def test_block_to_htmlnode_quote(self):
        block = """>quote
>quote2
>quote3"""
        result = block_to_htmlnode(block, block_type_quote)
        expected = ParentNode("blockquote",[LeafNode(None,"""quote
quote2
quote3""")])
        self.assertEqual(result,expected)
    
    def test_block_to_htmlnode_code(self):
        block = """```
def code():
    print("hello world")   
```"""
        result = block_to_htmlnode(block, block_type_code)
        expected = ParentNode("pre",[LeafNode("code","""
def code():
    print("hello world")   
""")])
        self.assertEqual(result,expected)       
    
    def test_block_to_htmlnode_unordered_list(self):
        block = """* item1
* item2
* item3
* item4"""
        result = block_to_htmlnode(block, block_type_ulist)
        expected = ParentNode("ul", [ParentNode("li",[LeafNode(None,"item1")]),
                                      ParentNode("li",[LeafNode(None,"item2")]),
                                      ParentNode("li",[LeafNode(None,"item3")]),
                                      ParentNode("li",[LeafNode(None,"item4")])]
                               )
        self.assertEqual(result,expected)
    
    def test_block_to_htmlnode_ordered_list(self):
         block = """1. item1
2. item2
3. item3
4. item4"""
         result = block_to_htmlnode(block, block_type_olist)
         expected = ParentNode("ol", [ParentNode("li",[LeafNode(None,"item1")]),
                                      ParentNode("li",[LeafNode(None,"item2")]),
                                      ParentNode("li",[LeafNode(None,"item3")]),
                                      ParentNode("li",[LeafNode(None,"item4")])]
                               )
         self.assertEqual(result,expected)    
    
    def test_block_to_htmlnode_paragraph(self):
        block = """This is some paragraph text.
Another line of paragraph text."""
        result = block_to_htmlnode(block, block_type_paragraph)
        expected = ParentNode("p",[LeafNode(None,"""This is some paragraph text.
Another line of paragraph text.""")])
        self.assertEqual(result,expected)  
        
        
    def test_markdown_to_html_node(self):
        markdown = """# front-end development is the worst

        Look, front-end development is for script kiddies and soydevs who can't handle the real programming. I mean,
        it's just a bunch of divs and spans, right? And css??? It's like, "Oh, I want this to be red, but not thaaaaat
        red." What a joke.

        Real programmers code, not silly markup languages. They code on Arch Linux, not Mac OS, and certainly not
        Windows. They use Vim, not VS Code. They use C, not HTML. Come to the ![backend](https://www.boot.dev), where the real programming happens."""
        result = markdown_to_html_node(markdown)
        print(result)
        expected = ParentNode("div",[
            ParentNode("h1",[LeafNode(None,"front-end development is the worst")]),
            ParentNode("p",[LeafNode(None,"""Look, front-end development is for script kiddies and soydevs who can't handle the real programming. I mean,
        it's just a bunch of divs and spans, right? And css??? It's like, "Oh, I want this to be red, but not thaaaaat
        red." What a joke.""")]),
            ParentNode("p",[LeafNode(None,"""Real programmers code, not silly markup languages. They code on Arch Linux, not Mac OS, and certainly not
        Windows. They use Vim, not VS Code. They use C, not HTML. Come to the """),
                            LeafNode("img",'',{'src': "https://www.boot.dev", 'alt': "backend"}),
                            LeafNode(None,""", where the real programming happens.""", None)], None)], None)
        self.assertEqual(result,expected)   
    