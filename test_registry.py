"""
Unit tests for the Registry class.
"""

import unittest
from registry import Registry


class TestRegistry(unittest.TestCase):
    """Test cases for the Registry class."""
    
    def setUp(self):
        """Set up a fresh registry for each test."""
        self.registry = Registry()
    
    def test_init_empty(self):
        """Test that a new registry is empty."""
        self.assertEqual(len(self.registry), 0)
        self.assertEqual(self.registry.list_keys(), [])
    
    def test_add_single_item(self):
        """Test adding a single item to the registry."""
        result = self.registry.add("key1", "value1")
        self.assertEqual(result, "value1")
        self.assertEqual(self.registry.get("key1"), "value1")
        self.assertEqual(len(self.registry), 1)
    
    def test_add_multiple_items(self):
        """Test adding multiple items to the registry."""
        self.registry.add("key1", "value1")
        self.registry.add("key2", "value2")
        self.registry.add("key3", "value3")
        
        self.assertEqual(len(self.registry), 3)
        self.assertEqual(self.registry.get("key1"), "value1")
        self.assertEqual(self.registry.get("key2"), "value2")
        self.assertEqual(self.registry.get("key3"), "value3")
    
    def test_add_updates_existing(self):
        """Test that adding with an existing key updates the value."""
        self.registry.add("key1", "value1")
        self.registry.add("key1", "value2")
        
        self.assertEqual(self.registry.get("key1"), "value2")
        self.assertEqual(len(self.registry), 1)
    
    def test_get_nonexistent_key(self):
        """Test getting a value for a key that doesn't exist."""
        self.assertIsNone(self.registry.get("nonexistent"))
    
    def test_get_with_default(self):
        """Test getting a value with a custom default."""
        result = self.registry.get("nonexistent", "default_value")
        self.assertEqual(result, "default_value")
    
    def test_remove_existing_key(self):
        """Test removing an existing key."""
        self.registry.add("key1", "value1")
        result = self.registry.remove("key1")
        
        self.assertEqual(result, "value1")
        self.assertIsNone(self.registry.get("key1"))
        self.assertEqual(len(self.registry), 0)
    
    def test_remove_nonexistent_key(self):
        """Test removing a key that doesn't exist."""
        result = self.registry.remove("nonexistent")
        self.assertIsNone(result)
    
    def test_list_keys(self):
        """Test listing all keys."""
        self.registry.add("key1", "value1")
        self.registry.add("key2", "value2")
        self.registry.add("key3", "value3")
        
        keys = self.registry.list_keys()
        self.assertEqual(len(keys), 3)
        self.assertIn("key1", keys)
        self.assertIn("key2", keys)
        self.assertIn("key3", keys)
    
    def test_list_items(self):
        """Test listing all key-value pairs."""
        self.registry.add("key1", "value1")
        self.registry.add("key2", "value2")
        
        items = self.registry.list_items()
        self.assertEqual(len(items), 2)
        self.assertIn(("key1", "value1"), items)
        self.assertIn(("key2", "value2"), items)
    
    def test_clear(self):
        """Test clearing the registry."""
        self.registry.add("key1", "value1")
        self.registry.add("key2", "value2")
        
        self.assertEqual(len(self.registry), 2)
        
        self.registry.clear()
        
        self.assertEqual(len(self.registry), 0)
        self.assertEqual(self.registry.list_keys(), [])
    
    def test_contains(self):
        """Test the 'in' operator for checking key existence."""
        self.registry.add("key1", "value1")
        
        self.assertIn("key1", self.registry)
        self.assertNotIn("nonexistent", self.registry)
    
    def test_len(self):
        """Test the len() function."""
        self.assertEqual(len(self.registry), 0)
        
        self.registry.add("key1", "value1")
        self.assertEqual(len(self.registry), 1)
        
        self.registry.add("key2", "value2")
        self.assertEqual(len(self.registry), 2)
        
        self.registry.remove("key1")
        self.assertEqual(len(self.registry), 1)
    
    def test_repr(self):
        """Test the string representation of the registry."""
        self.registry.add("key1", "value1")
        repr_str = repr(self.registry)
        
        self.assertIn("Registry", repr_str)
        self.assertIn("key1", repr_str)
        self.assertIn("value1", repr_str)
    
    def test_various_value_types(self):
        """Test storing various types of values."""
        self.registry.add("string", "text")
        self.registry.add("int", 42)
        self.registry.add("float", 3.14)
        self.registry.add("list", [1, 2, 3])
        self.registry.add("dict", {"nested": "value"})
        self.registry.add("none", None)
        
        self.assertEqual(self.registry.get("string"), "text")
        self.assertEqual(self.registry.get("int"), 42)
        self.assertEqual(self.registry.get("float"), 3.14)
        self.assertEqual(self.registry.get("list"), [1, 2, 3])
        self.assertEqual(self.registry.get("dict"), {"nested": "value"})
        self.assertIsNone(self.registry.get("none"))


if __name__ == "__main__":
    unittest.main()
