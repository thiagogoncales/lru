import pytest
from lru import (LRUCache, LRUCacheException)


def test_initializes_empty_cache():
    cache = LRUCache(5)


def test_inserts_and_gets_value():
    cache = LRUCache(5)
    expected_value = 'I am expected'
    mock_key = 'such key'
    cache.put(mock_key, expected_value)
    assert cache.get(mock_key) == expected_value


def test_gets_non_existing_key_returns_none():
    cache = LRUCache(5)
    mock_key = 'I do not exist'
    assert cache.get(mock_key) is None


def test_delete_key():
    cache = LRUCache(5)
    expected_value = 'I am expected'
    mock_key = 'such key'
    cache.put(mock_key, expected_value)
    cache.delete(mock_key)
    assert cache.get(mock_key) is None


def test_delete_non_existent_key_noop():
    cache = LRUCache(5)
    mock_key = 'I do not exist'
    cache.delete(mock_key)
    assert cache.get(mock_key) is None


def test_reset_dict():
    cache = LRUCache(5)
    expected_value = 'I am expected'
    mock_key = 'such key'
    cache.put(mock_key, expected_value)
    cache.reset()
    assert cache.get(mock_key) is None

def test_can_insert_up_to_size():
    size = 5
    cache = LRUCache(size)

    def get_mock_value(key):
        return 'value {}'.format(i)

    for i in range(size):
        cache.put(i, get_mock_value(i))

    for i in range(size):
        assert cache.get(i) == get_mock_value(i)


def test_inserting_when_full_breaks():
    size = 5
    cache = LRUCache(size)

    def get_mock_value(key):
        return 'value {}'.format(i)

    for i in range(size):
        cache.put(i, get_mock_value(i))

    with pytest.raises(LRUCacheException):
        cache.put('no good, it is full', 'mock_value')


def test_updating_value_when_full_works():
    size = 5
    keys = list(range(5))
    cache = LRUCache(size)

    def get_mock_value(key):
        return 'value {}'.format(i)

    for i in keys:
        cache.put(i, get_mock_value(i))

    mock_value = 'updated_value'
    cache.put(keys[0], mock_value)
    assert cache.get(keys[0]) == mock_value
