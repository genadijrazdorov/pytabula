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