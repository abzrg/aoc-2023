import re
import sys


def first(content: list[str]) -> int:
    limits = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    possible_games: list[int] = []

    cube_pattern = re.compile(r"(\d\d?) (red|green|blue)")

    for i, game in enumerate(content):
        game_index = i + 1
        game_possible = True

        for m in re.finditer(cube_pattern, game):
            if m is None:
                raise ValueError("Invalid Game: cube pattern not found.")

            cube_count = int(m.group(1))
            cube_color = m.group(2)

            if cube_count > limits[cube_color]:
                game_possible = False

        if game_possible:
            possible_games.append(game_index)

    return sum(possible_games)


def second(content: list[str]) -> int:
    powers: list[int] = []

    cube_pattern = re.compile(r"(\d\d?) (red|green|blue)")

    for game in content:
        maximums: dict[str, int] = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        for m in re.finditer(cube_pattern, game):
            if m is None:
                raise ValueError("Invalid Game: cube pattern not found.")

            cube_count = int(m.group(1))
            cube_color = m.group(2)

            if cube_count > maximums[cube_color]:
                maximums[cube_color] = cube_count

        power = 1
        for key in maximums.keys():
            power *= maximums[key]
        powers.append(power)

    return sum(powers)


def main() -> int:
    argv: list[str] = sys.argv
    if len(argv) < 2:
        print("Usage: python main.py <input/test.txt>", file=sys.stderr)
        return 1

    with open(argv[1], "r") as f:
        content = f.readlines()
        print(f"First Puzzle:\t{first(content)}")
        print(f"Second Puzzle:\t{second(content)}")

    return 0


if __name__ == "__main__":
    raise (SystemExit(main()))
