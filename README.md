# pyTable

## Basics

~~~pycon
>>> from pytable import Table

>>> t = Table([('Ivica', 'M', 10), ('Marica', 'F', 8)], columns=('name', 'sex', 'age'))
>>> print(t)
name    sex  age 
------- ---- ----
Ivica   M      10
Marica  F       8

>>> t
Table([('Ivica', 'M', 10), ('Marica', 'F', 8)], columns=('name', 'sex', 'age'))

>>> t.columns
('name', 'sex', 'age')

>>> len(t)
2

>>> t[0]
('Ivica', 'M', 10)

>>> #t[0]
Row(name='Ivica', sex='M', age=10)

>>> t[:, 'name']
('Ivica', 'Marica')

>>> t[1, 'age']
8

>>> ('Marica', 'F', 8) in t
True

>>> 'Ivica' in t
True

>>> for r in t:
...     print(r)
('Ivica', 'M', 10)
('Marica', 'F', 8)

>>> for r in reversed(t):
...     print(r)
('Marica', 'F', 8)
('Ivica', 'M', 10)

>>> # t.index()

>>> # t.count()

~~~


## Slicing

~~~pycon
>>> print(t[:2])
name    sex  age 
------- ---- ----
Ivica   M      10
Marica  F       8

>>> print(t[:1])
name   sex  age 
------ ---- ----
Ivica  M      10

>>> print(t[:1, 'name': 'age'])
name   sex 
------ ----
Ivica  M   

~~~


## Table mutation

+ >>> t[...] = Table()
+ >>> del t[...]
+ >>> t.insert()
+ >>> t.append()
+ >>> t.reverse()
+ >>> t.extend()
+ >>> t.pop()
+ >>> t.remove()
+ >>> t += Table()
