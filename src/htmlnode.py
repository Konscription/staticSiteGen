from typing import (Type,Dict,List)


class HTMLNode:
    """represent a "node" in an HTML document tree 
    (like a <p> tag and its contents, or an <a> tag and its contents)
    and is purpose-built to render itself as HTML.
    """
    def __init__(self, tag: str = None, value: str = None, children: List['HTMLNode'] = None, props: Dict[str,str] = None) -> None:
        """4 optional data members
            counterintuitively, every data member should be optional and default to None:
            An HTMLNode without a tag will just render as raw text
            An HTMLNode without a value will be assumed to have children
            An HTMLNode without children will be assumed to have a value
            An HTMLNode without props simply won't have any attributes

        Args:
            tag (str, optional): A string representing the HTML tag name.(e.g. "p", "a", "h1", etc.) Defaults to None.
            value (str, optional): A string representing the value of the HTML tag.(e.g. the text inside a paragraph) Defaults to None.
            children (List[HTMLNode], optional): A list of HTMLNode objects representing the children of this node. Defaults to None.
            props (Dict[str,str], optional): a dictionary of key-value pairs representing the attributes of the HTML tag. 
                For example, a link (<a> tag) might have {"href": "https://www.google.com"}
                Defaults to None.
        """        
        self.tag = tag  #A string representing the HTML tag name
        self.value = value #A string representing the value of the HTML tag
        self.children = children #A list of HTMLNode objects representing the children of this node
        self.props = props #A dictionary of key-value pairs representing the attributes of the HTML tag

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self) -> str:
        """return a string that represents the HTML attributes of the node.

        Returns:
            str: string representation of the HTML attributes of the node
        """        
        if self.props is None or self.props is {}:
            return ''
        prop = ''
        for key, value in self.props.items():
            prop += f' {key}="{value}"'
        return prop
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag},{self.value}, children: {self.children},{self.props})"
    
    def __eq__(self, other: Type['HTMLNode']) -> bool:
        """compare two HTML nodes, and evaluate if they are equal.
        
        Args:
            other (HTMLNode): other HTMLNode object to compare

        Returns:
            bool: true if objects values are the same, false otherwise
        """        
        if not isinstance(other, HTMLNode):
            return False                
        return (
            self.tag == other.tag 
            and self.value == other.value
            and self.children_eq(self.children, other.children)
            and self.props == other.props
        )
        
    def children_eq(self, children: List['HTMLNode'], other_children: List['HTMLNode']) -> bool:
        if children != [] and children != None and other_children != [] and other_children != None:
            for child in children:
                for other_child in other_children:
                    if child.tag != other_child.tag:
                        return False
                    if child.value != other_child.value:
                        return False
                    if not self.children_eq(child.children, other_child.children):
                        return False
        return True

class LeafNode(HTMLNode):
    """a type of HTMLNode that represents a single HTML tag with no children. 
    For example, a simple <p> tag with some text inside of it
    """
    def __init__(self, tag: str, value:str, props: Dict[str,str] = None):
        """inherits from HTMLNode.
        dissallows children.
        value is required.

        Args:
            tag (str): A string representing the HTML tag name.(e.g. "p", "a", "h1", etc.)
            value (str): A string representing the value of the HTML tag.(e.g. the text inside a paragraph)
            props (Dict[str,str], optional): a dictionary of key-value pairs representing the attributes of the HTML tag. 
                For example, a link (<a> tag) might have {"href": "https://www.google.com"}
                Defaults to None.
        """        
        super().__init__(tag, value, None, props)
    
    def to_html(self) -> str:
        """renders a leaf node as an HTML string

        Raises:
            ValueError: raised error when a leaf node has no value

        Returns:
            str: a string of html using the data of the node
        """        
        if self.value is None:
            raise ValueError("All leaf nodes require a value.")
        if self.tag is None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    """model to handle the nesting of HTML nodes inside of one another. 
    Any HTML node that's not "leaf" node (i.e. it has children) is a "parent" node.
    """
    def __init__(self, tag: str, children: List[HTMLNode], props: Dict[str,str] = None):
        """It doesn't take a value argument
            The children argument is not optional

        Args:
            tag (str): A string representing the HTML tag name.(e.g. "p", "a", "h1", etc.)
            children (List[HTMLNode]): A list of HTMLNode objects representing the children of this node.
            props (Dict[str,str], optional): a dictionary of key-value pairs representing the attributes of the HTML tag. 
                For example, a link (<a> tag) might have {"href": "https://www.google.com"}
                Defaults to None.
        """        
        super().__init__(tag,None,children,props)

    def to_html(self) -> str:
        """ensure all data is present else throw an error.
        return a string representing the HTML tag of the node and its children.

        Raises:
            ValueError: raise an error if there is no value for a Tag in this node
            ValueError: raise an error if there are no children in this node

        Returns:
            str: returns a string representing the HTML tag of the node and its children.
        """        
        if self.tag is None:
            raise ValueError("Tag value required")
        if self.children is None:
            raise ValueError("Parent node requires children")
        if self.children == []:
            return f"<{self.tag}{self.props_to_html()}></{self.tag}>"
        html= f"<{self.tag}{self.props_to_html()}>"
        if self.tag == '':
            html = ''
        for child in self.children:
            html += child.to_html()
        if self.tag == '':
            return html
        html += f"</{self.tag}>"
        return html
    
    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"


