from collections.abc import Iterable
from typing import Self

from . import abc


class Table(abc.Table):
    columns = tuple()

    def __new__(
        cls,
        sequence_of_rows: abc.abc.Iterable[abc.Row] = None,
        columns: tuple[str] = None,
    ) -> Self:
        obj = super().__new__(cls)
        if sequence_of_rows is None:
            sequence_of_rows = tuple()
        else:
            sequence_of_rows = tuple(sequence_of_rows)
        obj._tbl = sequence_of_rows
        if columns is None:
            columns = tuple()
        else:
            columns = tuple(columns)

        obj.columns = columns
        return obj

    def __getitem__(self, index) -> abc.Item | abc.Row | Self:
        index, col = super().__getitem__(index)

        if isinstance(index, slice):
            if isinstance(col, slice):
                return type(self)(
                    [row[col] for row in self._tbl[index]], self.columns[col]
                )

            elif col is not None:
                return [row[col] for row in self._tbl[index]]

            else:
                return type(self)(self._tbl[index], self.columns)

        elif col is not None:
            return self._tbl[index][col]

        else:
            return self._tbl[index]

    def __len__(self) -> int:
        return len(self._tbl)


class MutableTable(Table, abc.MutableTable):
    def __new__(
        cls,
        sequence_of_rows: abc.abc.Iterable[abc.Row] = None,
        columns: tuple[str] = None,
    ) -> Self:
        obj = super().__new__(cls)
        if sequence_of_rows is None:
            sequence_of_rows = []
        else:
            sequence_of_rows = [list(row) for row in sequence_of_rows]
        obj._tbl = sequence_of_rows

        if columns is None:
            columns = []
        else:
            columns = list(columns)

        obj.columns = columns
        return obj

    def __setitem__(self, index, value) -> None:
        try:
            index, col = super(Table, self).__getitem__(index)

        # append a new column
        except ValueError:
            index, col = index
            if index != slice(None):
                raise ValueError("Can only append whole column")

            for idx, v in enumerate(value):
                self._tbl[idx].append(v)

            self.columns.append(col)

        else:
            if isinstance(index, slice):
                if index == slice(None) and value.columns:
                    self.columns[col] = value.columns
                start, stop, step = index.indices(len(self._tbl))
                value = iter(value)

            else:
                start, stop, step = index, index + 1, 1
                value = iter([value])

            if col is None:
                col = slice(None)

            if isinstance(col, slice):
                for idx in range(start, stop, step):
                    self._tbl[idx][col] = list(next(value))

            else:
                for idx in range(start, stop, step):
                    self._tbl[idx][col] = next(value)

    def __delitem__(self, index) -> None:
        index, col = super(Table, self).__getitem__(index)
        if col is None:
            col = slice(None)

        if index != slice(None) and col != slice(None):
            raise ValueError("Can only delete whole rows or columns")

        # delete whole row(s)
        if index != slice(None):
            del self._tbl[index]

        # delete whole column(s)
        elif col != slice(None):
            for row in self._tbl:
                del row[col]

            del self.columns[col]

    def insert(self, index, value) -> None:
        self._tbl.insert(index, value)
