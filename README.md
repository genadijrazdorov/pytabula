# pyTable

## Basics

~~~python
>>> from pytable import Table

>>> t = Table(name=['Ivica', 'Marica'], sex=['M', 'F'], age=[10, 8])
>>> t
<Table

name    sex  age
------- ---- ----
Ivica   M    10
Marica  F    8

>

>>> t.columns
['name', 'sex', 'age']


>>> len(t)
2

>>> t[0]
Row(name='Ivica', sex='M', age=10)

>>> t[..., 'name']
['Ivica', 'Marica']

>>> t[1, 'age']
8

>>> 'Ivica' in t
True

>>> ('Marica', 'F', 8) in t
True

>>> for l in t:
...     pass

>>> reversed(t)
<Table

name    sex  age
------- ---- ----
Marica  F    8
Ivica   M    10

>

>>> t.index()

>>> t.count()


>>> t[...] = Table()
>>> del t[...]
>>> t.insert()
>>> t.append()
>>> t.reverse()
>>> t.extend()
>>> t.pop()
>>> t.remove()
>>> t += Table()
~~~

## Slicing

~~~python
>>> t[:2]
<Table

name    sex  age
------- ---- ----
Ivica   M    10
Marica  F    8

>

>>> t[:1]
<Table

name    sex  age
------- ---- ----
Ivica   M    10

>

>>> t[:1, 'name': 'age']
<Table

name    sex 
------- ----
Ivica   M   

>
~~~
