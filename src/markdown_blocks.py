from textnode import TextNode, TextType
from enum import Enum

def markdown_to_blocks(markdown):
    working_blocks = markdown.split("\n\n")
    blocks = []
    for block in working_blocks:
        stripped_block = block.strip()
        if stripped_block:
            blocks.append(stripped_block)
    return blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    if block.startswith(("#", "##", "###", "####", "#####", "######")):
        count = 0
        while count < len(block) and block[count] == '#':
            count += 1
        if count < len(block) and block[count] == ' ':
            return BlockType.HEADING
    
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    lines = block.split("\n")
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    
    if all(line.startswith(f"{i+1}. ") for i, line in enumerate(lines)):
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH