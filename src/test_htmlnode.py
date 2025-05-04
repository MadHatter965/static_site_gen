
import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_multiple_props(self):
        node = HTMLNode(None, None, None, {"href": "https://google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://google.com" target="_blank"')
    
    def test_props_to_html_with_single_prop(self):
        node = HTMLNode(None, None, None, {"class": "test-class"})
        self.assertEqual(node.props_to_html(), ' class="test-class"')
    
    def test_props_to_html_with_no_props(self):
        node = HTMLNode(None, None, None, {})
        self.assertEqual(node.props_to_html(), '')
        
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_fail(self):
        node = LeafNode("p")
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leafnode_with_tag_value_and_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://example.com"})
        self.assertEqual(node.to_html(), '<a href="https://example.com">Click me!</a>')

    def test_leafnode_with_value_only(self):
        node = LeafNode(None, "Plain text only.")
        self.assertEqual(node.to_html(), "Plain text only.")

    def test_leafnode_empty_props(self):
        node = LeafNode("p", "Some text.", {})
        self.assertEqual(node.to_html(), "<p>Some text.</p>")


if __name__ == "__main__":
    unittest.main()