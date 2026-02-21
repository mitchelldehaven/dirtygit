# dirtygit

Assert your git repo is clean and get the current commit hash. Useful for ensuring experiment reproducibility.

## Install

```
pip install dirtygit
```

## Usage

```python
import dirtygit

commit = dirtygit.check()  # returns commit hash if clean, asserts if dirty
```
