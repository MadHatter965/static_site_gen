from textnode import TextNode, TextType

def main():
    # sample TextNode
    node = TextNode(
        "TESTING MY CODE",
        TextType.LINK,
        "https://www.website.com"
    )
    
    # Print the node to test the __repr__ method
    print(node)

# Call the main function when the script is run
if __name__ == "__main__":
    main()