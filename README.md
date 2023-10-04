# pyTable

[table]: <https://en.wikipedia.org/wiki/Table_(information)>
[sequence]: <https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence>

[Table][table] is a [sequence] of objects organized in rows and columns.
Rows are integer indexed and columns are named.

Table is a subclass of Sequence as a sequence-of-rows.

## Table

~~~python
>>> # import
>>> from pytable import Table as T, MutableTable as mT

>>> # initialization
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
~~~python
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

>>> # rectange
>>> t[:1, :'age']
Table([('ozzy', 'dog')], columns=('name', 'animal'))

~~~

#### Index and count
~~~python
>>> # row index
>>> t.index(('marry', 'cat', 10))   
1

>>> # item index
>>> t.index(18)                     
(0, 'age')

>>> t[t.index(18)]
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

~~~python
>>> t = mT(list(t), columns=t.columns)

~~~

#### Set item
~~~python
>>> # row update
>>> t[0] = ('harry', 'mouse', 2)    
>>> print(t)
name   animal  age 
------ ------- ----
harry  mouse      2
marry  cat       10

>>> # item update
>>> t[0, 'animal'] = 'python'       
>>> print(t)
name   animal  age 
------ ------- ----
harry  python     2
marry  cat       10

>>> # slice update
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
>>> # row deleting
>>> del t[1]                        
>>> print(t)
name   animal  size  age  food   
------ ------- ----- ---- -------
harry  rabbit  big      3 carrot 

>>> # column deleting
>>> del t[:, 'age']                 
>>> print(t)
name   animal  size  food   
------ ------- ----- -------
harry  rabbit  big   carrot 

~~~
