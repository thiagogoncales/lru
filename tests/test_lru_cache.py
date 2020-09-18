import pytest
from lru import LRUCacheException


def test_initializes_empty_cache(LRUCacheParametrized):
    cache = LRUCacheParametrized(5)


def test_inserts_and_gets_value(LRUCacheParametrized):
    cache = LRUCacheParametrized(5)
    expected_value = 'I am expected'
    mock_key = 'such key'
    cache.put(mock_key, expected_value)
    assert cache.get(mock_key) == expected_value


def test_gets_non_existing_key_returns_none(LRUCacheParametrized):
    cache = LRUCacheParametrized(5)
    mock_key = 'I do not exist'
    assert cache.get(mock_key) is None


def test_delete_key(LRUCacheParametrized):
    cache = LRUCacheParametrized(5)
    expected_value = 'I am expected'
    mock_key = 'such key'
    cache.put(mock_key, expected_value)
    cache.delete(mock_key)
    assert cache.get(mock_key) is None


def test_delete_non_existent_key_noop(LRUCacheParametrized):
    cache = LRUCacheParametrized(5)
    mock_key = 'I do not exist'
    cache.delete(mock_key)
    assert cache.get(mock_key) is None


def test_reset_dict(LRUCacheParametrized):
    cache = LRUCacheParametrized(5)
    expected_value = 'I am expected'
    mock_key = 'such key'
    cache.put(mock_key, expected_value)
    cache.reset()
    assert cache.get(mock_key) is None


def test_can_insert_up_to_size(LRUCacheParametrized):
    size = 5
    cache = LRUCacheParametrized(size)

    def get_mock_value(key):
        return 'value {}'.format(key)

    for i in range(size):
        cache.put(i, get_mock_value(i))

    for i in range(size):
        assert cache.get(i) == get_mock_value(i)


def test_inserting_when_full_removes_lru_key(LRUCacheParametrized):
    size = 5
    keys = list(range(5))
    cache = LRUCacheParametrized(size)

    def get_mock_value(key):
        return 'value {}'.format(key)

    for i in keys:
        cache.put(i, get_mock_value(i))

    new_key = 'should be inserted, even though it is full'
    mock_value = 'mock_value'
    cache.put(new_key, mock_value)

    assert cache.get(new_key) == mock_value

    assert cache.get(keys[0]) is None
    for i in keys[1:]:
        assert cache.get(i) == get_mock_value(i)


def test_assert_get_updates_lru(LRUCacheParametrized):
    size = 2
    old_key_to_be_get = 'old but should not be deleted'
    new_key_but_will_be_deleted = 'new but should be deleted'
    mock_value = 'mock value'

    cache = LRUCacheParametrized(size)

    cache.put(old_key_to_be_get, mock_value)
    cache.put(new_key_but_will_be_deleted, 'some value')

    cache.get(old_key_to_be_get)
    cache.put('a new key appears', 'some other value')

    assert cache.get(old_key_to_be_get) == mock_value
    assert cache.get(new_key_but_will_be_deleted) is None


def test_deleting_lru_key_removes_from_lru_queue(LRUCacheParametrized):
    def get_mock_value(key):
        return 'value {}'.format(key)

    size = 3
    first_key = 'first!'
    second_key = 'second!'
    third_key = 'third!'
    fourth_key = 'fourth!'
    key_add_removes_first = 'fifth!'
    key_add_removes_third = 'sixth!'

    cache = LRUCacheParametrized(size)

    cache.put(first_key, get_mock_value(first_key))
    cache.put(second_key, get_mock_value(second_key))
    cache.put(third_key, get_mock_value(third_key))

    # currently cache is full, with lru as 1, 2, 3
    # delete key 2 so lru becomes 1, 3
    cache.delete(second_key)

    # adding key 4 is fine because it's not full anymore
    # lru is 1, 3, 4
    cache.put(fourth_key, get_mock_value(fourth_key))

    assert cache.get(first_key) == get_mock_value(first_key)
    assert cache.get(third_key) == get_mock_value(third_key)
    assert cache.get(fourth_key) == get_mock_value(fourth_key)
    assert cache.get(second_key) is None

    # adding keys now remove according to lru
    cache.put(key_add_removes_first, get_mock_value(key_add_removes_first))
    cache.put(key_add_removes_third, get_mock_value(key_add_removes_third))

    assert cache.get(fourth_key) == get_mock_value(fourth_key)
    assert cache.get(key_add_removes_first) == \
        get_mock_value(key_add_removes_first)
    assert cache.get(key_add_removes_third) == \
        get_mock_value(key_add_removes_third)
    assert cache.get(first_key) is None
    assert cache.get(third_key) is None


def test_updating_value_when_full_works(LRUCacheParametrized):
    size = 5
    keys = list(range(5))
    cache = LRUCacheParametrized(size)

    def get_mock_value(key):
        return 'value {}'.format(i)

    for i in keys:
        cache.put(i, get_mock_value(i))

    mock_value = 'updated_value'
    cache.put(keys[0], mock_value)
    assert cache.get(keys[0]) == mock_value
