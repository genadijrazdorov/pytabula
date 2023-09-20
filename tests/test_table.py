from pytable import Table, abc

import pytest


@pytest.mark.xfail
def test_fail():
    assert False


@pytest.fixture
def tbl():
    return Table((
        ('ozzy', 'dog', 18),
        ('mary', 'cat', 12)
    ), columns=('name', 'animal', 'age'))
    

class TestTable:
    def test__len__(self, tbl):
        assert len(Table()) == 0
        assert len(Table((1, 2, 3))) == 3
        assert len(tbl) == 2

    def test__eq__(self, tbl):
        assert tbl == Table((
            ('ozzy', 'dog', 18),
            ('mary', 'cat', 12)
        ), columns=('name', 'animal', 'age'))

        assert tbl != Table()

        assert tbl != Table((
            ('ozzy', 'dog', 18),
            ('mary', 'cat', 2)
        ), columns=('name', 'animal', 'age'))

    def test__eq__sequence(self, tbl):
        assert tbl == (
            ('ozzy', 'dog', 18),
            ('mary', 'cat', 12)
        )

    def test__eq__int(self, tbl):
        assert tbl != 1

    def test__hash__(self, tbl):
        assert hash(tbl) == hash((
            ('name', 'animal', 'age'),
            ('ozzy', 'dog', 18),
            ('mary', 'cat', 12)
        ))

    
class TestTable__getitem__:
    def test_single_row(self, tbl):
        assert tbl[0] == ('ozzy', 'dog', 18)

    def test_negative_index(self, tbl):
        assert tbl[-1] == ('mary', 'cat', 12)

    def test_row_slice(self, tbl):
        assert tbl[0:1] == Table((('ozzy', 'dog', 18),), columns=('name', 'animal', 'age'))

    def test_negative_row_slice(self, tbl):
        assert tbl[-1:] == Table((('mary', 'cat', 12),), columns=('name', 'animal', 'age'))

    def test_single_item(self, tbl):
        assert tbl[0, 'name'] == 'ozzy'

    def test_slice_single_column(self, tbl):
        assert isinstance(tbl[0:1, 'name'], tuple)
        assert tbl[0:1, 'name'] == ('ozzy',)

    def test_slice_slice(self, tbl):
        assert tbl[0:1, 'name':'age'] == Table((('ozzy', 'dog'),), columns=('name', 'animal'))