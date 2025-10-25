"""
A simple registry implementation for storing and retrieving key-value pairs.
"""


class Registry:
    """A registry for storing and managing key-value pairs."""
    
    def __init__(self):
        """Initialize an empty registry."""
        self._storage = {}
    
    def add(self, key, value):
        """
        Add or update a key-value pair in the registry.
        
        Args:
            key: The key to store the value under
            value: The value to store
        
        Returns:
            The stored value
        """
        self._storage[key] = value
        return value
    
    def get(self, key, default=None):
        """
        Get a value from the registry by key.
        
        Args:
            key: The key to look up
            default: The default value to return if key is not found
        
        Returns:
            The value associated with the key, or default if not found
        """
        return self._storage.get(key, default)
    
    def remove(self, key):
        """
        Remove a key-value pair from the registry.
        
        Args:
            key: The key to remove
        
        Returns:
            The value that was removed, or None if key was not found
        """
        return self._storage.pop(key, None)
    
    def list_keys(self):
        """
        List all keys in the registry.
        
        Returns:
            A list of all keys in the registry
        """
        return list(self._storage.keys())
    
    def list_items(self):
        """
        List all key-value pairs in the registry.
        
        Returns:
            A list of tuples (key, value) for all items in the registry
        """
        return list(self._storage.items())
    
    def clear(self):
        """Clear all entries from the registry."""
        self._storage.clear()
    
    def __len__(self):
        """Return the number of items in the registry."""
        return len(self._storage)
    
    def __contains__(self, key):
        """Check if a key exists in the registry."""
        return key in self._storage
    
    def __repr__(self):
        """Return a string representation of the registry."""
        return f"Registry({self._storage})"
