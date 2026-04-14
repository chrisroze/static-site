from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
import pprint

# This module defines the main functions for the static site generator, including functions 
# to convert TextNode instances to HTMLNode instances, split TextNode instances based on delimiters, 
# and extract markdown images from text.
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

# This function splits a list of TextNode instances based on a specified TextType delimiter (e.g., bold, italic) 
# and returns a new list of TextNode instances with the appropriate types.
def split_nodes_delimiter(old_nodes_list, text_type):
    list_of_nodes = []
    for old_nodes in old_nodes_list:   
        temp_lst = old_nodes.text.split(text_type.value)        
        for i in range(len(temp_lst)):
            if len(temp_lst[i])!=0: 
                node = TextNode(temp_lst[i],text_type) if i%2==1 else TextNode(temp_lst[i])
                list_of_nodes.append(node)
    return list_of_nodes


# This function splits a list of TextNode instances based on markdown link syntax 
# and returns a new list of TextNode instances with the appropriate types (e.g., link, image, text).
def extract_markdown_images(text):
    lst = []  
    while ("[" in text and "]" in text and "(" in text and ")" in text
                and text.find("[") < text.find("]") < text.find("(") < text.find(")")):
        temp = text.split("[",1)
        link = temp[1].split("]",1)[0]
        temp1 = temp[1].split("]",1)[1].split("(",1)[1].split(")",1)
        url = temp1[0]
        text = temp1[1]
        lst.append((link, url))      
    return lst

# This function splits a list of TextNode instances based on markdown link syntax 
# and returns a new list of TextNode instances with the appropriate types (e.g., link, image, text).
def split_nodes_link(nodes_list):
    lst = []  
    for node in nodes_list:
        text = node.text
        while ("[" in text and "]" in text and "(" in text and ")" in text
                    and text.find("[") < text.find("]") < text.find("(") < text.find(")")):
            temp = text.split("[",1)
            link = temp[1].split("]",1)[0]
            temp1 = temp[1].split("]",1)[1].split("(",1)[1].split(")",1)
            url = temp1[0]
            text = temp1[1]
            if temp[0][-1] == "!":
                lst.append(("t",temp[0][:-1], None)) if temp[0] else None
                lst.append(("p",link, url))
            else:
                lst.append(("t",temp[0], None)) if temp[0] else None
                lst.append(("l",link, url))
        if len(text) != 0:
            lst.append(("t",text, None))
    return tuple_to_textnode(lst)

# This function converts a list of tuples (type, text, url) into a list of TextNode instances 
# based on the specified type (e.g., link, image, text).
# it is called by split_nodes_link to convert the output list of tuples into a list of TextNode instances.
def tuple_to_textnode(tuple_list):
    text_nodes = []
    for type, text, url in tuple_list:
        if type == "l":
            text_nodes.append(TextNode(text, TextType.LINK, url))
        elif type == "p":
            text_nodes.append(TextNode(text, TextType.IMAGE, url))
        else:
            text_nodes.append(TextNode(text, TextType.TEXT))
    return text_nodes   



def main():    

    pass

if __name__ == "__main__":
    main()