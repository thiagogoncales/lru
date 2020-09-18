class LRUCacheException(Exception):
    pass

class LRUQueueException(Exception):
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


class LRUQueue:
    def __init__(self):
        self.inner = []

    def add(self, value):
        self.inner.append(value)

    def remove(self, value):
        self.inner.remove(value)

    def pop(self):
        try:
            return self.inner.pop()
        except IndexError:
            raise LRUQueueException('Popping from empty list')

    def _test_is_empty(self):
        return len(self.inner) == 0

    def _test_element_in(self, value):
        return value in self.inner
