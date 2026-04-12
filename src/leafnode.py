from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def __repr__(self):
        return f"LeafNode(tag='{self.tag}', value='{self.value}', props='{self.props}')"
    
    def __eq__(self, other):
        if not isinstance(other, LeafNode):
            return False
        return (self.tag == other.tag and
                self.value == other.value and
                self.props == other.props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value to convert to HTML")
        if self.tag is None:
            return self.value
        attrs = self.props_to_html()
        opening_tag = f"<{self.tag}{attrs}>"
        closing_tag = f"</{self.tag}>"
        return f"{opening_tag}{self.value}{closing_tag}"        
