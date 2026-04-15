from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING1 = "#"
    HEADING2 = "##"
    HEADING3 = "###"
    HEADING4 = "####"
    HEADING5 = "#####"
    HEADING6 = "######"
    UNORDERED_LIST = "-"
    BLOCKQUOTE = ">"
    BLOCKCODE = "```"
    ORDERED_LIST = "1."


def block_to_blocktype(block : str) -> BlockType:
    if block.startswith(BlockType.HEADING1.value + " "):
        return BlockType.HEADING1
    elif block.startswith(BlockType.HEADING2.value + " "):
        return BlockType.HEADING2
    elif block.startswith(BlockType.HEADING3.value + " "):
        return BlockType.HEADING3
    elif block.startswith(BlockType.HEADING4.value + " "):
        return BlockType.HEADING4
    elif block.startswith(BlockType.HEADING5.value + " "):
        return BlockType.HEADING5
    elif block.startswith(BlockType.HEADING6.value + " "):
        return BlockType.HEADING6
    elif block.startswith(BlockType.UNORDERED_LIST.value + " "):
        list_of_lines = block.split("\n")
        for line in list_of_lines:
            if not line.startswith(BlockType.UNORDERED_LIST.value + " "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    elif block.startswith(BlockType.BLOCKCODE.value + "\n") and block.endswith("\n" + BlockType.BLOCKCODE.value):
        return BlockType.BLOCKCODE
    elif block.startswith(BlockType.BLOCKQUOTE.value):
        list_of_lines = block.split("\n")
        for line in list_of_lines:
            if not line.startswith(BlockType.BLOCKQUOTE.value):
                return BlockType.PARAGRAPH
        return BlockType.BLOCKQUOTE
    elif block.startswith(BlockType.ORDERED_LIST.value + " "):
        list_of_lines = block.split("\n")
        list_number = 1
        for line in list_of_lines:
            if not line.startswith(f"{list_number}. "):
                return BlockType.PARAGRAPH
            list_number += 1
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH


# This function splits a markdown string into blocks based on empty lines and returns a list of non-empty blocks.
def markdown_to_blocks(md : str) -> list[str]:
    list_of_blocks = []
    for block in md.split("\n\n"):
        stripped_block = block.strip()
        if stripped_block:
            list_of_blocks.append(stripped_block)
    return list_of_blocks