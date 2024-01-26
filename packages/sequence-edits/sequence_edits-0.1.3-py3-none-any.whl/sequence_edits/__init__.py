"""
### Sequence edits
Tools for encoding/decoding sequence editions (insertions/deletions)
- `decompress: edits, [start, end) -> indices`
- `apply: edits, start, xs -> edited xs`
- `Edit`: skip or insert
"""
from .edits import Skip, Insert, Edit
from .main import decompress, apply