class LRUCacheException(Exception):
    pass

class LRUQueueException(Exception):
    pass


class LRUCache:
    def __init__(self, size):
        self.size = size
        self._set_inner_storage()

    def put(self, key, value):
        self._add_key_to_lru_queue(key)

        if self._is_full():
            key_to_remove = self._get_lru_key_to_remove()
            self.delete(key_to_remove)

        self._inner[key] = value

    def get(self, key):
        self._add_key_to_lru_queue(key)
        return self._inner.get(key)

    def delete(self, key):
        try:
            del self._inner[key]
        except KeyError:
            pass

        try:
            self._inner_q.remove(key)
        except LRUQueueException:
            pass

    def reset(self):
        self._set_inner_storage()

    def _set_inner_storage(self):
        self._inner = {}
        self._inner_q = LRUQueue()

    def _is_full(self):
        return len(self._inner) == self.size

    def _has_key(self, key):
        return key in self._inner

    def _add_key_to_lru_queue(self, key):
        if self._has_key(key):
            self._inner_q.remove(key)

        self._inner_q.add(key)

    def _get_lru_key_to_remove(self):
        return self._inner_q.pop()


class LRUQueue:
    def __init__(self):
        self.inner = []

    def add(self, value):
        self.inner.append(value)

    def remove(self, value):
        try:
            self.inner.remove(value)
        except ValueError:
            raise LRUQueueException('key not in queue')

    def pop(self):
        try:
            return self.inner.pop(0)
        except IndexError:
            raise LRUQueueException('Popping from empty list')

    def _test_is_empty(self):
        return len(self.inner) == 0

    def _test_element_in(self, value):
        return value in self.inner
