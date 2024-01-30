import typer

from grepenv.cli import (
    print_environment,
    print_matching_keys,
    show_examples,
    try_compile_regex_pattern,
)

from .grepenv import filter_env_by_regular_expression, parse_environment


app = typer.Typer(add_completion=False, no_args_is_help=True)

_HELP_STRING = """
greps the env

\b
By default, all keys and values are searched for matches.
See options to specify only keys, or only values.

\b
Pattern matching is done using regex SEARCH. Use anchor characters if 
matching the whole key or value is necessary.
"""

_EPILOG_STRING = """
Call grepenv with the --example flag to see some example usage.
"""


@app.command(help=_HELP_STRING, epilog=_EPILOG_STRING, no_args_is_help=True)
def _(
    pattern: str = typer.Argument(
        ".*", help="Regular expression pattern to search with."
    ),
    respect_case: bool = typer.Option(
        False,
        "-c",
        "--respect-case",
        help="Respect case of pattern characters. By default, the given regular expression will be set to ignore the case of alphabetic characters.",
    ),
    keys_only: bool = typer.Option(False, "-k", "--keys", help="Only search keys."),
    values_only: bool = typer.Option(
        False, "-v", "--values", help="Only search values."
    ),
    find_key: bool = typer.Option(
        False,
        "-fk",
        "--find-key",
        help="Modified behavior of grepenv. Will grep for all keys that match the given pattern, and return their corresponding value with no formatting, one per line.",
    ),
    no_highlight: bool = typer.Option(
        False, "-nh", "--no-highlight", help="Disable match highlighting."
    ),
    example: bool = typer.Option(False, "--example", help="Print some example usage."),
):
    # Exit on example
    if example:
        return show_examples()

    pat = try_compile_regex_pattern(pattern, ignore_case=not respect_case)

    # Handle find key branch
    if find_key:
        return print_matching_keys(parse_environment(), pat)

    # Regular highlight and print functionality
    env = filter_env_by_regular_expression(
        pat, keys_only=keys_only, values_only=values_only
    )

    print_environment(
        env,
        pat,
        keys_only=keys_only,
        values_only=values_only,
        highlight=not no_highlight,
    )


def main():
    app()


if __name__ == "__main__":
    main()
