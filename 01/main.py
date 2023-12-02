def first(text: list[str]) -> int:
    calibs: list[int] = []

    for line in text:
        calib: str = ""

        for c in line:
            if c.isnumeric():
                calib += c

        if calib != "":
            calib = calib[0] + calib[-1]
            calibs.append(int(calib))

    return sum(calibs)


digits: dict[str, int] = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def second(text: list[str]) -> int:
    calibs: list[int] = []

    for line in text:
        calib: list[tuple[int, str]] = []  # (index, digit)

        for k, v in digits.items():
            idx = line.find(k)
            ridx = line.rfind(k)

            calib.append((idx, str(v)))
            calib.append((ridx, str(v)))

        for idx, c in enumerate(line):
            if c.isnumeric():
                calib.append((idx, c))

        calib.sort(key=lambda tup: tup[0])

        calibs.append(int(calib[0][1] + calib[-1][1]))

    return sum(calibs)


def main() -> int:
    with open("input.txt", "r") as content:
        text = content.readlines()
        print(f"First Puzzle:\t{first(text)}")
        print(f"Second Puzzle:\t{second(text)}")
    return 0


if __name__ == "__main__":
    raise (SystemExit(main()))
