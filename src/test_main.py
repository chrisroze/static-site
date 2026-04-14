import unittest 
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextNode, TextType
from main import extract_markdown_images, split_nodes_delimiter, split_nodes_link, text_node_to_html_node, text_to_textnodes


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
         exemple1 = [TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)]
         result1 = split_nodes_delimiter(exemple1,TextType.BOLD)
         expected_result1 = [TextNode("This is text with a ", TextType.TEXT), TextNode("bolded phrase", TextType.BOLD), TextNode(" in the middle", TextType.TEXT)]
         self.assertEqual(result1, expected_result1)

    def test_split_nodes_delimiter_bold_start_end(self):
        exemple2 = [TextNode("**This is text** with bolded phrase at the start **and at the end**", TextType.TEXT)]
        result2 = split_nodes_delimiter(exemple2,TextType.BOLD)
        expected_result2 = [TextNode("This is text", TextType.BOLD), TextNode(" with bolded phrase at the start ", TextType.TEXT), TextNode("and at the end", TextType.BOLD)]
        self.assertEqual(result2, expected_result2)

    def test_split_nodes_delimiter_italic(self):
        exemple3 = [TextNode("This is text with a _italicized phrase_ in the middle", TextType.TEXT)]
        result3 = split_nodes_delimiter(exemple3,TextType.ITALIC)
        expected_result3 = [TextNode("This is text with a ", TextType.TEXT), TextNode("italicized phrase", TextType.ITALIC), TextNode(" in the middle", TextType.TEXT)]
        self.assertEqual(result3, expected_result3)

    def test_split_nodes_delimiter_italic_start_end(self):
        exemple4 = [TextNode("_This is an italicized phrase_ with bolded phrase at the start _and at the end_", TextType.TEXT)]
        result4 = split_nodes_delimiter(exemple4,TextType.ITALIC)
        expected_result4 = [TextNode("This is an italicized phrase", TextType.ITALIC), TextNode(" with bolded phrase at the start ", TextType.TEXT), TextNode("and at the end", TextType.ITALIC)]
        self.assertEqual(result4, expected_result4)

    def test_split_nodes_delimiter_code(self):
        exemple5 = [TextNode("This is text with a `code phrase` in the middle", TextType.TEXT)]
        result5 = split_nodes_delimiter(exemple5,TextType.CODE)
        expected_result5 = [TextNode("This is text with a ", TextType.TEXT), TextNode("code phrase", TextType.CODE), TextNode(" in the middle", TextType.TEXT)]
        self.assertEqual(result5, expected_result5)

    def test_split_nodes_delimiter_code_start_end(self):
        exemple6 = [TextNode("`This is a code phrase` with bolded phrase at the start `and at the end`", TextType.TEXT)]
        result6 = split_nodes_delimiter(exemple6,TextType.CODE)
        expected_result6 = [TextNode("This is a code phrase", TextType.CODE), TextNode(" with bolded phrase at the start ", TextType.TEXT), TextNode("and at the end", TextType.CODE)]
        self.assertEqual(result6, expected_result6)

    def test_split_nodes_delimiter_quote(self):
        exemple7 = [TextNode("This is text with a >quote phrase> in the middle", TextType.TEXT)]
        result7 = split_nodes_delimiter(exemple7,TextType.QUOTE)
        expected_result7 = [TextNode("This is text with a ", TextType.TEXT), TextNode("quote phrase", TextType.QUOTE), TextNode(" in the middle", TextType.TEXT)]
        self.assertEqual(result7, expected_result7)

# Tests for extract_markdown_images function
# =============================================
    def test_extract_markdown_images(self):
       text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
       result = extract_markdown_images(text)
       self.assertEqual(result, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_extract_markdown_images_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])
    
    def test_extract_markdown_images_mixed(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and a link [to boot dev](https://www.boot.dev)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("to boot dev", "https://www.boot.dev")])

# Tests for split_nodes_link function
# =============================================
    def test_split_nodes_link(self):
        nodes = [TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",TextType.TEXT,),
            TextNode("This is text with an image ![alt text](https://www.example.com/image.jpg) inside a text",TextType.TEXT),
            TextNode("This is text with a [ quote and ] but not a link",TextType.TEXT),
            TextNode("This is (https://www.boot.dev) not a link",TextType.TEXT), 
            TextNode("Link before (https://www.boot.dev) [alt text] after",TextType.TEXT)]
        result = split_nodes_link(nodes)
        expected_result = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            TextNode("This is text with an image ", TextType.TEXT),
            TextNode("alt text", TextType.IMAGE, "https://www.example.com/image.jpg"),
            TextNode(" inside a text", TextType.TEXT),
            TextNode("This is text with a [ quote and ] but not a link",TextType.TEXT),
            TextNode("This is (https://www.boot.dev) not a link",TextType.TEXT), 
            TextNode("Link before (https://www.boot.dev) [alt text] after",TextType.TEXT),
        ]
        self.assertEqual(result, expected_result)

    def test_split_nodes_link_no_links(self):
        nodes = [TextNode("This is text with no links or images", TextType.TEXT)]
        result = split_nodes_link(nodes)
        expected_result = [TextNode("This is text with no links or images", TextType.TEXT)]
        self.assertEqual(result, expected_result)

# Tests for text_to_textnodes function
# =============================================
    def test_text_to_textnodes(self):
        text = "This is a **bold** text with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev) to boot.dev."
        result = text_to_textnodes(text)
        expected_result = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            TextNode(" to boot.dev.", TextType.TEXT)
        ]
        self.assertEqual(result, expected_result)


if __name__ == "__main__":  
    unittest.main()