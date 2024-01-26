"""Helper functionality for the cli.

These functions may call sys.exit(), and so should only be called form the
cli itself.
"""
import re
import sys

from typing import NoReturn, Union, List

from rich.console import Console
from rich.live import Live
from rich.syntax import Syntax
from rich.panel import Panel

from grepenv.grepenv import EnvItem


_CONSOLE = Console()


def try_compile_regex_pattern(
    pattern: str, ignore_case: bool = True
) -> Union[re.Pattern, NoReturn]:
    """Attempt to compile the given regex `pattern`.

    If an exception is thrown during compilation, an error will be printed,
    and the program will exit.
    """
    try:
        return re.compile(pattern, re.IGNORECASE if ignore_case else 0)
    except Exception as e:
        print_error(f"Couldn't compile regular expression ({e})")
        sys.exit(1)


def highlight_string(var: str, pat: re.Pattern) -> str:
    """Scan the given string variable, and return a modified version in which
    all ranges matched by `pat` surrounded in `rich` highlighting tags.
    """
    if not pat.search(var):
        return var

    for m in reversed(list(pat.finditer(var))):
        start = m.start()
        end = m.end()

        s0 = var[:start]
        s1 = var[start:end]
        s2 = var[end:]

        var = f"{s0}[red]{s1}[/]{s2}"

    return var


def print_environment(
    env: List[EnvItem],
    pat: re.Pattern,
    keys_only: bool = False,
    values_only: bool = False,
    highlight: bool = True,
):
    """Prints all environment items with styling according to the given options."""
    for x in env:
        # Format key
        if values_only:
            key_s = f"[dim]{x.key}[/]"
        elif highlight:
            key_s = highlight_string(x.key, pat)
        else:
            key_s = x.key

        # Format value
        if keys_only:
            value_s = f"[dim]{x.value}[/]"
        elif highlight:
            value_s = highlight_string(x.value, pat)
        else:
            value_s = x.value

        # concat
        _CONSOLE.print(f"{key_s}={value_s}", highlight=False)


def print_matching_keys(env: List[EnvItem], pat: re.Pattern):
    for x in env:
        if pat.search(x.key):
            print(x.value)


def print_error(m: str):
    """Print a formatted error message `m`."""
    _CONSOLE.print(f"[bold error]ERROR: [/]{m}")


def show_examples():
    examples = [
        (
            "Find all environment keys and variables containing the letters 'xdg'",
            """
            $ grepenv xdg
            XDG_CONFIG_DIRS=/etc/xdg/xdg-cinnamon:/etc/xdg
            XDG_CURRENT_DESKTOP=X-Cinnamo
            XDG_RUNTIME_DIR=/run/user/1000
            XDG_SEAT=seat0
            ...
            """,
        ),
        (
            "Find all environment keys and variables containing the letters 'xdg' (strict lowercase)",
            """
            $ grepenv xdg -c
            XDG_CONFIG_DIRS=/etc/xdg/xdg-cinnamon:/etc/xdg
            """,
        ),
        (
            "Find all keys containing the letters 'git'",
            """
            $ grepenv git -k
            GITHUB_API_TOKEN=abc_NlNhalNDL78NAhdKhNAk78bdf7f
            """,
        ),
        (
            "Extract all values from keys which contain the letters 'git'",
            """
            $ grepenv git -fk
            abc_NlNhalNDL78NAhdKhNAk78bdf7f
            """,
        ),
        (
            "Get all environment that looks like an api key",
            """
            $ grepenv "_api_(key|token)_" -k
            GITHUB_API_TOKEN=abc_NlNhalNDL78NAhdKhNAk78bdf7f
            OPENAI_API_KEY=123_abcdefghijklmnop
            """,
        ),
    ]

    for title, body in examples:
        _CONSOLE.print(Panel(Syntax(body, "bash"), title=title, title_align="left"))
