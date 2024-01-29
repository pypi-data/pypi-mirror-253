import eurostat
from deprecated.classic import deprecated
from pandas.core.frame import DataFrame
from typing import Any, Dict, Iterable, List, Optional, Tuple, Union

from drb.core.path import ParsedPath
from drb.core.node import DrbNode
from drb.core.factory import DrbFactory
from drb.core.predicate import Predicate
from drb.exceptions.core import DrbException, DrbFactoryException
from drb.nodes.abstract_node import AbstractNode


class DrbEurostatServiceNode(AbstractNode):
    """
    Represent a node for browsing Eurostat data.

    Its attribute "tables" contain the list of all the available
    dataset and tables in the eurostat service.
    Its children is a list of DrbEurostatDataNode that can be browsed
    by dataset code.
    This node has no implementations.
    """

    def __init__(self):
        super().__init__()
        self.name = 'Eurostat service'
        self._path = 'eurostat://'
        toc = eurostat.get_toc()
        self._data = [r for r in toc if r[2] in ['dataset', 'table']]
        self.__init_attributes()

    def __init_attributes(self):
        tables = [(r[0], r[1]) for r in self._data]
        self @= ('tables', tables)

    @property
    def path(self) -> ParsedPath:
        return ParsedPath(self._path)

    @property
    @deprecated(version='1.2.0',
                reason='Usage of the bracket is recommended')
    def children(self) -> List[DrbNode]:
        return EurostatDataList(self, self._data)

    def _get_named_child(self, name: str, namespace_uri: str = None,
                         occurrence: Union[int, slice] = 0
                         ) -> Union[DrbNode, List[DrbNode]]:
        if namespace_uri is not None:
            raise DrbException('namespace_uri not supported for this node')
        if not occurrence == 0:
            raise DrbException('occurrence not supported for this node')
        code = name.upper()
        children = [child for child in self._data if child[1] == code]
        if len(children) <= 0:
            raise DrbException(f'No child found having name: {name}')
        index = self._data.index(children[0])
        return self.children[index]

    def __getitem__(self, item):
        if isinstance(item, Predicate):
            raise KeyError(f"{type(item)} type not supported.")
        return super().__getitem__(item)

    def __setitem__(self, key, value):
        raise NotImplementedError

    def __delitem__(self, key):
        raise NotImplementedError


class DrbEurostatDataNode(AbstractNode):
    """
    Represent an Eurostat dataset or table.

    Its attribute "columns" contain the list of the data available
    in this dataset or table.
    Its children is a list of DrbEurostatRowNode that can be browsed
    only by its index in the table.
    This node can return DataFrame implementation.
    """

    def __init__(self, parent: DrbEurostatServiceNode, name, code):
        super().__init__()
        self.parent = parent
        self.name = name
        self._path = 'eurostat://' + code
        self._code = code
        data = eurostat.get_data(code)
        self._header = data[0]
        self._data = data[1:]
        self.__imatmul__(('columns', self._header))
        self.add_impl(DataFrame, self._to_panda_dataframe)
        self._available_impl = [DataFrame]

    @property
    def path(self) -> ParsedPath:
        return ParsedPath(self._path)

    @property
    @deprecated(version='1.2.0',
                reason='Usage of the bracket is recommended')
    def children(self) -> List[DrbNode]:
        return EurostatRowList(self, self._header, self._data)

    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            return self.children[item]
        elif isinstance(item, (Predicate, str, tuple)):
            raise KeyError(f"Invalid key: {type(item)} type not supported.")
        raise TypeError(f"{type(item)} type not supported.")

    def __setitem__(self, key, value):
        raise NotImplementedError

    def __delitem__(self, key):
        raise NotImplementedError

    @staticmethod
    def _to_panda_dataframe(node: DrbNode, **kwargs) -> DataFrame:
        if isinstance(node, DrbEurostatDataNode):
            return eurostat.get_data_df(node._code)
        raise TypeError(f"Invalid node type: {type(node)}")


class DrbEurostatRowNode(AbstractNode):
    """
    Represent a single row of an eurostat dataset or table.

    Its attribute "columns" contain the list of the data available
    in this row.
    Its children is a list of DrbEurostatValueNode that can be browsed
    by index or name of the column.
    This node has noimplementations.
    """

    def __init__(self, parent: DrbEurostatDataNode, header, data, index: str):
        super().__init__()
        self.name = parent.name + str(index)
        self._path = parent.path / str(index)
        self.parent = parent
        self._header = header
        self._data = data
        self.__init_attributes()

    def __init_attributes(self):
        for e in self.parent.attribute_names():
            value = self.parent @ e[0]
            self @= (e[0], value)

    @property
    def path(self) -> ParsedPath:
        return self._path

    @property
    @deprecated(version='1.2.0',
                reason='Usage of the bracket is recommended')
    def children(self) -> List[DrbNode]:
        children = []
        for i in range(len(self._header)):
            children.append(DrbEurostatValueNode(
                self, self._header[i], self._data[i]))
        return children

    def __getitem__(self, item):
        if isinstance(item, Predicate):
            raise KeyError(f"{type(item)} type not supported.")
        return super().__getitem__(item)

    def __setitem__(self, key, value):
        raise NotImplementedError

    def __delitem__(self, key):
        raise NotImplementedError


class DrbEurostatValueNode(AbstractNode):
    """
    Represent a single Eurostat value from a dataset or table.

    """

    def __init__(self, parent: DrbEurostatRowNode, name, value):
        super().__init__()
        self.parent = parent
        self.name = name
        self.value = value

    @property
    @deprecated(version='1.2.0',
                reason='Usage of the bracket is recommended')
    def children(self) -> List[DrbNode]:
        return []

    def __setitem__(self, key, value):
        raise NotImplementedError

    def __delitem__(self, key):
        raise NotImplementedError


class EurostatRowList(list):

    def __init__(self, node: DrbEurostatDataNode, header, data):
        super().__init__()
        self._node = node
        self._header = header
        self._data = data

    def __getitem__(self, item):

        if isinstance(item, slice):
            sliced_list = self._data[item]
            return EurostatRowList(self._node, self._header, sliced_list)

        elif isinstance(item, int):
            if item <= len(self._data):
                row = self._data[item]
                node = DrbEurostatRowNode(self._node, self._header, row, item)
                return node
            else:
                raise IndexError
        elif isinstance(item, (Predicate, str, tuple)):
            raise KeyError(f'Invalid key: {type(item)}')
        else:
            raise TypeError(f"{type(item)} type not supported.")

    def __iter__(self):
        def gen():
            i = 0
            while i < len(self._data):
                row = self._data[i]
                node = DrbEurostatRowNode(self._node, self._header, row, i)
                yield node
                i += 1
        return gen()

    def __len__(self):
        return len(self._data)

    def append(self, obj: Any) -> None:
        raise NotImplementedError

    def clear(self) -> None:
        raise NotImplementedError

    def copy(self) -> List[DrbEurostatDataNode]:
        raise NotImplementedError

    def count(self, value: Any) -> int:
        raise NotImplementedError

    def extend(self, iterable: Iterable[DrbEurostatDataNode]) -> None:
        raise NotImplementedError

    def index(self, value: Any, start: int = ..., stop: int = ...) -> int:
        raise NotImplementedError

    def insert(self, index: int, obj: DrbEurostatDataNode) -> None:
        raise NotImplementedError

    def pop(self, index: int = ...) -> DrbEurostatDataNode:
        raise NotImplementedError

    def remove(self, value: Any) -> None:
        raise NotImplementedError

    def reverse(self) -> None:
        raise NotImplementedError

    def sort(self: List, *, key: None = ..., reverse: bool = ...) -> None:
        raise NotImplementedError


class EurostatDataList(list):

    def __init__(self, node: DrbEurostatServiceNode, data):
        super().__init__()
        self._node = node
        self._data = data

    def __getitem__(self, item):

        if isinstance(item, slice):
            sliced_list = self._data[item]
            return EurostatDataList(self._node, sliced_list)

        elif isinstance(item, int):
            if item <= len(self._data):
                data = self._data[item]
                node = DrbEurostatDataNode(self._node, data[0], data[1])
                return node
            else:
                raise IndexError
        else:
            raise KeyError(f'Invalid key: {type(item)}')

    def __iter__(self):
        def gen():
            i = 0
            while i < len(self._data):
                data = self._data[i]
                node = DrbEurostatDataNode(self._node, data[0], data[1])
                yield node
                i += 1
        return gen()

    def __len__(self):
        return len(self._data)

    def append(self, obj: Any) -> None:
        raise NotImplementedError

    def clear(self) -> None:
        raise NotImplementedError

    def copy(self) -> List[DrbEurostatDataNode]:
        raise NotImplementedError

    def count(self, value: Any) -> int:
        raise NotImplementedError

    def extend(self, iterable: Iterable[DrbEurostatDataNode]) -> None:
        raise NotImplementedError

    def index(self, value: Any, start: int = ..., stop: int = ...) -> int:
        raise NotImplementedError

    def insert(self, index: int, obj: DrbEurostatDataNode) -> None:
        raise NotImplementedError

    def pop(self, index: int = ...) -> DrbEurostatDataNode:
        raise NotImplementedError

    def remove(self, value: Any) -> None:
        raise NotImplementedError

    def reverse(self) -> None:
        raise NotImplementedError

    def sort(self: List, *, key: None = ..., reverse: bool = ...) -> None:
        raise NotImplementedError


class DrbEurostatFactory(DrbFactory):

    def _create(self,  node: DrbNode) -> DrbNode:
        if not node.path.scheme == 'eurostat':
            raise DrbFactoryException(
                'Incorrect path, path must start with "eurostat://"')
        table_name = node.path.netloc
        if table_name:
            try:
                node = DrbEurostatServiceNode()[table_name]
                return node
            except (DrbException, KeyError):
                raise DrbFactoryException(
                    f'table {table_name} not found')
        return DrbEurostatServiceNode()
