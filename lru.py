class LRUCacheException(Exception):
    pass

class LRUQueueException(Exception):
    pass


class LRUQueueSimple:
    def __init__(self):
        self.inner = []

    def add(self, value):
        try:
            self.remove(value)
        except LRUQueueException:
            pass

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


class LRUQueueButFaster:
    class Node:
        def __init__(self, value, previous_node=None, next_node=None):
            self.value = value
            self.previous_node = previous_node
            self.next_node = next_node

    def __init__(self):
        self._least_recently_used_node = None
        self._most_recently_used_node = None
        self._nodes_map = {}

    def add(self, value):
        if value in self._nodes_map:
            self.remove(value)

        new_node = self.Node(
            value,
            previous_node=self._most_recently_used_node,
        )

        if self._most_recently_used_node is not None:
            self._most_recently_used_node.next_node = new_node
        self._most_recently_used_node = new_node

        if self._least_recently_used_node is None:
            self._least_recently_used_node = new_node
        self._nodes_map[value] = new_node

    def remove(self, value):
        if value not in self._nodes_map:
            raise LRUQueueException('key not in queue')

        node_to_remove = self._nodes_map[value]

        if node_to_remove.previous_node:
            node_to_remove.previous_node.next_node = node_to_remove.next_node
        else:
            self._least_recently_used_node = node_to_remove.next_node

        if node_to_remove.next_node:
            node_to_remove.next_node = node_to_remove.previous_node
        else:
            self._most_recently_used_node = node_to_remove.previous_node

        del self._nodes_map[value]
        del node_to_remove

    def pop(self):
        node_to_return = self._least_recently_used_node

        if node_to_return is None:
            raise LRUQueueException('Popping from empty list')

        self._least_recently_used_node = node_to_return.next_node

        is_only_node_in_list = node_to_return.next_node is None
        if is_only_node_in_list:
            self._most_recently_used_node = None

        del self._nodes_map[node_to_return.value]
        return node_to_return.value

    def _test_is_empty(self):
        return len(self._nodes_map) == 0

    def _test_element_in(self, value):
        return value in self._nodes_map


class LRUCache:
    def __init__(self, size, queue_constructor=LRUQueueButFaster):
        self.size = size
        self._queue_constructor = queue_constructor
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
        self._inner_q = self._queue_constructor()

    def _is_full(self):
        return len(self._inner) == self.size

    def _has_key(self, key):
        return key in self._inner

    def _add_key_to_lru_queue(self, key):
        self._inner_q.add(key)

    def _get_lru_key_to_remove(self):
        return self._inner_q.pop()
