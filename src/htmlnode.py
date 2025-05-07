from textnode import TextType, TextNode

class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self. props = props
    
    def to_html(slef):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
    
        props_str = " " + " ".join([f'{key}="{value}"' for key, value in self.props.items()])
        
        return props_str
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
        
class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return f"{self.value}"
        if self.props:
            attrs = [f'{key}="{value}"' for key, value in self.props.items()]
            attr_str = " ".join(attrs)
            return f"<{self.tag} {attr_str}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("Tag is required")
        if self.children == None:
            raise ValueError("Child is required")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        if self.props:
            attrs = [f'{key}="{value}"' for key, value in self.props.items()]
            attr_str = " ".join(attrs)
            return f"<{self.tag} {attr_str}>{children_html}</{self.tag}>"
        else:
            return f"<{self.tag}>{children_html}</{self.tag}>"

def text_node_to_html_node(text_node):
    if text_node.text_type not in (TextType.TEXT, TextType.BOLD, TextType.ITALIC, TextType.CODE, TextType.LINK, TextType.IMAGE):
        raise Exception("Unrecognized text type")
    if text_node.text_type == TextType.TEXT:
        return LeafNode(tag=None, value=text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode(tag = "b", value=text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode(tag = "i", value=text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode(tag="code", value=text_node.text)
    if text_node.text_type == TextType.LINK:
        if text_node.url == None:
            raise ValueError("URL required")
        if text_node.text == None:
            raise ValueError("anchor text required")
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        if text_node.url == None:
            raise ValueError("URL required")
        if text_node.text == None:
            raise ValueError("alt text required")
        return LeafNode(tag= "img", value= "", props={"src": text_node.url , "alt" :text_node.text})
