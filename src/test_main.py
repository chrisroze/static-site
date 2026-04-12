import unittest 
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextNode, TextType
from main import split_nodes_delimiter, text_node_to_html_node


class TestMain(unittest.TestCase):

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



# Tests for split_nodes_delimiter function
# =============================================

    def test_split_nodes_delimiter_bold(self):
         exemple1 = "This is text with a **bolded phrase** in the middle"
         result1 = split_nodes_delimiter(exemple1,TextType.BOLD)
         expected_result1 = [TextNode("This is text with a ", TextType.TEXT), TextNode("bolded phrase", TextType.BOLD), TextNode(" in the middle", TextType.TEXT)]
         self.assertEqual(result1, expected_result1)

    def test_split_nodes_delimiter_bold_start_end(self):
        exemple2 = "**This is text** with bolded phrase at the start **and at the end**"
        result2 = split_nodes_delimiter(exemple2,TextType.BOLD)
        expected_result2 = [TextNode("This is text", TextType.BOLD), TextNode(" with bolded phrase at the start ", TextType.TEXT), TextNode("and at the end", TextType.BOLD)]
        self.assertEqual(result2, expected_result2)

    def test_split_nodes_delimiter_italic(self):
        exemple3 = "This is text with a _italicized phrase_ in the middle"
        result3 = split_nodes_delimiter(exemple3,TextType.ITALIC)
        expected_result3 = [TextNode("This is text with a ", TextType.TEXT), TextNode("italicized phrase", TextType.ITALIC), TextNode(" in the middle", TextType.TEXT)]
        self.assertEqual(result3, expected_result3)

    def test_split_nodes_delimiter_italic_start_end(self):
        exemple4 = "_This is an italicized phrase_ with bolded phrase at the start _and at the end_"
        result4 = split_nodes_delimiter(exemple4,TextType.ITALIC)
        expected_result4 = [TextNode("This is an italicized phrase", TextType.ITALIC), TextNode(" with bolded phrase at the start ", TextType.TEXT), TextNode("and at the end", TextType.ITALIC)]
        self.assertEqual(result4, expected_result4)

    def test_split_nodes_delimiter_code(self):
        exemple5 = "This is text with a 'code phrase' in the middle"
        result5 = split_nodes_delimiter(exemple5,TextType.CODE)
        expected_result5 = [TextNode("This is text with a ", TextType.TEXT), TextNode("code phrase", TextType.CODE), TextNode(" in the middle", TextType.TEXT)]
        self.assertEqual(result5, expected_result5)

    def test_split_nodes_delimiter_code_start_end(self):
        exemple6 = "'This is a code phrase' with bolded phrase at the start 'and at the end'"
        result6 = split_nodes_delimiter(exemple6,TextType.CODE)
        expected_result6 = [TextNode("This is a code phrase", TextType.CODE), TextNode(" with bolded phrase at the start ", TextType.TEXT), TextNode("and at the end", TextType.CODE)]
        self.assertEqual(result6, expected_result6)



if __name__ == "__main__":  
    unittest.main()