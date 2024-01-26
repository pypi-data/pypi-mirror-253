from typing import Iterable, TypeVar
from functools import cmp_to_key
import ramda as R
from .edits import Skip, Insert, Inserted, Edit

@cmp_to_key
def key(x: Edit, y: Edit) -> Edit:
    if x.idx != y.idx:
        return x.idx - y.idx
    elif x.type != y.type:
        return -1 if x.type == 'insert' else 1 # inserts first
    else:
        return 0

V =  TypeVar("V")    
def decompress(edits: list[Skip|Insert[V]], start: int = 0, end: int = None) -> Iterable[int|Inserted[V]]:
    """Applies `edits` to `[start, end)`, returning a full iterable of indices
    - e.g. `decompress([insert(4), skip(6)], start=3, end=8) == xs `
        - `list(xs) == [3, None, 4, 5, 7] # inserted before 4, skipped 6`
    - If `end is None`, applies until last edit
    """
    i = start
    edits = sorted(edits, key=key)
    for edit in filter(lambda e: start <= e.idx < (end or float('inf')), edits):
        yield from range(i, edit.idx)
        if edit.type == "skip":
            i = edit.idx+1
        elif edit.type == "insert":
            yield Inserted(edit.value)
            i = edit.idx
    if end is not None:
        yield from range(i, end)

A = TypeVar('A')
def apply(edits: list[Skip|Insert[V]], xs: list[A], start: int = 0) -> Iterable[A | V]:
    """Applies `edits` to an actual list `xs[start:]`"""
    for i in decompress(edits, start=start, end=len(xs)):
        yield i.value if isinstance(i, Inserted) else xs[i]