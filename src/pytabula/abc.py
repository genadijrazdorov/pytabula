from collections import abc
from abc import abstractmethod
from typing import Any, Self, TypeAlias


Item: TypeAlias = Any
Row: TypeAlias = tuple[Item, ...]


class Table(abc.Sequence):
    """All the operations on a read-only table.

    Concrete subclasses must override columns, __new__, __getitem__, and __len__.

    """

    @property
    @abstractmethod
    def columns(self) -> tuple[str]:
        "T.columns -> returns columns' names"
        return tuple()  # pragma: no cover

    @abstractmethod
    def __new__(
        cls, sequence_of_rows: abc.Iterable[Row] = None, columns: tuple[str] = None
    ) -> Self:
        return super().__new__(cls)

    @abstractmethod
    def __getitem__(self, index) -> Item | Row | Self:
        if isinstance(index, tuple):
            index, col = index
            if isinstance(col, slice):
                start, stop = col.start, col.stop
                try:
                    start = self.columns.index(start)

                except ValueError:
                    if start is None:
                        start = 0
                    else:
                        raise ValueError(f"{start} not in columns")

                try:
                    stop = self.columns.index(stop)

                except ValueError:
                    if stop is None:
                        stop = len(self.columns)
                    else:
                        raise ValueError(f"{stop} not in columns")

                col = slice(start, stop)

            else:
                col = self.columns.index(col)

        else:
            col = None

        return index, col

    @abstractmethod
    def __len__(self) -> int:
        return 0  # pragma: no cover

    def __contains__(self, item_or_row: Item | Row) -> bool:
        if super().__contains__(item_or_row):
            return True

        for row in self:
            if item_or_row in row:
                return True

        return False

    def index(self, item_or_row: Item | Row) -> int | tuple[int, str]:
        "T.index(x) -> integer index of x in T; raises ValueError if not found"
        try:
            return super().index(item_or_row)

        except ValueError:
            for i, row in enumerate(self):
                if item_or_row in row:
                    return i, self.columns[row.index(item_or_row)]

        raise ValueError(f"{item_or_row} not found")

    def count(self, item_or_row: Item | Row) -> int:
        "T.count(x) -> number of occurrences of x in T"
        if count := super().count(item_or_row):
            return count

        else:
            # TODO: this is a row count, not an item count!
            return sum(1 for row in self if item_or_row in row)

    def __hash__(self) -> int:
        return hash((self.columns, *list(self)))

    def __eq__(self, other: Self) -> bool:
        try:
            if len(self) != len(other) or self.columns != other.columns:
                return False

        except TypeError:
            return NotImplemented

        except AttributeError:
            pass

        for s, o in zip(self, other):
            if s != o:
                return False

        else:
            return True

    def __lt__(self, other: Self) -> bool:
        if not isinstance(other, Table):
            raise TypeError(f"{other} is not a Table")

        for s, o in zip(self, other):
            if not s < o:
                return False

        else:
            return True

    def __add__(self, other: Self) -> Self:
        assert self.columns == other.columns

        return type(self)(tuple(self) + tuple(other), columns=self.columns)

    def __mul__(self, other: int) -> Self:
        return type(self)(tuple(self) * other, columns=self.columns)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({list(self)}, columns={self.columns})"

    def __str__(self) -> str:
        size = [len(c) for c in self.columns]
        for row in self:
            for i, c in enumerate(row):
                size[i] = max(size[i], len(str(c)))

        t = " ".join(f"{{:{s + 1}}}" for s in size)
        s = [t.format(*self.columns).rstrip()]
        s.append(t.format(*("-" * (i + 1) for i in size)).rstrip())
        s.extend(t.format(*row).rstrip() for row in self)

        return "\n".join(s)


class MutableTable(Table, abc.MutableSequence):
    """All the operations on a read-write table.

    Concrete subclasses must override columns, __new__, __getitem__, __len__, __setitem__, __delitem__ and insert().

    """

    __hash__ = None

    @abstractmethod
    def __setitem__(self, index, value: Item | Row | Self) -> None:
        pass  # pragma: no cover

    @abstractmethod
    def __delitem__(self, index) -> None:
        pass  # pragma: no cover

    @abstractmethod
    def insert(self, index: int, row: Row) -> None:
        "T.insert(index, row) -> insert row at index"
        pass  # pragma: no cover
