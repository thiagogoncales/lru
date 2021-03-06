import pytest
from lru import (
    LRUQueueButFaster,
    LRUQueueException,
    LRUQueueSimple,
)


def test_initialize_and_add_to_queue(LRUQueueParametrized):
    queue = LRUQueueParametrized()
    first_value = 'first'
    second_value = 'second'
    queue.add(first_value)
    queue.add(second_value)
    assert queue.pop() == first_value
    assert queue.pop() == second_value


def test_popping_from_empty_list_raises(LRUQueueParametrized):
    queue = LRUQueueParametrized()
    with pytest.raises(LRUQueueException):
        queue.pop()


def test_remove_element(LRUQueueParametrized):
    queue = LRUQueueParametrized()
    mock_value = 'I am a mock'
    queue.add('some value')
    queue.add(mock_value)
    queue.add('some other value')

    assert queue._test_element_in(mock_value)
    queue.remove(mock_value)
    assert not queue._test_element_in(mock_value)


def test_removing_non_existing_element(LRUQueueParametrized):
    queue = LRUQueueParametrized()
    queue.add('some value')

    with pytest.raises(LRUQueueException):
        queue.remove('I do not exist')
