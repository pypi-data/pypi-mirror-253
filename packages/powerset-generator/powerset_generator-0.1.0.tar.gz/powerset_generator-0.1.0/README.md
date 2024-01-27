# Python Power set generator

[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v0.json)](https://github.com/charliermarsh/ruff)

```python
import powerset_generator

for e in powerset_generator.subsets(["one", "two", "three", "three"]):
    print(e)
```

produces

```txt
set()
{'one'}
{'three'}
{'two'}
{'one', 'three'}
{'one', 'two'}
{'three', 'two'}
{'one', 'three', 'two'}
```

Note that the empty set, `set()` is included in the output
and that the function treats the duplicated input element `"three"` as if it appeared only once.
This is correct behavior the mathematical notion of power set.

See the more complete (perhaps excessively so) [documentation](https://jpgoldberg.github.io/powerset-generator/) for more details.

## Credit

The code for the `subsets()` function is derived heavily from
[Allen Downey](https://stackoverflow.com/users/661626/allen-downey)'s
[Stack Overflow answer](https://stackoverflow.com/a/53726866/1304076).
