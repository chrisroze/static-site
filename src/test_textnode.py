from platform import node
import unittest
from textnode import TextNode, TextType

# This module defines unit tests for the TextNode class, which represents a piece of text with a specific type (e.g., bold, italic, link).
class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq2(self):
        node = TextNode("This is a text node", TextType.IMAGE, "https://www.example.com/image.png")
        node2 = TextNode("This is a text node", TextType.IMAGE, "https://www.example.com/image.png")
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode("This is a text node", TextType.LINK, "https://www.example.com/image.png")
        node2 = TextNode("This is a text node", TextType.IMAGE, "https://www.example.com/image.png")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        expected_repr = "TextNode(TEXT='This is a text node', TEXT_TYPE=TextType.ITALIC, URL='None')"
        self.assertEqual(repr(node), expected_repr)

    def test_textnode_str(self):
        node = TextNode("Hello World", TextType.TEXT)
        self.assertEqual(str(node), "text: Hello World")

    def test_invalid_text_type_raises(self):
        with self.assertRaises(ValueError):
            TextNode("Hello World", "not-a-valid-text-type")

    def test_default_text_type_is_text(self):
        node = TextNode("Hello World")
        self.assertEqual(node.text_type, TextType.TEXT)

    def test_textnode_str_link_with_url(self):
        node = TextNode("Boot.dev", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(str(node), "link: Boot.dev (https://www.boot.dev)")

    def test_textnode_str_link_without_url(self):
        node = TextNode("Boot.dev", TextType.LINK)
        self.assertEqual(str(node), "link: Boot.dev")




if __name__ == "__main__":
    unittest.main()