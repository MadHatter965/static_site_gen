from textnode import TextNode, TextType
import re

def markdown_to_blocks(markdown):
    working_blocks = markdown.split("\n\n")
    blocks = []
    for block in working_blocks:
        stripped_block = block.strip()
        if stripped_block:
            blocks.append(stripped_block)
    return blocks
