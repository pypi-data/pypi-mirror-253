# pyscanf

<p>
    <a href="https://github.com/KirilStrezikozin/pyscanf/releases"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
    <a href="https://github.com/KirilStrezikozin/pyscanf/releases"><img src="https://img.shields.io/github/release/KirilStrezikozin/pyscanf.svg" alt="Latest Release"></a>
    <a href="https://github.com/KirilStrezikozin/pyscanf/actions"><img src="https://github.com/KirilStrezikozin/pyscanf/workflows/python-publish/badge.svg" alt="Build Status"></a>
</p>

A Python package to read formatted input from the standard input in C style.

Jump to [installation](#installation) or [usage](#installation).

## Introduction

Straight up with an example. When you need to read any kind of input in Python, like the one below, how uncomfortable do you think it is? 

```python
# Input:
# 5 4
# 1001 12 girl 2.6
# 1002 23 boy 2.2
# 1003 23 girl 2.2
# 1004 45 boy 10.3
# 1005 3 girl 12.0

n, m = map(int, input().split())
matrix = []

for i in range(n):
    m = input().split()
    matrix.append([int(m[0]), int(m[1]), m[2], float(m[3])])

for i in range(n):
    print(matrix[i])

# Output:
# [1001, 12, 'girl', 2.6]
# [1002, 23, 'boy', 2.2]
# [1003, 23, 'girl', 2.2]
# [1004, 45, 'boy', 10.3]
# [1005, 3, 'girl', 12.0]

```

I do not mean that using `map` and `split`, and parsing is wrong or bad in any sense. The only thing I want to show you is that you can write this instead:

```python
n, m = scanf("%d %d")
matrix = []

for i in range(n):
    matrix.append(scanf("%d %d %s %f"))
```

Still not impressed? Here is what you also get:

```python
n = scanf("%d")
m = scanf("%d")
matrix = []

for i in range(n):
    matrix.append(scanf("%d %d %s %f"))
```

And both of these examples work for the initial input entered from keyboard while executing the code:

```
5 4
1001 12 girl 2.6
1002 23 boy 2.2
1003 23 girl 2.2
1004 45 boy 10.3
1005 3 girl 12.0
```

## Installation

To install and use the latest `pyscanf` in your python project, run:

```
$ pip install pyscanf
```


## Usage

### Import `pyscanf`

`pyscanf` has no dependencies and is basically just a single function. A simple import will get you running:

```python
from pyscanf import scanf
```

### Basic usage

The `scanf()` function is documented to give you usage instructions inside your editor. So, just call `scanf()` and provide it a `match` (string) query, which is essentially a string with format specifiers to parse the input:

```python
n = scanf("%d")
```

### Format specifiers

Input is read character by character until `match` query is exhausted. Supported format specifiers are (note that some are different from standard Python format specifiers):

- `%d` (int),
- `%r` (bool),
- `%f` (float),
- `%x` (complex number).
- `%s` (string/char),

Raises `ValueError` when format specifier and read value did not match.
Raises `TypeError` when match query did not have any valid format specifiers.

The number of characters read by each format specifier is limited by `limit`. Default is 256.

### Read character by character

What makes `pyscanf` a successor to the regular way of reading input in Python is its way to read character by character from stdin. Given an input:

```
32 11.50 foo
```

You can read it by either:

```python
a, b, s = scanf("%d %f %s")
```

Or in separate lines even though the input was typed in a single file. This is the core similarity with C's `scanf` function:

```python
a = scanf("%d")
b = scanf("%f")
s = scanf("%s")
```

Overall, `pyscanf` can make reading input in Python much more intuitive and straightforward. And requires less overhead with ensuring correct variable types.

```python
# Input:
# 5 4
# 1001 12 girl 2.6
# 1002 23 boy 2.2
# 1003 23 girl 2.2
# 1004 45 boy 10.3
# 1005 3 girl 12.0

n, m = scanf("%d %d")
matrix = []

for i in range(n):
    matrix.append(scanf("%d %d %s %f"))

for x in matrix:
    assert (type(x[0]) is int 
            and type(x[1]) is int
            and type(x[2]) is str
            and type(x[3]) is float)
    print(x)

# Output:
# [1001, 12, 'girl', 2.6]
# [1002, 23, 'boy', 2.2]
# [1003, 23, 'girl', 2.2]
# [1004, 45, 'boy', 10.3]
# [1005, 3, 'girl', 12.0]

```

## Future updates

So far, `pyscanf` meats its initial creation intentions. But this does not mean that improvements are not welcome. Here, we appreciate the opposite. Below is the list of possible additions to `pyscanf`, but you can always open a pull request with your own suggestions as long as they meet `pyscanf`'s guidelines (see below):

- [ ] Parse a given string or a file.
- [ ] Use regex to parse input. Similar to what `parse` can do.
- [ ] Your feature here.


## Contributing guidelines

`pyscanf` is a small Python package. Its main purpose is to serve a comfortable and easy way to read input in Python. Its main goal is to not necessarily be as feature-rich as possible, but to be ultra compact and applicable for reading input.
