# chunker
tools for chunking iterables


## chunker.split

```py
>>> a_list = ["foo", 'bar', 'SENTINEL', 'bacon', 'eggs']
>>> split(a_list, 'SENTINEL')
[['foo', 'bar'], ['bacon', 'eggs']]
```

## chunker.chunk

```py
>>> r = range(5)
>>> for c in chunk(r, 2):
...     print(a, b)
(0, 1)
(2, 3)
(4,)
```
