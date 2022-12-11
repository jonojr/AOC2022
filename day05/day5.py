import re

if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        incoming_state, instructions = input_file.read().split('\n\n')
        incoming_state = incoming_state.split('\n')

    incoming_state = incoming_state[:-1]
    incoming_state = [row[1::4] for row in incoming_state]

    state = [list() for _ in incoming_state[0]]
    state_part2 = [list() for _ in incoming_state[0]]

    for row in incoming_state[::-1]:
        for i, value in enumerate(row):
            if value != ' ':
                state[i].append(value)
                state_part2[i].append(value)

    print(f"Starting state: {state}")

    instructions = instructions.split('\n')
    for instruction in instructions:
        match = re.match(r"move (\d+) from (\d+) to (\d+)", instruction)

        count, start, end = map(int, match.group(1, 2, 3))

        # Fix 1 indexing
        start -= 1
        end -= 1

        to_move = state[start][-count:]
        to_move = to_move[::-1]  # Reverse list to account for one by one movement
        state[start] = state[start][:-count]
        state[end].extend(to_move)

        # Part 2
        to_move = state_part2[start][-count:]
        state_part2[start] = state_part2[start][:-count]
        state_part2[end].extend(to_move)

    print(f"Part 1: {''.join([stack[-1] for stack in state])}")
    print(f"Part 2: {''.join([stack[-1] for stack in state_part2])}")
