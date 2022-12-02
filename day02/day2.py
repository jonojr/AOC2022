#
# A - Rock - X
# B - Paper - Y
# C - Scissors - Z

WIN = 6
DRAW = 3
LOOSE = 0

ROCK = 1
PAPER = 2
SCISSORS = 3

PART_1_MAPPING = {
    "A X": ROCK + DRAW,  # Rock vs Rock
    "A Y": PAPER + WIN,  # Rock vs Paper
    "A Z": SCISSORS + LOOSE,  # Rock vs Scissors

    "B X": ROCK + LOOSE,  # Paper vs Rock
    "B Y": PAPER + DRAW,  # Paper vs Paper
    "B Z": SCISSORS + WIN,  # Paper vs Scissors

    "C X": ROCK + WIN,  # Scissors vs Rock
    "C Y": PAPER + LOOSE,  # Scissors vs Paper
    "C Z": SCISSORS + DRAW,  # Scissors vs Scissors
}

# X - Loose
# Y - Draw
# Z - Win
PART_2_MAPPING = {
    # They pick ROCK
    "A X": SCISSORS + LOOSE,  # ROCK + LOOSE = SCISSORS
    "A Y": ROCK + DRAW,  # ROCK + DRAW = ROCK
    "A Z": PAPER + WIN,  # ROCK + WIN = PAPER

    # They choose PAPER
    "B X": ROCK + LOOSE,  # PAPER + LOOSE = ROCK
    "B Y": PAPER + DRAW,  # PAPER + DRAW = PAPER
    "B Z": SCISSORS + WIN,  # PAPER + WIN = SCISSORS

    # They choose SCISSORS
    "C X": PAPER + LOOSE,  # SCISSORS + LOOSE = PAPER
    "C Y": SCISSORS + DRAW,  # SCISSORS + DRAW = SCISSORS
    "C Z": ROCK + WIN,  # SCISSORS + WIN = ROCK
}


if __name__ == "__main__":
    elves = []
    with open("input.txt", "r") as input_file:
        games = input_file.read().split('\n')

    part_2_results = [PART_2_MAPPING[game] for game in games]

    print(f"Part 1: {sum([PART_1_MAPPING[game] for game in games])}")
    print(f"Part 2: {sum(part_2_results)}")
