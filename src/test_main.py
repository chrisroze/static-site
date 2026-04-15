import unittest 
from main import text_node_to_html_node
from textnode import TextNode, TextType



class TestMain(unittest.TestCase):
    pass

# Tests for text_node_to_html_node function
# =============================================
    def test_text_node_to_html_node_link(self):
        node1 = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
        html_node1 = text_node_to_html_node(node1)
        expected_html1 = '<a href="https://www.boot.dev">This is some anchor text</a>'
        self.assertEqual(html_node1.to_html(), expected_html1)

    def test_text_node_to_html_node_plain(self):
        node2 = TextNode("This is some plain text", TextType.TEXT)
        html_node2 = text_node_to_html_node(node2)
        expected_html2 = 'This is some plain text'
        self.assertEqual(html_node2.to_html(), expected_html2)

    def test_text_node_to_html_node_bold(self):
        node3 = TextNode("This is bold some text", TextType.BOLD)
        html_node3 = text_node_to_html_node(node3)
        expected_html3 = '<b>This is bold some text</b>'
        self.assertEqual(html_node3.to_html(), expected_html3)

    def test_text_node_to_html_node_italic(self):
        node4 = TextNode("This is italic some text", TextType.ITALIC)
        html_node4 = text_node_to_html_node(node4)
        expected_html4 = '<i>This is italic some text</i>'
        self.assertEqual(html_node4.to_html(), expected_html4)

    def test_text_node_to_html_node_quote(self):
        node5 = TextNode("This is a quote", TextType.QUOTE)
        html_node5 = text_node_to_html_node(node5)
        expected_html5 = '<blockquote>This is a quote</blockquote>'
        self.assertEqual(html_node5.to_html(), expected_html5)

    def test_text_node_to_html_node_code(self):
        node6 = TextNode("This is some code", TextType.CODE)
        html_node6 = text_node_to_html_node(node6)
        expected_html6 = '<code>This is some code</code>'
        self.assertEqual(html_node6.to_html(), expected_html6)  



if __name__ == "__main__":  
    unittest.main()