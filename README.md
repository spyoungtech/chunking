# chunking
tools for chunking iterables

Requires Python 3.5+

[![Build Status](https://travis-ci.org/spyoungtech/chunking.svg?branch=master)](https://travis-ci.org/spyoungtech/chunking)

### Note: 

The main reason this package was created was to fill a small gap in [more-itertools](https://github.com/erikrose/more-itertools) for splitting an iterable ON a value (`chunking.split` / `chunking.iter_split`) -- That gap in more-itertools has since been filled with the [addition of `split_at`](https://github.com/erikrose/more-itertools/pull/178).

As such, you should probably just use [more-itertools](https://github.com/erikrose/more-itertools).

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
