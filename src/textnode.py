from htmlnode import LeafNode
from typing import Type
text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TextNode:
    """Model to represent types of inline text for parsing Markdown"""    
    def __init__(self, text: str, text_type: str, url: str = None):
        """Constructor with 3 properties
            current expected text types are: (Normal text,Bold text,Italic text,Code text,Links,Images)
        Args:
            text (str): The text content of the node
            text_type (str): The type of text this node contains, e.g.( "bold" or "italic" )
            url (str, optional): The URL of the link or image, if the text is a link. Defaults to None.
        """        
        self.text = text 
        self.text_type = text_type 
        self.url = url

    def __eq__(self, other: Type['TextNode']) -> bool:
        """compare two text nodes, and evaluate if they are equal.
        
        Args:
            other (TextNode): other TextNode object to compare

        Returns:
            bool: true if objects values are the same, false otherwise
        """        
        if not isinstance(other, TextNode):
            return False
        return (
            self.text == other.text 
            and self.text_type == other.text_type 
            and self.url == other.url
        )
    
    def __repr__(self) -> str:  
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    """convert a TextNode to an HTMLNode
        will convert them to a subclass of HTMLNode, namely a LeafNode
    Args:
        text_node (TextNode): a TextNode to convert
    Raises:
        ValueError: Raised when a TextNode has an invalid text type

    Returns:
        LeafNode: a HTMLNode with no children and the correct tag and values
                    for the text type of the given TextNode
    """    
    text_type = text_node.text_type
    text = text_node.text
    if text_type == "text":
        return LeafNode(None,text)
    if text_type == "bold":
        return LeafNode("b",text)
    if text_type == "italic":
        return LeafNode("i",text)
    if text_type == "code":
        return LeafNode("code",text)
    if text_type == "link":
        return LeafNode("a",text,{"href":text_node.url})
    if text_type == "image":
        return LeafNode("img",'',{"src":text_node.url,"alt":text})
    raise ValueError(f"Invalid text type: {text_type}")



            



