import re
import sys


def first(content: list[str]) -> int:
    return len(content)


def second(content: list[str]) -> int:
    return len(content)


def main() -> int:
    argv: list[str] = sys.argv
    if len(argv) < 2:
        print("Usage: python main.py <input/test.txt>", file=sys.stderr)
        return 1

    with open(argv[1], "r") as f:
        content = list(map(str.strip, f.readlines()))
        print(f"First Puzzle:\t{first(content)}")
        print(f"Second Puzzle:\t{second(content)}")

    return 0


if __name__ == "__main__":
    raise (SystemExit(main()))
