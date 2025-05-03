
import unittest
from htmlnode import HTMLNode

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
        

if __name__ == "__main__":
    unittest.main()