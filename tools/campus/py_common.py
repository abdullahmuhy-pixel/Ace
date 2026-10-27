"""Helper for the Programming with Python course: run a snippet and capture what it prints, so every
"what is printed?" answer in the course is checked by actually running the code."""
import io
import contextlib


def out(code):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        exec(code, {})
    return buf.getvalue().strip()


def check(code, expected):
    got = out(code)
    assert got == str(expected), (code, got, expected)
    return expected
