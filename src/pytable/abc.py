from collections import abc
from abc import abstractmethod
from typing import Self


class Table(abc.Sequence):
    @property
    @abstractmethod
    def columns(self):
        return tuple()      # pragma: no cover
    
    def __repr__(self):
        return f'{self.__class__.__name__}({list(self)}, columns={self.columns})'

    def __str__(self):
        size = [len(c) for c in self.columns]
        for row in self:
            for i, c in enumerate(row):
                size[i] = max(size[i], len(str(c)))

        t = ' '.join(f'{{:{s + 1}}}' for s in size) + '\n'
        s = t.format(*self.columns)
        s += t.format(*('-' * (i + 1) for i in size))
        for row in self:
            s += t.format(*row)

        return s[:-1]
    
    @abstractmethod
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    @abstractmethod
    def __getitem__(self, index):
        if isinstance(index, tuple):
            index, col = index
            if isinstance(col, slice):
                s = self.columns.index(col.start)
                e = self.columns.index(col.stop)
                col = slice(s, e)
            else:
                col = self.columns.index(col)
        
        else:
            col = slice(None)

        return index, col
    
    @abstractmethod
    def __len__(self):
        return 0            # pragma: no cover

    def __contains__(self, row_or_item) -> bool:
        if super().__contains__(row_or_item):
            return True

        for row in self:
            if row_or_item in row:
                return True
            
        return False
    
    def index(self, item):
        pass
    
    def count(self, item):
        pass


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
        pass
    
    def __le__(self, other: Self) -> bool:
        pass
    
    def __gt__(self, other: Self) -> bool:
        pass
    
    def __ge__(self, other: Self) -> bool:
        pass
    

    def __add__(self, other: Self) -> Self:
        pass
    
    def __mul__(self, other: int) -> Self:
        pass