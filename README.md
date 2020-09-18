# LRU

## Description
Implements an in-code LRU Cache. Allows to set a maximum size and any inserts after it is full removes the Least Recently Used key. 

Usage:
```py
from lru import LRUCache

# initialize it with some size
cache = LRUCache(20)

# add keys to it
cache.add('my key', 'some value')
cache.add('some other key', 'some other value')

# get values
cache.get('my key') # 'some value'

# remove from cache
cache.delete('some other key') 

# deleting non existing key is OK
cache.delete('I do not exist') # OK!

# if it's full, it rmeoves the least recently used item
cache = LRUCache(3)
cache.add('key 1', 'value 1')
cache.add('key 2', 'value 2')
cache.add('key 3', 'value 3')
cache.add('key 4', 'value 4') # 'key 1' was removed to make space for 'key 4'!

# if you read a key, it also accounts for the LRU queue
cache.get('key 2) # now LRU is 'key 3'!
cache.add('key 5', 'value 5') # 'key 3' was removed to make space for 'key 5'!
```

## How to use
- Install Python 3.8 and pipenv
- `make install`
- `make test`

## Explanation
### LRU Cache
LRUCache is very straightforward. It implements the cache as a Python dictionary. Whenever you insert, it first checks if it's full and if it is, gets the LRU from its internal LRUQueue and removes that item.
LRUCache also needs to update the LRUQueue on insert and read (so that key is the most recently used) and on remove (it's a stale key in the Queue otherwise).

### LRU Queue
A simple implementation of the Queue. In essence, it's just an array. It exposes methods to add to the end of the array, pop from the beginning and remove an item from the array.
As a simple implementation, it has as time complexity (N is number of keys in cache/queue):
- add - O(1)
- remove - O(N)
- pop - O(N) (we are popping from the start, so yea) 

## FAQ
*What were you listening to while doing this?*
Ne Obliviscaris - Citadel
