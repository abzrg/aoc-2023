import re
import sys


def first(cards: list[str]) -> int:
    pat = re.compile(r"^Card\s*\d+:((?:\s+\d+)+)\s\|((?:\s+\d+)+)$")

    points: list[int] = []

    for card in cards:
        for m in re.finditer(pat, card):
            winnums = set(map(int, m.group(1).split()))
            mynums = set(map(int, m.group(2).split()))

            win_count: int = len(winnums & mynums)

            if win_count != 0:
                points.append(2 ** (win_count - 1))

    return sum(points)


def second(cards: list[str]) -> int:
    """
    - Loop over each card
    - compute the number of winning numbers (wincount)
    - for `wincount` card after the current card:
        - curcopies = get the number of current copies of those cards
        - for `curcopies` times add 1 to number of copies of the card
    - compute the sum of the list of number of copies
    """
    pat = re.compile(r"^Card\s*\d+:((?:\s+\d+)+)\s\|((?:\s+\d+)+)$")

    num_copies = [1] * len(cards)

    for i, card in enumerate(cards):
        for m in re.finditer(pat, card):
            winnums = set(map(int, m.group(1).split()))
            mynums = set(map(int, m.group(2).split()))

            wincount: int = len(winnums & mynums)

            for j in range(i + 1, i + wincount + 1):
                try:
                    num_copies[j] += num_copies[i]
                except IndexError:
                    continue

    return sum(num_copies)


def main() -> int:
    argv: list[str] = sys.argv
    if len(argv) < 2:
        print("Usage: python main.py <input/test.txt>", file=sys.stderr)
        return 1

    with open(argv[1], "r") as f:
        cards = list(map(str.strip, f.readlines()))
        print(f"First Puzzle:\t{first(cards)}")
        print(f"Second Puzzle:\t{second(cards)}")

    return 0


if __name__ == "__main__":
    raise (SystemExit(main()))
