# pyTable

[table]: <https://en.wikipedia.org/wiki/Table_(information)>
[sequence]: <https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence>

[Table][table] is a [sequence] of objects organized in rows and columns.
Rows are integer indexed and columns are named.

Table is a subclass of Sequence as a sequence-of-rows.

## Table initialization

~~~python
>>> from pytable import Table as T, MutableTable as mT

>>> t = T([
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
~~~python
>>> ('marry', 'cat', 10) in t       # row in table
True

>>> 'dog' in t                      # item in table
True

>>> ('ozzy', 'cat', 18) not in t    # row not in table
True

>>> 'bird' not in t                 # item not in table
True

~~~

#### Get item
~~~python
>>> t[0]                            # row indexing
('ozzy', 'dog', 18)

>>> t[1, 'animal']                  # item indexing
'cat'

>>> t[:1]                           # row slicing
Table([('ozzy', 'dog', 18)], columns=('name', 'animal', 'age'))

>>> #t[0, :'age']                    # column slicing
Table([('ozzy', 'dog')], columns=('name', 'animal'))

~~~

#### Index and count
~~~python
>>> t.index(('marry', 'cat', 10))   # row index
1

>>> t.index(18)                     # item index
(0, 'age')

>>> t.count(('ozzy', 'dog', 18))    # row count
1

>>> t.count('cat')                  # item count
1

~~~

<https://docs.python.org/3/library/stdtypes.html#immutable-sequence-types>

### Mutable Table operations

Mutable Table operations extends the [mutable sequence types](<https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types>) API.

~~~python
>>> t = mT(list(t), columns=t.columns)

~~~

#### Set item
~~~python
>>> t[0] = ('harry', 'mouse', 2)    # row update
>>> print(t)
name   animal  age 
------ ------- ----
harry  mouse      2
marry  cat       10

>>> t[0, 'animal'] = 'python'       # item update
>>> print(t)
name   animal  age 
------ ------- ----
harry  python     2
marry  cat       10

>>>                                 # slice update
>>> t[:, 'animal':] = T([('rabbit', 3), ('spider', 1)])
>>> print(t)
name   animal  age 
------ ------- ----
harry  rabbit     3
marry  spider     1

~~~

##### Append column
~~~python
>>> t[:, 'food'] = ('carrot', 'fly')
>>> print(t)
name   animal  age  food   
------ ------- ---- -------
harry  rabbit     3 carrot 
marry  spider     1 fly    

~~~

##### Insert column(s)
~~~python
>>> t[:, 'age':'age'] = T([('big',), ('small',)], columns=('size',))
>>> print(t)
name   animal  size   age  food   
------ ------- ------ ---- -------
harry  rabbit  big       3 carrot 
marry  spider  small     1 fly    

~~~

#### Delete item
~~~python
>>> del t[1]                        # row deleting
>>> print(t)
name   animal  size  age  food   
------ ------- ----- ---- -------
harry  rabbit  big      3 carrot 

>>> del t[:, 'age']                 # column deleting
>>> print(t)
name   animal  size  food   
------ ------- ----- -------
harry  rabbit  big   carrot 

~~~
