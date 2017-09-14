# chunking
tools for chunking iterables

## Installation

```
python -m pip install chunking
```

## chunking.chunk

```py
>>> from chunking import chunk
>>> r = range(5)
>>> for c in chunk(r, 2):
...     print(c)
...
(0, 1)
(2, 3)
(4,)
```

## chunking.split

```py
>>> from chunking import split
>>> a_list = ["foo", 'bar', 'SEP', 'bacon', 'eggs']
>>> split(a_list, 'SEP')
[['foo', 'bar'], ['bacon', 'eggs']]
```

## chunking.iter_split

Like split, but a generator.

```py
>>> from chunking import iter_split
>>> a_list = ["foo", 'bar', 'SEP', 'bacon', 'eggs']
>>> for c in iter_split(a_list,'SEP'):
...     print(c)
...
['foo', 'bar']
['bacon', 'eggs']
```