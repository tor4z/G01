from typing import Generic, List, TypeVar


T = TypeVar('T')


class Queue(Generic[T]):
    def __init__(self) -> None:
        self._data: List[T] = []
    
    def en_queue(self, element: T) -> None:
        self._data.append(element)

    def de_queue(self) -> T:
        element = self._data[0]
        self._data = self._data[1:]
        return element

    @property
    def empty(self) -> bool:
        return len(self._data) == 0

    def clean(self) -> None:
        self._data: List[T] = []
