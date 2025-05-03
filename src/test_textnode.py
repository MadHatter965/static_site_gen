import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_different_text(self):
        node = TextNode("THIS IS A TEXT NODE", TextType.ITALIC)
        node2 = TextNode("THIS IS A DIFFERENT TEXT NODE", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    def test_different_type(self):
        node = TextNode("This is one type of text node", TextType.BOLD)
        node2 = TextNode("This is one type of text node", TextType.TEXT)
        self.assertNotEqual(node,node2)
    def test_different_url(self):
        node1 = TextNode("Link text", TextType.LINK, "https://example.com")
        node2 = TextNode("Link text", TextType.LINK, "https://different-url.com")
        self.assertNotEqual(node1, node2)
    def test_one_with_url(self):
        node1 = TextNode("Text", TextType.LINK, "https://example.com")
        node2 = TextNode("Text", TextType.LINK, None)  # Using explicit None
        self.assertNotEqual(node1, node2)
    def test_same_url(self):
        node1 = TextNode("Link text", TextType.LINK, "https://example.com")
        node2 = TextNode("Link text", TextType.LINK, "https://example.com")
        self.assertEqual(node1, node2)
    def test_default_url(self):
        # This tests that the default url value is None
        node = TextNode("Text", TextType.TEXT)  # No url specified
        self.assertEqual(node.url, None)

if __name__ == "__main__":
    unittest.main()