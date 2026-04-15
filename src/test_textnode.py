from platform import node
import unittest
from textnode import TextNode, TextType

# This module defines unit tests for the TextNode class, which represents a piece of text with a specific type (e.g., bold, italic, link).
class TestTextNode(unittest.TestCase):

# Tests for TextNode class
# =============================================
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
        expected_repr = "TextNode(TEXT='This is a text node', TEXT_TYPE=TextType.ITALIC)"
        self.assertEqual(repr(node), expected_repr)

    def test_textnode_str(self):
        node = TextNode("Hello World", TextType.TEXT)
        self.assertEqual(str(node), ": Hello World")

    def test_invalid_text_type_raises(self):
        with self.assertRaises(ValueError):
            TextNode("Hello World", "not-a-valid-text-type")

    def test_default_text_type_is_text(self):
        node = TextNode("Hello World")
        self.assertEqual(node.text_type, TextType.TEXT)

    def test_textnode_str_link_with_url(self):
        node = TextNode("Boot.dev", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(str(node), "[link]: Boot.dev (https://www.boot.dev)")

    def test_textnode_str_link_without_url(self):
        node = TextNode("Boot.dev", TextType.LINK)
        self.assertEqual(str(node), "[link]: Boot.dev")


# Tests for text_node_to_html_node function
# =============================================
    def test_text_node_to_html_node_link(self):
        node1 = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
        html_node1 = node1.to_html_node()
        expected_html1 = '<a href="https://www.boot.dev">This is some anchor text</a>'
        self.assertEqual(html_node1.to_html(), expected_html1)

    def test_text_node_to_html_node_plain(self):
        node2 = TextNode("This is some plain text", TextType.TEXT)
        html_node2 = node2.to_html_node()
        expected_html2 = 'This is some plain text'
        self.assertEqual(html_node2.to_html(), expected_html2)

    def test_text_node_to_html_node_bold(self):
        node3 = TextNode("This is bold some text", TextType.BOLD)
        html_node3 = node3.to_html_node()
        expected_html3 = '<b>This is bold some text</b>'
        self.assertEqual(html_node3.to_html(), expected_html3)

    def test_text_node_to_html_node_italic(self):
        node4 = TextNode("This is italic some text", TextType.ITALIC)
        html_node4 = node4.to_html_node()
        expected_html4 = '<i>This is italic some text</i>'
        self.assertEqual(html_node4.to_html(), expected_html4)

    def test_text_node_to_html_node_quote(self):
        node5 = TextNode("This is a quote", TextType.QUOTE)
        html_node5 = node5.to_html_node()
        expected_html5 = '<blockquote>This is a quote</blockquote>'
        self.assertEqual(html_node5.to_html(), expected_html5)

    def test_text_node_to_html_node_code(self):
        node6 = TextNode("This is some code", TextType.CODE)
        html_node6 = node6.to_html_node()
        expected_html6 = '<code>This is some code</code>'
        self.assertEqual(html_node6.to_html(), expected_html6)  

if __name__ == "__main__":
    unittest.main()