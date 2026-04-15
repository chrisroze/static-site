import unittest 
from block import block_to_blocktype, markdown_to_blocks

class TestBlockFunctions(unittest.TestCase):
# Tests for markdown_to_blocks function
# =============================================
    def test_markdown_to_blocks(self):
        md = """
        This is **bolded** paragraph



This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line


- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_empty_lines(self):
        md = """



This is a paragraph with empty lines before and after


"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is a paragraph with empty lines before and after"])

    def test_markdown_to_blocks_only_empty_lines(self):
        md = """


        
        
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])    
        
if __name__ == "__main__":
    unittest.main()