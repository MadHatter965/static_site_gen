import unittest
from markdown_blocks import markdown_to_blocks, BlockType, block_to_block_type
from enum import Enum

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

class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph(self):
        text = "This is a simple paragraph."
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)
        
        text = "This is a paragraph\nwith multiple lines."
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)

    def test_heading(self):
        text = "# This is a heading"
        self.assertEqual(block_to_block_type(text), BlockType.HEADING)
        
        text = "## This is a level 2 heading"
        self.assertEqual(block_to_block_type(text), BlockType.HEADING)
        
        text = "###### This is a level 6 heading"
        self.assertEqual(block_to_block_type(text), BlockType.HEADING)
        
        # Not a heading (no space after #)
        text = "#This is not a heading"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)

    def test_code(self):
        text = "```\ncode block\n```"
        self.assertEqual(block_to_block_type(text), BlockType.CODE)
        
        text = "```python\ndef hello():\n    print('Hello')\n```"
        self.assertEqual(block_to_block_type(text), BlockType.CODE)
        
        # Not a code block (only starts with ```)
        text = "```\ncode block without end"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)

    def test_code(self):
        text = "```\ncode block\n```"
        self.assertEqual(block_to_block_type(text), BlockType.CODE)
        
        text = "```python\ndef hello():\n    print('Hello')\n```"
        self.assertEqual(block_to_block_type(text), BlockType.CODE)
        
        # Not a code block (only starts with ```)
        text = "```\ncode block without end"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)

    def test_unordered_list(self):
        text = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(block_to_block_type(text), BlockType.UNORDERED_LIST)
        
        # Not an unordered list (missing space after -)
        text = "-Item 1\n-Item 2\n-Item 3"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)
        
        # Not an unordered list (inconsistent formatting)
        text = "- Item 1\nItem 2\n- Item 3"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)

    def test_ordered_list(self):
        # Valid ordered list
        text = "1. First item\n2. Second item\n3. Third item"
        self.assertEqual(block_to_block_type(text), BlockType.ORDERED_LIST)
        
        # Not an ordered list (doesn't start with 1)
        text = "2. First item\n3. Second item\n4. Third item"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)
        
        # Not an ordered list (non-sequential)
        text = "1. First item\n3. Third item\n4. Fourth item"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)
        
        # Not an ordered list (wrong format)
        text = "1) First item\n2) Second item\n3) Third item"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)
        
        # Not an ordered list (missing space after period)
        text = "1.First item\n2.Second item\n3.Third item"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)
        
        # Single item ordered list
        text = "1. Only item"
        self.assertEqual(block_to_block_type(text), BlockType.ORDERED_LIST)

    def test_paragraph(self):
        # Simple paragraph
        text = "This is a simple paragraph."
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)
        
        # Multi-line paragraph
        text = "This is a paragraph\nwith multiple lines."
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)
        
        # Paragraph with special characters
        text = "Paragraph with *italic*, **bold**, and `code`."
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)
        
        # Empty string (should default to paragraph)
        text = ""
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)
        
        # Paragraph that might look similar to other blocks but doesn't meet criteria
        text = "#Not a heading because no space"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)
        
        text = "```Only one code marker"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)
        
        text = "- Not an unordered list\nBecause second line doesn't start with -"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()