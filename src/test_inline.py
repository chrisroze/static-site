import unittest 
from textnode import TextNode, TextType
from inline import extract_markdown_images, split_nodes_delimiter, split_nodes_link


class TestInline(unittest.TestCase):


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

  


if __name__ == "__main__":  
    unittest.main()