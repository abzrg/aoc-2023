import re
import sys


def isspecial(c: str) -> bool:
    assert len(c) == 1
    assert c != "\n"

    if c == "." or c.isnumeric():
        return False
    return True


def first(schem: list[str]) -> int:
    num_pattern = re.compile(r"(\d+)")

    parts: list[int] = []

    for i, line in enumerate(schem):
        for m in re.finditer(num_pattern, line):
            if m is None:
                continue

            is_part = False

            m_start = m.start()
            m_end = m.end()

            for j in range(m_start - 1, m_end + 1):
                found_special = False

                if j < 1 or j >= len(schem[0]) - 1:  # A BIG BUG DIED HERE
                    continue
                if i == 0:
                    found_special = isspecial(schem[i][j]) or isspecial(schem[i + 1][j])
                elif i == len(schem) - 1:
                    found_special = isspecial(schem[i - 1][j]) or isspecial(schem[i][j])
                else:
                    found_special = (
                        isspecial(schem[i - 1][j])
                        or isspecial(schem[i][j])
                        or isspecial(schem[i + 1][j])
                    )

                if found_special:
                    is_part = True
                    break

            number = int(m.group(1))
            if is_part:
                parts.append(number)

    return sum(parts)


def second(schem: list[str]) -> int:
    """
    - find the stars in each line
    - for each star find all the numbers in the prev, curr, and next line
    - for each of those lines if a number is in proximity of the star store it
    - if the number of numbers around star is two then we have a gear
    """
    star_pat = re.compile(r"(\*)")
    num_pat = re.compile(r"(\d+)")

    gear_ratios = []

    for i, line in enumerate(schem):
        for m_star in re.finditer(star_pat, line):
            if m_star is None:
                break

            gears = []

            m_star_start = m_star.start()

            for j in (i - 1, i, i + 1):
                if j < 0 or j > len(schem):
                    continue

                for m_number in re.finditer(num_pat, schem[j]):
                    if m_number is None:
                        break

                    if (
                        m_star_start - 1 <= (m_number.end() - 1) <= m_star_start + 1
                        or m_star_start - 1 <= m_number.start() <= m_star_start + 1
                    ):
                        gears.append(int(m_number.group()))

            if len(gears) == 2:
                gear_ratio = gears[0] * gears[1]
                gear_ratios.append(gear_ratio)

    return sum(gear_ratios)


def main() -> int:
    argv: list[str] = sys.argv
    if len(argv) < 2:
        print("Usage: python main.py <input/test.txt>", file=sys.stderr)
        return 1

    with open(argv[1], "r") as f:
        schem = list(map(str.strip, f.readlines()))
        print(f"First Puzzle:\t{first(schem)}")
        print(f"Second Puzzle:\t{second(schem)}")

    return 0


if __name__ == "__main__":
    raise (SystemExit(main()))
