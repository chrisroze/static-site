import unittest
from htmlnode import HTMLNode
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leafnode_creation(self):
        node = LeafNode(tag='p', value='Hello, World!', props={'class': 'text'})
        self.assertEqual(node.tag, 'p')
        self.assertEqual(node.value, 'Hello, World!')
        self.assertEqual(node.props, {'class': 'text'})


    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leafnode_equality(self):
        node1 = LeafNode(tag='p', value='Hello, World!', props={'class': 'text'})
        node2 = LeafNode(tag='p', value='Hello, World!', props={'class': 'text'})
        node3 = LeafNode(tag='p', value='Different text', props={'class': 'text'})
        node4 = LeafNode(tag='p', value='Hello, World!', props={'class': 'different'})
        node5 = HTMLNode(tag='b', value='Hello, World!', props={'class': 'text'})
        self.assertEqual(node1, node2)
        self.assertNotEqual(node1, node3)
        self.assertNotEqual(node1, node4)
        self.assertNotEqual(node1, node5)

def test_leafnode_to_html_with_props(self):
    node = LeafNode(tag='a', value='Click here', props={'href': 'https://example.com'})
    expected_html = '<a href="https://example.com">Click here</a>'
    self.assertEqual(node.to_html(), expected_html)


if __name__ == '__main__':
    unittest.main()