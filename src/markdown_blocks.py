from textnode import TextNode, TextType
import re

def markdown_to_blocks(markdown):
    working_blocks = markdown.split("\n\n")
    blocks = []
    for block in working_blocks:
        if block.strip():
            blocks.append(block.strip())
    return blocks
