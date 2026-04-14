from enum import Enum

# This module defines the TextNode class, which represents a piece of text with a specific type (e.g., bold, italic, link).
class TextType(Enum):
    TEXT = ""
    BOLD = "**"
    ITALIC = "_"
    CODE = "'"
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