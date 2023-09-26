from . import abc


class Table(abc.Table):
    columns = tuple()
    
    def __new__(cls, sequence_of_rows: list[tuple] = None, columns: list[str] = None):
        obj = super().__new__(cls)
        if sequence_of_rows is None:
            sequence_of_rows = []
        obj._tbl = sequence_of_rows
        if columns is None:
            columns = tuple()
        else:
            columns = tuple(columns)
        
        obj.columns = columns
        return obj

    def __getitem__(self, index):
        index, col = super().__getitem__(index)
            
        if isinstance(index, slice):
            if isinstance(col, slice):
                return Table([row[col] for row in self._tbl[index]], self.columns[col])
            else:
                return tuple(row[col] for row in self._tbl[index])
        else:
            return self._tbl[index][col]
    
    def __len__(self):
        return len(self._tbl)


class MutableTable(Table, abc.MutableTable):
    def __setitem__(self, index, value):
        try:
            index, col = super(Table, self).__getitem__(index)

        # append a new column
        except ValueError:
            index, col = index
            if index != slice(None):
                raise ValueError("Can only append whole column")

            for idx, v in enumerate(value):
                row = list(self._tbl[idx])
                row.append(v)
                self._tbl[idx] = tuple(row)

            columns = list(self.columns)
            columns.append(col)
            self.columns = tuple(columns)
            
        else:
            if isinstance(index, slice):
                if index == slice(None) and value.columns:
                    columns = list(self.columns)
                    columns[col] = value.columns
                    self.columns = tuple(columns)
                start, stop, step = index.indices(len(self._tbl))
                value = iter(value)

            else:
                start, stop, step = index, index + 1, 1
                value = iter([value])

            for idx in range(start, stop, step):
                row = list(self._tbl[idx])
                row[col] = next(value)
                self._tbl[idx] = tuple(row)

    def __delitem__(self, index):
        index, col = super(Table, self).__getitem__(index)
        if index != slice(None) and col != slice(None):
            raise ValueError("Can only delete whole rows or columns")
        
        if index != slice(None):
            del self._tbl[index]

        elif col != slice(None):
            for idx, row in enumerate(self._tbl):
                row = list(row)
                del row[col]
                self._tbl[idx] = tuple(row)

            columns = list(self.columns)
            del columns[col]
            self.columns = tuple(columns)

    def insert(self, index, value):
        self._tbl.insert(index, value)