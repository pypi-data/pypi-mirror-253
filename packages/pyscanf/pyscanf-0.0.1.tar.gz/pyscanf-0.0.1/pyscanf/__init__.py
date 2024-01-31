# Copyright (c) 2024 kemplerart

__all__ = ["scanf"]


def scanf(match: str, limit: int = 256) -> list[
    int | bool | float | complex | str
] | int | bool | float | complex | str:
    """
    Read formatted input from stdin in C style.

    Input is read character by character until match query is exhausted.
    Supported format specifiers are (note that some are different from
    standard Python format specifiers):
        %d (int),
        %r (bool),
        %f (float),
        %x (complex).
        %s (string/char),

    Raises ValueError when format specifier and read value did not match.
    Raises TypeError when match query did not have any valid format specifiers.

    The number of characters read by each format specifier is limited.
    Default is 256.
    """

    def is_bool(c: str) -> bool:
        return c.lower() != "false" and c != "0"

    from sys import stdin
    fmt_specs = match.strip().split()
    vals = []

    for fmt_spec in fmt_specs:
        if fmt_spec[0] != '%':
            raise TypeError("Invalid format specifier %s" % fmt_spec)

        cs = []
        tries = 0
        while tries < limit:
            c = stdin.read(1)

            if c.strip():
                cs.append(c)
                tries += 1
                continue

            elif len(cs) == 0:
                continue

            s = ''.join(cs)

            parse_funcs = {
                "%d": int,
                "%r": is_bool,
                "%f": float,
                "%x": complex,
                "%s": str,
            }

            parse_func = parse_funcs.get(fmt_spec, None)
            if parse_func is None:
                raise TypeError("Unknown format specifier %s" % fmt_spec)

            try:
                vals.append(parse_func(s))
                break
            except ValueError:
                raise ValueError(
                    "Invalid format specifier %s for %s" % (fmt_spec, s))

    if len(vals) == 0:
        raise TypeError("No valid format specifiers in match query")
    elif len(vals) == 1:
        return vals[0]
    return vals


if __name__ == '__main__':
    """
    # Input example:

    5 4
    1001 12 girl 2.6
    1002 23 boy 2.2
    1003 23 girl 2.2
    1004 45 boy 10.3
    1005 3 girl 12.0
    """

    """
    # Old way:

    n, m = map(int, input().split())
    matrix = []

    for i in range(n):
        m = input().split()
        matrix.append([int(m[0]), int(m[1]), m[2], float(m[3])])

    for i in range(n):
        print(matrix[i])
    """

    # New way:

    n = scanf("%d")
    m = scanf("%d")
    matrix = []

    assert type(n) is int

    for i in range(n):
        matrix.append(scanf("%d %d %s %f"))

    for i in range(n):
        print(matrix[i])

    for x in matrix:
        assert type(x[0]) is int and type(x[1]) is int and type(
            x[2]) is str and type(x[3]) is float
