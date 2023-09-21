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

>>> t.index(('Ivica', 'M', 10))
0

>>> t.index('F')
(1, 'sex')

>>> t.index(1)
Traceback (most recent call last):
  ...
ValueError: 1 not found

>>> t.count(('Ivica', 'M', 10))
1

>>> t.count('M')
1

>>> t == t
True

>>> t > Table([('Ivica', 'M', 13)])
False

>>> print(t + Table([('Jura', 'M', 100)], columns=('name', 'sex', 'age')))
name    sex  age 
------- ---- ----
Ivica   M      10
Marica  F       8
Jura    M     100

>>> print(t * 2)
name    sex  age 
------- ---- ----
Ivica   M      10
Marica  F       8
Ivica   M      10
Marica  F       8

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

>>> print(t[:1, :'age'])
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
