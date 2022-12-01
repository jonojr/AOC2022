
if __name__ == "__main__":
    elves = []
    with open("input.txt", "r") as input_file:
        caloric_values = input_file.read().split('\n\n')
        for elf in caloric_values:
            elves.append([int(value) for value in elf.split()])

    elves = sorted([sum(elf) for elf in elves])
    print(f"Part 1: {elves[-1]}")
    print(f"Part 2: {sum(elves[-3:])}")
