from lru import LRUCache


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
