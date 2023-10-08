# pytabula

[table]: <https://en.wikipedia.org/wiki/Table_(information)>
[sequence]: <https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence>

[Table][table] is a [sequence] of objects organized in rows and columns.
Rows are numbered and columns are named.

Table is a subclass of [`collections.abc.Sequence`][sequence], specifically a sequence-of-sequences.

## Table

~~~python
>>> # import
>>> from pytabula import Table, MutableTable as MTable

>>> # initialization
>>> t = Table([
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

Common Table operations extends [common Sequence operations](<https://docs.python.org/3/library/stdtypes.html#common-sequence-operations>) API.

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
>>> Table([r[:Col.AGE] for r in t[:1]], columns=t.columns[:Col.AGE])
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

<https://docs.python.org/3/library/stdtypes.html#immutable-sequence-types>

### Mutable Table operations

Mutable Table operations extends the [mutable sequence types](<https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types>) API.

#### Set item
<details>
<summary>show/hide sequence api</summary>

###### Sequence
~~~python
>>> mt = MTable(list(t), columns=t.columns)

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
>>> mt = MTable(list(t), columns=t.columns)

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

>>> mt[:, 'animal':] = Table([('rabbit', 3), ('spider', 1)])
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
>>> mt = MTable(list(t), columns=t.columns)

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
>>> mt = MTable(list(t), columns=t.columns)



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
>>> mt = MTable(list(t), columns=t.columns)

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
>>> mt = MTable(list(t), columns=t.columns)



>>> mt[:, 'age':'age'] = Table([('big',), ('small',)], columns=('size',))
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
>>> mt = MTable(list(t), columns=t.columns)

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
>>> mt = MTable(list(t), columns=t.columns)

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
