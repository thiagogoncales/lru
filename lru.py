class LRUCache:
    def __init__(self, size):
        self.size = size
        self._set_inner_storage()

    def put(self, key, value):
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
