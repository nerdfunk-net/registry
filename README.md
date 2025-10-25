# Registry

A simple and lightweight registry implementation for storing and retrieving key-value pairs in Python.

## Features

- Simple API for adding, getting, and removing items
- Support for any Python object as values
- List all keys or key-value pairs
- Check for key existence with the `in` operator
- Clear all entries at once

## Usage

```python
from registry import Registry

# Create a new registry
reg = Registry()

# Add items
reg.add("name", "John Doe")
reg.add("age", 30)
reg.add("email", "john@example.com")

# Get items
name = reg.get("name")  # Returns "John Doe"
country = reg.get("country", "USA")  # Returns "USA" (default value)

# Check if key exists
if "age" in reg:
    print(f"Age: {reg.get('age')}")

# List all keys
keys = reg.list_keys()  # Returns ['name', 'age', 'email']

# List all items
items = reg.list_items()  # Returns [('name', 'John Doe'), ('age', 30), ...]

# Remove an item
reg.remove("age")

# Get registry size
size = len(reg)

# Clear all items
reg.clear()
```

## Testing

Run the test suite with:

```bash
python -m unittest test_registry.py -v
```

## API Reference

### `Registry()`

Initialize a new empty registry.

### `add(key, value)`

Add or update a key-value pair in the registry.

- **key**: The key to store the value under
- **value**: The value to store
- **Returns**: The stored value

### `get(key, default=None)`

Get a value from the registry by key.

- **key**: The key to look up
- **default**: The default value to return if key is not found
- **Returns**: The value associated with the key, or default if not found

### `remove(key)`

Remove a key-value pair from the registry.

- **key**: The key to remove
- **Returns**: The value that was removed, or None if key was not found

### `list_keys()`

List all keys in the registry.

- **Returns**: A list of all keys in the registry

### `list_items()`

List all key-value pairs in the registry.

- **Returns**: A list of tuples (key, value) for all items in the registry

### `clear()`

Clear all entries from the registry.

### Special Methods

- `len(registry)`: Get the number of items in the registry
- `key in registry`: Check if a key exists in the registry
- `repr(registry)`: Get a string representation of the registry
