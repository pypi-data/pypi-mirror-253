# simplememcache

[![PyPI version](https://badge.fury.io/py/simplememcache.svg)](https://badge.fury.io/py/simplememcache)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/aj-jaiswal007/SimpleMemCache/blob/main/LICENSE)

`simplememcache` is a lightweight Python package providing a simple and efficient Least Recently Used (LRU) cache implementation. It allows you to cache and manage key-value pairs with a maximum size, automatically evicting the least recently used items when the cache reaches its limit.

## Installation

You can install `simplememcache` using pip:

```bash
pip install simplememcache
```


## Importing the package
```python
from simplememcache.lru import LRUCache
```

## Creating a cache instance
```python
# Create an LRU cache with a maximum size of 100 items
cache = LRUCache(max_size=100)
```

## Inserting items into the cache
```python
cache.insert("key1", "value1")
cache.insert("key2", 42)
```

## Getting items from the cache
```python
value = cache.get("key1")
print(value)  # Output: "value1"
```

## Getting items with default value
```python
value = cache.get_or_default("nonexistent_key", default="default_value")
print(value)  # Output: "default_value"
```

## Upserting items into the cache
```python
# Upsert (update or insert) an item into the cache
result = cache.upsert("key1", "new_value")
print(result)  # Output: False (key1 already existed, value updated)
```

## Deleting items from the cache
```python
deleted_value = cache.delete("key2")
print(deleted_value)  # Output: 42
```

## Deleting items with default value
```python
deleted_value = cache.delete_or_default("nonexistent_key", default="default_value")
print(deleted_value)  # Output: "default_value"
```

## Checking the size of the cache
```python
cache_size = cache.size
print(cache_size)  # Output: 1
```

# Contributing
Feel free to contribute by opening issues or submitting pull requests on the [GitHub repository](https://github.com/aj-jaiswal007/SimpleMemCache).

# License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/aj-jaiswal007/SimpleMemCache/blob/master/LICENSE) file for details.