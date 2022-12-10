def completely_overlap(pair) -> bool:
    a1_left, a1_right = pair[0]
    a2_left, a2_right = pair[1]

    assignment_1_contains_assignment_2 = a1_left >= a2_left and a1_right <= a2_right
    assignment_2_contains_assignment_1 = a2_left >= a1_left and a2_right <= a1_right

    return assignment_1_contains_assignment_2 or assignment_2_contains_assignment_1


def any_overlap(pair) -> bool:
    a1_left, a1_right = pair[0]
    a2_left, a2_right = pair[1]

    return any(
        [
            a1_left <= a2_left < a1_right,
            a1_left <= a2_left <= a1_right,
            a2_left <= a1_right <= a2_right,
            a2_left <= a1_left <= a2_right,
        ]
    )


if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        assignment_pairs = input_file.read().split('\n')
        assignment_pairs = [pair.split(',') for pair in assignment_pairs]
        assignment_pairs = [[list(map(int, pair[0].split('-'))), list(map(int, pair[1].split('-')))] for pair in assignment_pairs]

    result = 0

    part1 = sum(map(completely_overlap, assignment_pairs))

    print(f"Part 1: {part1}")

    part2 = sum(map(any_overlap, assignment_pairs))
    print(f"Part 2: {part2}")
