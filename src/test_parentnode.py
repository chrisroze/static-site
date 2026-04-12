from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
import unittest


class TestParentNode(unittest.TestCase):

    def test_parentnode_to_html(self):
            node1 = ParentNode(tag='div', children=[
                LeafNode(tag='p', value='Hello, World!')
            ])
            expected_html1 = "<div><p>Hello, World!</p></div>"
            self.assertEqual(node1.to_html(), expected_html1)
    
    def test_nested_parentnode_to_html(self):
            node2 = ParentNode(tag='div', children=[
                ParentNode(tag='p', children=[
                    LeafNode(tag='span', value='Hello, '),
                    LeafNode(tag='span', value='World!')
                ])
            ])
            expected_html2 = "<div><p><span>Hello, </span><span>World!</span></p></div>"
            self.assertEqual(node2.to_html(), expected_html2)


    def test_parentnode_with_props_to_html(self):
            node3 = ParentNode(tag='div', children=[
                ParentNode(tag='a', children=[
                    LeafNode(tag='span', value='Hello, '),
                    LeafNode(tag='span', value='World!')
                ], props={'href': 'https://example.com', 'style': 'color: red; font-weight: bold; text-decoration: none;'})
            ])
            expected_html3 = '<div><a href="https://example.com" style="color: red; font-weight: bold; text-decoration: none;"><span>Hello, </span><span>World!</span></a></div>'
            self.assertEqual(node3.to_html(), expected_html3)


    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )            

if __name__ == '__main__':
    unittest.main()