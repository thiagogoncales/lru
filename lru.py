class LRUCacheException(Exception):
    pass


class LRUCache:
    def __init__(self, size):
        self.size = size
        self._set_inner_storage()

    def put(self, key, value):
        if key not in self._inner and self._is_full():
            raise LRUCacheException('I am full!')

        self._inner[key] = value

    def get(self, key):
        return self._inner.get(key)

    def delete(self, key):
        try:
            del self._inner[key]
        except KeyError:
            pass

    def reset(self):
        self._set_inner_storage()

    def _set_inner_storage(self):
        self._inner = {}

    def _is_full(self):
        return len(self._inner) == self.size
