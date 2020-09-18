from lru import (
    LRUCache,
    LRUQueueButFaster,
    LRUQueueSimple,
)

import time

SIZE = 1000

def timer(queue_type):
    cache = LRUCache(SIZE, queue_constructor=queue_type)
    simple_initial_time = time.time()
    for i in range(SIZE * 10):
        cache.put(i, 'value {}'.format(i))
    return time.time() - simple_initial_time


if __name__ == '__main__':
    print('Simple took {}s'.format(timer(LRUQueueSimple)))
    print('ButFaster took {}s'.format(timer(LRUQueueButFaster)))
