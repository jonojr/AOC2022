
if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        buffer = input_file.read()

    for i in range(4, len(buffer)):
        window = buffer[i-4:i]
        if len(set(window)) == 4:
            print(f"Part 1: {i}")
            break

    for i in range(14, len(buffer)):
        window = buffer[i - 14:i]
        if len(set(window)) == 14:
            print(f"Part 2: {i}")
            break
