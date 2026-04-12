from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
import pprint


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


def split_nodes_delimiter(old_nodes, text_type):
    list_of_nodes = []
    temp_lst = old_nodes.split(text_type.value)
    for i in range(len(temp_lst)):
        if len(temp_lst[i])!=0: 
            node = TextNode(temp_lst[i],text_type) if i%2==1 else TextNode(temp_lst[i])
            list_of_nodes.append(node)
    return list_of_nodes
    






def main():
    
    pass



if __name__ == "__main__":
    main()