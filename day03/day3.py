def priority(character: str):
    ordinal = ord(character)

    # Lowercase
    if 97 <= ordinal <= 122:
        return ordinal - 96

    # Uppercase
    if 65 <= ordinal <= 90:
        return ordinal - 38

    raise ValueError(f"Invalid character given {character}, expected a-z or A-Z")


if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        rucksacks = input_file.read().split('\n')

    split_rucksacks = [(rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]) for rucksack in rucksacks]
    duplicated_items = [set(rucksack[0]).intersection(set(rucksack[1])).pop() for rucksack in split_rucksacks]
    print(f"Part 1: {sum(map(priority, duplicated_items))}")

    rucksack_sets = [set(rucksack) for rucksack in rucksacks]
    rucksack_groups = [rucksack_sets[i:i + 3] for i in range(len(rucksack_sets))[::3]]
    rucksack_group_items = [group[0].intersection(*group[1:]).pop() for group in rucksack_groups]
    print(f"Part 2: {sum(map(priority, rucksack_group_items))}")
