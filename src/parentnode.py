from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        self.tag = tag
        self.children = children
        self.props = props

    def __repr__(self):
        return f"ParentNode(tag='{self.tag}', children={self.children}, props={self.props})"
    
    def __eq__(self, other):
        if not isinstance(other, ParentNode):
            return False
        return (self.tag == other.tag and
                self.children == other.children and
                self.props == other.props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag to convert to HTML")
        if self.children is None:
            raise ValueError("ParentNode must have children to convert to HTML")
        attrs = self.props_to_html()
        opening_tag = f"<{self.tag}{attrs}>"
        closing_tag = f"</{self.tag}>"
        children_html = ''.join(child.to_html() for child in self.children)
        return f"{opening_tag}{children_html}{closing_tag}"
    
