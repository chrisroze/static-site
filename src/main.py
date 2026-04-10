from textnode import TextNode, TextType


def main():
    node01 = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node01)
    print(repr(node01))





if __name__ == "__main__":
    main()