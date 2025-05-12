import unittest
from markdown_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_simple_blocks(self):
        md = "First block\n\nSecond block"
        expected = ["First block", "Second block"]
        self.assertEqual(markdown_to_blocks(md), expected)

    def test_extra_whitespace(self):
        md = "\n\nFirst block\n\n\nSecond block\n\n   \nThird block"
        expected = ["First block", "Second block", "Third block"]
        self.assertEqual(markdown_to_blocks(md), expected)

    def test_empty_input(self):
        md = ""
        expected = []
        self.assertEqual(markdown_to_blocks(md), expected)

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

if __name__ == "__main__":
    unittest.main()