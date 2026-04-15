from enum import Enum
from leafnode import LeafNode
from parentnode import ParentNode

# This module defines the TextNode class, which represents a piece of text with a specific type (e.g., bold, italic, link).
class TextType(Enum):
    TEXT = ""
    BOLD = "**"
    ITALIC = "_"
    CODE = "`"
    LINK = "[link]"
    IMAGE = "!"
    QUOTE = ">"


# The TextNode class represents a piece of text with a specific type (e.g., bold, italic, link).
# It has attributes for the text content, the type of text, and an optional URL for links and images.
class TextNode:
    def __init__(self, text: str, text_type: TextType = TextType.TEXT, url: str = None):
        if not isinstance(text_type, TextType):
            raise ValueError("text_type must be an instance of TextType")
        self.text = text
        self.text_type = text_type
        self.url = url  # For links and images

    def __str__(self):
        if self.text_type in {TextType.LINK, TextType.IMAGE} and self.url is not None:
            return f"{self.text_type.value}: {self.text} ({self.url})"
        return f"{self.text_type.value}: {self.text}"
    
    def __repr__(self):
        if self.text_type in {TextType.LINK, TextType.IMAGE} and self.url is not None:
            return f"TextNode(TEXT='{self.text}', TEXT_TYPE={self.text_type}, URL='{self.url}')"
        return f"TextNode(TEXT='{self.text}', TEXT_TYPE={self.text_type})"
    
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return NotImplemented
        return (self.text == other.text and 
                self.text_type == other.text_type and 
                self.url == other.url)

# This module defines the main functions for the static site generator, including functions 
# to convert TextNode instances to HTMLNode instances, split TextNode instances based on delimiters, 
# and extract markdown images from text.
    def to_html_node(self):
        if self.text_type == TextType.TEXT:
            return LeafNode(value=self.text)
        elif self.text_type == TextType.BOLD:
            return ParentNode(tag='b', children=[LeafNode(value=self.text)])
        elif self.text_type == TextType.ITALIC:
            return ParentNode(tag='i', children=[LeafNode(value=self.text)])
        elif self.text_type == TextType.LINK:
            return ParentNode(tag='a', children=[LeafNode(value=self.text)], props={'href': self.url})
        elif self.text_type == TextType.IMAGE:
            return LeafNode(tag='img', props={'src': self.url, 'alt': self.text})
        elif self.text_type == TextType.CODE:
            return ParentNode(tag='code', children=[LeafNode(value=self.text)])
        elif self.text_type == TextType.QUOTE:
            return ParentNode(tag='blockquote', children=[LeafNode(value=self.text)])
        else:
            raise ValueError(f"Unsupported TextType: {self.text_type}")    