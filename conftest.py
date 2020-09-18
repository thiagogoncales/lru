import pytest

from lru import (
    LRUCache,
    LRUQueueButFaster,
    LRUQueueSimple,
)


@pytest.fixture(params=[LRUQueueSimple, LRUQueueButFaster])
def LRUQueueParametrized(request):
    return request.param


@pytest.fixture
def LRUCacheParametrized(LRUQueueParametrized):
    def _LRUCache(*args, **kwargs):
        return LRUCache(
            *args,
            queue_constructor=LRUQueueParametrized,
            **kwargs,
        )

    return _LRUCache
