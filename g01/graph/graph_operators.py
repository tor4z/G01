from typing import List
from .node import Node
from .utils import Queue


def top_sort(node: Node) -> List[Node]:
    dfs_seq: List[Node] = dfs_sort(node)
    return reversed(dfs_seq)


def dfs_sort(node: Node) -> List[Node]:
    result: List[Node] = []
    def _dfs_sort(node: Node) -> None:
        if node.name not in result:
            result.append(node)
            for child in node.children_iter():
                _dfs_sort(child)

    _dfs_sort(node)
    return result


def bfs_sort(node: Node) -> List[Node]:
    result: List[Node] = []
    queue = Queue[Node]()
    queue.en_queue(node)

    while not queue.empty:
        node = queue.de_queue()
        result.append(node)
        for child in node.children_iter():
            if child not in result:
                queue.en_queue(child)

    return result
