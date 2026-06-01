from pathlib import Path


def test_list_python_functions(tmp_path: Path):
    from .make_function_indxed import list_python_functions

    file_a = tmp_path / "a.py"
    file_a.write_text(
        "\n".join([
            "def foo(x, y=1):",
            "    return x + y",
            "",
            "class Bar:",
            "    def baz(self, a, *, flag=False):",
            "        return a",
        ]),
        encoding="utf-8",
    )

    file_b = tmp_path / "b.py"
    file_b.write_text(
        "\n".join([
            "async def coro(p, /, q, *args, r=3, **kwargs):",
            "    return p",
        ]),
        encoding="utf-8",
    )

    result = list_python_functions(tmp_path)
    observed = [
        (item["file"], item["function"], item["arguments"], item["line"])
        for item in result
    ]

    assert observed == [
        ("a.py", "foo", "(x, y = 1)", 1),
        ("a.py", "Bar.baz", "(self, a, *, flag = False)", 5),
        ("b.py", "coro", "(p, /, q, *args, r = 3, **kwargs)", 1),
    ]
