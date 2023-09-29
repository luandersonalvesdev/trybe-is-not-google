from ting_file_management.priority_queue import PriorityQueue
import pytest


MOCK_FILES = [
    {"qtd_linhas": 9},
    {"qtd_linhas": 2},
    {"qtd_linhas": 8},
    {"qtd_linhas": 4}
]


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()

    for file in MOCK_FILES:
        priority_queue.enqueue(file)

    assert priority_queue.dequeue() == MOCK_FILES[1]

    assert priority_queue.search(0) == MOCK_FILES[3]

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(len(priority_queue))
