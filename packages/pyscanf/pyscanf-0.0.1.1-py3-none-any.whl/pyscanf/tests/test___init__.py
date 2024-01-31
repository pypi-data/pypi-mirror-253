# Copyright (c) 2024 kemplerart

import pytest
from pyscanf import scanf


class _stdin():
    def __init__(self, inner: str) -> None:
        self.__inner = inner
        self.__read_from = -1
        return None

    def read(self, n: int = -1) -> str:
        if n < 1:
            return ""

        if self.__read_from >= len(self.__inner):
            raise IndexError("Inner of _stdin exhausted")

        self.__read_from += 1
        return self.__inner[self.__read_from:self.__read_from + n]


def _recursive_assert_results(results, cases):
    for i in range(len(results)):
        result = results[i]
        case = cases[i]

        if not hasattr(result, '__len__') or type(result) is str:
            assert result == case and type(result) is type(case)
            continue

        _recursive_assert_results(result, case)


def test_scanf_single_int(monkeypatch: pytest.MonkeyPatch,
                          capsys: pytest.CaptureFixture) -> None:
    test_case = """
    5
    """

    case = 5

    monkeypatch.setattr('sys.stdin', _stdin(test_case.strip()))

    result = scanf("%d")
    assert result == case and type(result) is type(case)

    return None


def test_scanf_single_str(monkeypatch: pytest.MonkeyPatch,
                          capsys: pytest.CaptureFixture) -> None:
    test_case = """
    foo
    """

    case = "foo"

    monkeypatch.setattr('sys.stdin', _stdin(test_case.strip()))

    result = scanf("%s")
    assert result == case and type(result) is type(case)

    return None


def test_scanf_single_float(monkeypatch: pytest.MonkeyPatch,
                            capsys: pytest.CaptureFixture) -> None:
    test_case = """
    2.654
    """

    case = 2.654

    monkeypatch.setattr('sys.stdin', _stdin(test_case.strip()))

    result = scanf("%f")
    assert result == case and type(result) is type(case)

    return None


def test_scanf_single_complex(monkeypatch: pytest.MonkeyPatch,
                              capsys: pytest.CaptureFixture) -> None:
    test_case = """
    5+3j
    """

    case = 5 + 3j

    monkeypatch.setattr('sys.stdin', _stdin(test_case.strip()))

    result = scanf("%x")
    assert result == case and type(result) is type(case)

    return None


def test_scanf_single_bool1(monkeypatch: pytest.MonkeyPatch,
                            capsys: pytest.CaptureFixture) -> None:
    test_case = """
    False
    """

    case = False

    monkeypatch.setattr('sys.stdin', _stdin(test_case.strip()))

    result = scanf("%r")
    assert result == case and type(result) is type(case)

    return None


def test_scanf_single_bool2(monkeypatch: pytest.MonkeyPatch,
                            capsys: pytest.CaptureFixture) -> None:
    test_case = """
    True
    """

    case = True

    monkeypatch.setattr('sys.stdin', _stdin(test_case.strip()))

    result = scanf("%r")
    assert result == case and type(result) is type(case)

    return None


def test_scanf_suite_bools(monkeypatch: pytest.MonkeyPatch,
                           capsys: pytest.CaptureFixture) -> None:
    test_case = """
    True 0 fox
    """

    cases = [
        True, False, True
    ]

    monkeypatch.setattr('sys.stdin', _stdin(test_case.strip()))

    results = [
        scanf("%r"),
        scanf("%r"),
        scanf("%r"),
    ]

    _recursive_assert_results(results, cases)
    return None


def test_scanf_suite_complex(monkeypatch: pytest.MonkeyPatch,
                             capsys: pytest.CaptureFixture) -> None:
    test_case = """
    False
    True
    4 5
    1001 12 girl 2.6
    1002 23 boy 2.2
    1003 23 girl 2.2
    1004 45 boy 10.3
    1005 3 girl 12.0
    """

    cases = [
        False,
        True,
        (4, 5),
        [[1001, 12, "girl", 2.6],
         [1002, 23, "boy", 2.2],
         [1003, 23, "girl", 2.2],
         [1004, 45, "boy", 10.3],
         [1005, 3, "girl", 12.0]]
    ]

    monkeypatch.setattr('sys.stdin', _stdin(test_case.strip()))

    results = [
        scanf("%r"),
        scanf("%r"),
        scanf("%d %d"),
        [scanf("%d %d %s %f") for _ in range(5)],
    ]

    _recursive_assert_results(results, cases)
    return None


def test_scanf_suite_by_char(monkeypatch: pytest.MonkeyPatch,
                             capsys: pytest.CaptureFixture) -> None:
    test_case = """
    1003 True foo bar 1234.1234
    """

    cases = [
        1003, True, "foo", ("bar", 1234.1234)
    ]

    monkeypatch.setattr('sys.stdin', _stdin(test_case.strip()))

    results = [
        scanf("%d"),
        scanf("%r"),
        scanf("%s"),
        scanf("%s %f"),
    ]

    _recursive_assert_results(results, cases)
    return None


def test_scanf_suite_with_raises(monkeypatch: pytest.MonkeyPatch,
                                 capsys: pytest.CaptureFixture) -> None:
    test_case = """
    56+10j vl232 vl232 vl232 vl232 1j+1
    45.22 true
    """

    monkeypatch.setattr('sys.stdin', _stdin(test_case.strip()))

    case = 56 + 10j
    result = scanf("%x")
    assert result == case and type(result) is type(case)

    fmt_spec = "foo"
    match = "Invalid format specifier %s for %s" % (fmt_spec, "vl232")
    with pytest.raises(ValueError, match=match):
        scanf(fmt_spec)

    fmt_spec = "%a"
    match = "Invalid format specifier %s for %s" % (fmt_spec, "vl232")
    with pytest.raises(ValueError, match=match):
        scanf(fmt_spec)

    fmt_spec = ""
    match = "No valid format specifiers in match query"
    with pytest.raises(TypeError, match=match):
        scanf(fmt_spec)

    fmt_spec = "%d"
    match = "Invalid format specifier %s for %s" % (fmt_spec, "vl232")
    with pytest.raises(ValueError, match=match):
        scanf(fmt_spec)

    case = "vl232"
    result = scanf("%s")
    print(result)
    assert result == case and type(result) is type(case)

    fmt_spec = "%x"
    match = "Invalid format specifier %s for %s" % (fmt_spec, "1j+1")
    with pytest.raises(ValueError):  # no match, regex does not like %x
        scanf(fmt_spec)

    case = 45.22
    result = scanf("%f")
    assert result == case and type(result) is type(case)

    case = True
    result = scanf("%r")
    assert result == case and type(result) is type(case)

    return None
