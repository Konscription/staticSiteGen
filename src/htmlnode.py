#Perhaps counterintuitively, every data member should be optional and default to None:
#
#An HTMLNode without a tag will just render as raw text
#An HTMLNode without a value will be assumed to have children
#An HTMLNode without children will be assumed to have a value
#An HTMLNode without props simply won't have any attributes



class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None) -> None:
        self.tag = tag  #A string representing the HTML tag name
        self.value = value #A string representing the value of the HTML tag
        self.children = children #A list of HTMLNode objects representing the children of this node
        self.props = props #A dictionary of key-value pairs representing the attributes of the HTML tag

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None or self.props is {}:
            return ''
        prop = ''
        for key, value in self.props.items():
            prop += f' {key}="{value}"'
        return prop
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag},{self.value}, children: {self.children},{self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("All leaf nodes require a value.")
        if self.tag is None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag,None,children,props)

    def to_html(self):
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
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"


    