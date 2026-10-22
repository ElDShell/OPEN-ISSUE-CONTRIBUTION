
import argparse
import sys
from typing import Optional, Sequence

from Training import __version__

def build_parse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Training CLI. A simple GitHub issue contribution powered tool.")
    parser.add_argument("--string-length", type=str, default=None, help="Returns the length of a string.")
    parser.add_argument("--version", action="version", version=f"Training {__version__}")
    return parser

def main(args: Optional[Sequence[str]] = None) -> None:
    parser = build_parse()
    parsed_args = parser.parse_args(args=args)
    if parsed_args.string_length is not None:
        print(f"The length of the string is: {len(str(parsed_args.string_length))}")
    else:
        # No flag given: a bare `python -m Training` should explain the tool,
        # not report the length of a default that was never passed.
        parser.print_help()

if __name__ == "__main__":
    sys.exit(main())
