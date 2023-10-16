[table]: <https://en.wikipedia.org/wiki/Table_(information)>
[Python]: <https://www.python.org/>
[Sequence]: <https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence>
[common sequence operations]: <https://docs.python.org/3/library/stdtypes.html#common-sequence-operations>
[immutable sequence types]: <https://docs.python.org/3/library/stdtypes.html#immutable-sequence-types>
[mutable sequence types]: <https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types>
[alternatives]: #alternatives


<pre id="pytabula-logo">
p     y     t    a     b    u    l   a
----- ----- ---- ----- ---- ---- --- -----
━━━━  ━━━━  ┏┓━  ━━━━  ┓━━  ━━━  ┓━  ━━━━
━━━━  ━━━━  ┛┗┓  ━━━━  ┃━━  ━━━  ┃━  ━━━━
┏━━┓  ┓━┏┓  ┓┏┛  ━━┓━  ┗━┓  ┓┏┓  ┃━  ━━┓━
┃┏┓┃  ┃━┃┃  ┃┃━  ━┓┃━  ┏┓┃  ┃┃┃  ┃━  ━┓┃━
┃┗┛┃  ┗━┛┃  ┃┗┓  ┗┛┗┓  ┗┛┃  ┗┛┃  ┗┓  ┗┛┗┓
┃┏━┛  ━┓┏┛  ┗━┛  ━━━┛  ━━┛  ━━┛  ━┛  ━━━┛
┃┃━━  ━┛┃━  ━━━  ━━━━  ━━━  ━━━  ━━  ━━━━
┗┛━━  ━━┛━  ━━━  ━━━━  ━━━  ━━━  ━━  ━━━━
</pre>

# pytabula

[![Discord](https://img.shields.io/discord/1162022978603728897?logo=discord)](https://discord.gg/yGtDjRhYy7)
[![Static Badge](https://img.shields.io/badge/www-pytabula-_)](https://genadijrazdorov.github.io/pytabula/)
[![Static Badge](https://img.shields.io/badge/pytabula-_?logo=github&logoColor=white&labelColor=black)](https://github.com/genadijrazdorov/pytabula)
[![PyPI - License](https://img.shields.io/pypi/l/pytabula)](LICENSE)
[![PyPI - Version](https://img.shields.io/pypi/v/pytabula)](https://pypi.org/project/pytabula/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pytabula)
[![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/genadijrazdorov/pytabula/python-app.yml)](https://github.com/genadijrazdorov/pytabula/actions/workflows/python-app.yml)
[![CodeQL](https://github.com/genadijrazdorov/pytabula/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/genadijrazdorov/pytabula/actions/workflows/github-code-scanning/codeql)



`pytabula` is a [Python] library for a [tabular data][table] based on [`collections.abc.Sequence`][Sequence].

A table is a sequence of items organized in rows and columns, much like a spreadsheet.
Although it is missing from Python standard library, there are numerous [alternative solutions][alternatives].

`pytabula.Table` is designed to be minimal and intuitive subclass of the [`Sequence`][Sequence] class.
`Table`, as such is a sequence of *rows*, with each row being a sequence of individual *items*.
Rows are indexed numerically and columns are named, allowing every item to be referenced by (row, column) pair.


## Install

`pytabula` can be easily pip installed.

First create and/or activate virtual environment:

~~~
$ python3.11 -m venv venv
$ source venv/bin/activate
(venv) $

~~~

pip install `pytabula` into virtual environment:

~~~
(venv) $ python -m pip install pytabula
Collecting pytabula
  Using cached pytabula-0.2.0-py3-none-any.whl (5.9 kB)
Installing collected packages: pytabula
Successfully installed pytabula-0.2.0
(venv) $

~~~

Check that `pytabula` is importable:

~~~
(venv) $ python -c "import pytabula as pt; print(pt.__pytabula__)"
p     y     t    a     b    u    l   a
----- ----- ---- ----- ---- ---- --- -----
━━━━  ━━━━  ┏┓━  ━━━━  ┓━━  ━━━  ┓━  ━━━━
━━━━  ━━━━  ┛┗┓  ━━━━  ┃━━  ━━━  ┃━  ━━━━
┏━━┓  ┓━┏┓  ┓┏┛  ━━┓━  ┗━┓  ┓┏┓  ┃━  ━━┓━
┃┏┓┃  ┃━┃┃  ┃┃━  ━┓┃━  ┏┓┃  ┃┃┃  ┃━  ━┓┃━
┃┗┛┃  ┗━┛┃  ┃┗┓  ┗┛┗┓  ┗┛┃  ┗┛┃  ┗┓  ┗┛┗┓
┃┏━┛  ━┓┏┛  ┗━┛  ━━━┛  ━━┛  ━━┛  ━┛  ━━━┛
┃┃━━  ━┛┃━  ━━━  ━━━━  ━━━  ━━━  ━━  ━━━━
┗┛━━  ━━┛━  ━━━  ━━━━  ━━━  ━━━  ━━  ━━━━

(venv) $

~~~


## Use

`pytabula` introduces two classes, namely `Table` and `MutableTable`, as subclasses of `Sequence` and `MutableSequence`.
This implies that you can utilize `Table` and `MutableTable` in a manner similar to how you would use `tuple` and `list`, respectively. In this context, we'll exclusively showcase the enhancements made to this API.


~~~python
>>> # import
>>> import pytabula as tbl

>>> # initialization
>>> t = tbl.Table([
...     ('ozzy', 'dog', 18),
...     ('marry', 'cat', 10),
... ], columns=('name', 'animal', 'age'))

>>> print(t)
name   animal  age
------ ------- ----
ozzy   dog       18
marry  cat       10

~~~

## Table operations

### Common Table Operations

Check [common sequence operations] for full overview.

#### Contains

<details>
<summary>show/hide sequence api</summary>

###### Sequence
~~~python
>>> # row in table
>>> ('marry', 'cat', 10) in t
True

>>> # item in table
>>> any('dog' in row for row in t)
True

>>> # row not in table
>>> ('ozzy', 'cat', 18) not in t
True

>>> # item not in table
>>> any('bird' not in row for row in t)
True

~~~

</details>

###### Table
~~~python
>>> # row in table
>>> ('marry', 'cat', 10) in t
True

>>> # item in table
>>> 'dog' in t
True

>>> # row not in table
>>> ('ozzy', 'cat', 18) not in t
True

>>> # item not in table
>>> 'bird' not in t
True

~~~

#### Get item


<details>
<summary>show/hide sequence api</summary>

###### Sequence
~~~python
>>> import enum
>>> class Col(enum.IntEnum):
...     NAME = 0
...     ANIMAL = 1
...     AGE = 2

>>> # row indexing
>>> t[0]
('ozzy', 'dog', 18)

>>> # item indexing
>>> t[1][Col.ANIMAL]
'cat'

>>> # row slicing
>>> t[:1]
Table([('ozzy', 'dog', 18)], columns=('name', 'animal', 'age'))

>>> # column slicing
>>> t[0][:Col.AGE]
('ozzy', 'dog')

>>> # rectangle
>>> tbl.Table([r[:Col.AGE] for r in t[:1]], columns=t.columns[:Col.AGE])
Table([('ozzy', 'dog')], columns=('name', 'animal'))

~~~

</details>

###### Table
~~~python
>>> # import enum
>>> # class Col(enum.IntEnum):
>>> #     NAME = 0
>>> #     ANIMAL = 1
>>> #     AGE = 2

>>> # row indexing
>>> t[0]
('ozzy', 'dog', 18)

>>> # item indexing
>>> t[1, 'animal']
'cat'

>>> # row slicing
>>> t[:1]
Table([('ozzy', 'dog', 18)], columns=('name', 'animal', 'age'))

>>> # column slicing
>>> t[0, :'age']
('ozzy', 'dog')

>>> # rectangle
>>> t[:1, :'age']
Table([('ozzy', 'dog')], columns=('name', 'animal'))

~~~

#### Index and count

<details>
<summary>show/hide sequence api</summary>

###### Sequence
~~~python
>>> # row index
>>> t.index(('marry', 'cat', 10))
1

>>> # item index
>>> row, col = next((i, Col(r.index(18))) for i, r in enumerate(t) if 18 in r)
>>> row, col
(0, <Col.AGE: 2>)

>>> t[row][col]
18

>>> # row count
>>> t.count(('ozzy', 'dog', 18))
1

>>> # item count
>>> sum(r.count('cat') for r in t)
1

~~~

</details>

###### Table
~~~python
>>> # row index
>>> t.index(('marry', 'cat', 10))
1

>>> # item index
>>> row, col = t.index(18)
>>> row, col
(0, 'age')

>>> t[row, col]
18

>>> # row count
>>> t.count(('ozzy', 'dog', 18))
1

>>> # item count
>>> t.count('cat')
1

~~~

### Immutable Table types

Check [immutable sequence types] for full overview.


### Mutable Table operations

Check [mutable sequence types] for full overview.

#### Set item
<details>
<summary>show/hide sequence api</summary>

###### Sequence
~~~python
>>> mt = tbl.MutableTable(list(t), columns=t.columns)

>>> # row update
>>> mt[0] = ('harry', 'mouse', 2)
>>> print(mt)
name   animal  age
------ ------- ----
harry  mouse      2
marry  cat       10

>>> # item update
>>> mt[0][Col.ANIMAL] = 'python'
>>> print(mt)
name   animal  age
------ ------- ----
harry  python     2
marry  cat       10

>>> # slice update
>>> for row, value in zip(mt, [('rabbit', 3), ('spider', 1)]):
...     row[Col.ANIMAL:] = value
>>> print(mt)
name   animal  age
------ ------- ----
harry  rabbit     3
marry  spider     1

~~~

</details>

###### Table
~~~python
>>> mt = tbl.MutableTable(list(t), columns=t.columns)

>>> # row update
>>> mt[0] = ('harry', 'mouse', 2)
>>> print(mt)
name   animal  age
------ ------- ----
harry  mouse      2
marry  cat       10

>>> # item update
>>> mt[0, 'animal'] = 'python'
>>> print(mt)
name   animal  age
------ ------- ----
harry  python     2
marry  cat       10

>>> # slice update

>>> mt[:, 'animal':] = tbl.Table([('rabbit', 3), ('spider', 1)])
>>> print(mt)
name   animal  age
------ ------- ----
harry  rabbit     3
marry  spider     1

~~~

##### Append column
<details>
<summary>show/hide sequence api</summary>

###### Sequence
~~~python
>>> mt = tbl.MutableTable(list(t), columns=t.columns)

>>> for row, value in zip(mt, ('chicken', 'fish')):
...     row.append(value)
>>> mt.columns.append('food')
>>> print(mt)
name   animal  age  food
------ ------- ---- --------
ozzy   dog       18 chicken
marry  cat       10 fish

~~~

</details>

###### Table
~~~python
>>> mt = tbl.MutableTable(list(t), columns=t.columns)



>>> mt[:, 'food'] = ('chicken', 'fish')
>>> print(mt)
name   animal  age  food
------ ------- ---- --------
ozzy   dog       18 chicken
marry  cat       10 fish

~~~

##### Insert column(s)
<details>
<summary>show/hide sequence api</summary>

###### Sequence
~~~python
>>> mt = tbl.MutableTable(list(t), columns=t.columns)

>>> for row, value in zip(mt, ('big', 'small')):
...     row[Col.AGE: Col.AGE] = (value,)
>>> mt.columns[Col.AGE: Col.AGE] = ('size',)
>>> print(mt)
name   animal  size   age
------ ------- ------ ----
ozzy   dog     big      18
marry  cat     small    10

~~~

</details>

###### Table
~~~python
>>> mt = tbl.MutableTable(list(t), columns=t.columns)



>>> mt[:, 'age':'age'] = tbl.Table([('big',), ('small',)], columns=('size',))
>>> print(mt)
name   animal  size   age
------ ------- ------ ----
ozzy   dog     big      18
marry  cat     small    10

~~~

#### Delete item
<details>
<summary>show/hide sequence api</summary>

###### Sequence
~~~python
>>> mt = tbl.MutableTable(list(t), columns=t.columns)

>>> # row deleting
>>> del mt[1]
>>> print(mt)
name  animal  age
----- ------- ----
ozzy  dog       18

>>> # column deleting
>>> for row in mt:
...     del row[Col.AGE]
>>> del mt.columns[Col.AGE]
>>> print(mt)
name  animal
----- -------
ozzy  dog

~~~

</details>

###### Table
~~~python
>>> mt = tbl.MutableTable(list(t), columns=t.columns)

>>> # row deleting
>>> del mt[1]
>>> print(mt)
name  animal  age
----- ------- ----
ozzy  dog       18

>>> # column deleting


>>> del mt[:, 'age']
>>> print(mt)
name  animal
----- -------
ozzy  dog

~~~
