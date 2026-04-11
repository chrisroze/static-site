from platform import node
import unittest
from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("div", {"class": "container"}, [])
        node2 = HTMLNode("div", {"class": "container"}, [])
        self.assertEqual(node, node2)

    def test_eq_different_tags(self):
        node = HTMLNode("div", {"class": "container"}, [])
        node2 = HTMLNode("span", {"class": "container"}, [])
        self.assertNotEqual(node, node2)

    def test_eq_different_attributes(self):
        node = HTMLNode("div", {"class": "container"}, [])
        node2 = HTMLNode("div", {"id": "main"}, [])
        self.assertNotEqual(node, node2)

    def test_eq_different_children(self):
        node = HTMLNode("div", {}, [HTMLNode("p", {}, [])])
        node2 = HTMLNode("div", {}, [HTMLNode("span", {}, [])])
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = HTMLNode("div", {"class": "container"}, [HTMLNode("p", {}, [])])
        expected_repr = "HTMLNode(tag='div', value={'class': 'container'}, children=[HTMLNode(tag='p', value={}, children=[], props=None)], props=None)"
        self.assertEqual(repr(node), expected_repr)

if __name__ == "__main__":
    unittest.main()