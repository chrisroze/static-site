from block import block_to_blocktype, markdown_to_blocks
from inline import split_nodes_delimiter, extract_markdown_images, split_nodes_link, tuple_to_textnode, text_to_textnodes
from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
import pprint


# This module defines the main functions for the static site generator, including functions
# to convert TextNode instances to HTMLNode instances, split TextNode instances based on delimiters,
# and extract markdown images from text. 
def main():    

    block01 = "# Heading 1 \n this is a heading 1 block"
    block02 = "## Heading 2 \n this is a heading 2 block"
    block03 = "### Heading 3 \n this is a heading 3 block"
    block04 = "#### Heading 4 \n this is a heading 4 block"
    block05 = "##### Heading 5 \n this is a heading 5 block"
    block06 = "###### Heading 6 \n this is a heading 6 block"
    block07 = "- Unordered list item 1 \n- Unordered list item 2 \n- Unordered list item 3"
    block08 = "> Blockquote line 1 \n> Blockquote line 2 \n> Blockquote line 3"
    block09 = "```\nCode block line 1\nCode block line 2\nCode block line 3\n```"
    block10 = "1. Ordered list item 1 \n2. Ordered list item 2 \n3. Ordered list item 3"
    block11 = "This is a paragraph block with **bold** text, _italic_ text, `code` text, a [link](https://www.example.com), and an ![image](https://www.example.com/image.jpg)."
    
    # positive test cases for block_to_blocktype function
    print(("test01",block01,block_to_blocktype(block01)))
    print(("test02",block02,block_to_blocktype(block02)))
    print(("test03",block03,block_to_blocktype(block03)))
    print(("test04",block04,block_to_blocktype(block04)))
    print(("test05",block05,block_to_blocktype(block05)))
    print(("test06",block06,block_to_blocktype(block06)))
    print(("test07",block07,block_to_blocktype(block07)))
    print(("test08",block08,block_to_blocktype(block08)))
    print(("test09",block09,block_to_blocktype(block09)))
    print(("test10",block10,block_to_blocktype(block10)))
    print(("test11",block11,block_to_blocktype(block11)))
    print("\n")
    # negative test case for block_to_blocktype function
    block12 = "This is a paragraph block without any markdown syntax."
    print(("test12",block12,block_to_blocktype(block12)))
    block013 = "> This is a blockquote block with a newline \n that does not start with a > character."
    print(("test13",block013,block_to_blocktype(block013)))
    block014 = "1. This is an ordered list blockwith a newline \n that does not start with the correct list number."
    print(("test14",block014,block_to_blocktype(block014)))
    block015 = "```\nThis is a code block that does not end with the correct delimiter.\n"
    print(("test15",block015,block_to_blocktype(block015)))
    block016 = "#This is a block that starts with a header markdown delimiter but does not follow the correct syntax.\n# This is not a valid heading block."
    print(("test16",block016,block_to_blocktype(block016)))
    block017 = "- This is an unordered list block with a newline \n that does not start with the correct list item syntax."
    print(("test17",block017,block_to_blocktype(block017)))


def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(value=text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return ParentNode(tag='b', children=[LeafNode(value=text_node.text)])
    elif text_node.text_type == TextType.ITALIC:
        return ParentNode(tag='i', children=[LeafNode(value=text_node.text)])
    elif text_node.text_type == TextType.LINK:
        return ParentNode(tag='a', children=[LeafNode(value=text_node.text)], props={'href': text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode(tag='img', props={'src': text_node.url, 'alt': text_node.text})
    elif text_node.text_type == TextType.CODE:
        return ParentNode(tag='code', children=[LeafNode(value=text_node.text)])
    elif text_node.text_type == TextType.QUOTE:
        return ParentNode(tag='blockquote', children=[LeafNode(value=text_node.text)])
    else:
        raise ValueError(f"Unsupported TextType: {text_node.text_type}")



if __name__ == "__main__":
    main()