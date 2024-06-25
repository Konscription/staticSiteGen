#THE TEXTNODE CLASS
#In textnode.py create a class called TextNode. It should have 3 properties that can be set in the constructor:
#
#self.text - The text content of the node
#self.text_type - The type of text this node contains, which is just a string like "bold" or "italic"
#self.url - The URL of the link or image, if the text is a link. Default to None if nothing is passed in.
#
#Next, create an __eq__ method that returns True if all of the properties of two TextNode objects are equal.
#
#Finally, create a __repr__ method that returns a string representation of the TextNode object. It should look like this:
#
#TextNode(TEXT, TEXT_TYPE, URL)
#Where TEXT, TEXT_TYPE, and URL are the values of the text, text_type, and url properties, respectively.


class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text 
        self.text_type = text_type 
        self.url = url

    def __eq__(self, other) -> bool:
        return (
            self.text == other.text 
            and self.text_type == other.text_type 
            and self.url == other.url
        )
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
