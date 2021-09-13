from typing import Generic, NoReturn, TypeVar, List,\
    Generator


T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, value: T, name: str) -> None:
        self._value = value
        self._name = name
        self._children = {}
        self._in_edges = {}
        self._out_edges = {}

    @property
    def value(self) -> T:
        return self._value

    @value.setter
    def value(self, value: T) -> None:
        self._value = value

    @property
    def name(self) -> str:
        return self._value

    @value.setter
    def name(self, *args) -> NoReturn:
        raise RuntimeError(f'Can not rename a node.')

    def add_child(self, child: 'Node') -> None:
        self._children[child.name] = child

    def del_child(self, name: str) -> None:
        child = self._children[name]
        child.detach(self.name)
        del self._children[name]

    def find_child(self, name: str) -> 'Node':
        return self._children[name]

    def exist_child(self, name: str) -> bool:
        return name in self._children

    def children_iter(self) -> Generator['Node']:
        for child in self._children:
            yield child

    def add_children(self, children :List['Node']) -> None:
        for child in children:
            self.add_child(child)

    def set_children(self, children :List['Node']) -> None:
        self.clean_children()
        self.add_children(children)

    def clean_children(self) -> None:
        for child in self._children:
            self.del_child(child)

    def detach(self, parent_name: str) -> None:
        del self._in_edges[parent_name]

    @property
    def empty(self) -> bool:
        return len(self._children) == 0

    def __str__(self) -> str:
        return f'<Node: {self._name}>'

    __repr__ = __str__


class Edge:
    pass
