from textnode import TextNode, TextType

def text_to_textnodes(text : str) -> list[TextNode]:
# This function converts a string of text into a list of TextNode instances by first splitting the text 
# based on markdown link syntax, then splitting the resulting TextNode instances based on bold, italic, 
# and code delimiters.
    text_node = TextNode(text)
    text_node_list = split_nodes_link([text_node])
    text_node_list = split_nodes_delimiter(text_node_list, TextType.BOLD)
    text_node_list = split_nodes_delimiter(text_node_list, TextType.ITALIC)
    text_node_list = split_nodes_delimiter(text_node_list, TextType.CODE)
    return text_node_list


def split_nodes_delimiter(old_nodes_list : list[TextNode], text_type: TextType) -> list[TextNode]:
# This function splits a list of TextNode instances based on a specified TextType delimiter (e.g., bold, italic) 
# and returns a new list of TextNode instances with the appropriate types.
    list_of_nodes = []
    for old_nodes in old_nodes_list:   
        temp_lst = old_nodes.text.split(text_type.value)        
        for i in range(len(temp_lst)):
            if len(temp_lst[i])!=0: 
                node = TextNode(temp_lst[i],text_type) if i%2==1 else TextNode(temp_lst[i],old_nodes.text_type, old_nodes.url)
                list_of_nodes.append(node)
    return list_of_nodes


def split_nodes_link(nodes_list : list[TextNode]) -> list[TextNode]:
# This function splits a list of TextNode instances based on markdown link syntax 
# and returns a new list of TextNode instances with the appropriate types (e.g., link, image, text).
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


def tuple_to_textnode(tuple_list : list[tuple[str, str, str]]) -> list[TextNode]:
# This function converts a list of tuples (type, text, url) into a list of TextNode instances 
# based on the specified type (e.g., link, image, text).
# it is called by split_nodes_link to convert the output list of tuples into a list of TextNode instances.
    text_nodes = []
    for type, text, url in tuple_list:
        if type == "l":
            text_nodes.append(TextNode(text, TextType.LINK, url))
        elif type == "p":
            text_nodes.append(TextNode(text, TextType.IMAGE, url))
        else:
            text_nodes.append(TextNode(text, TextType.TEXT))
    return text_nodes   


# This function splits a list of TextNode instances based on markdown link syntax 
# and returns a new list of TextNode instances with the appropriate types (e.g., link, image, text).
def extract_markdown_images(text : str) -> list[tuple[str, str]]:
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