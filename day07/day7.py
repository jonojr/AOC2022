import math
from typing import Self


class File:
    def __init__(self, directory: "Dir", filename: str, size: int):
        self.directory = directory
        self.filename = filename
        self.size = size

    def get_path(self):
        return f"{self.directory.get_path()}/{self.filename} (size: {self.size})"

    def __repr__(self):
        return self.get_path()


class Dir:
    def __init__(self, parent: Self | None, dir_name: str):
        self.parent = parent
        self.dir_name = dir_name
        self.files: dict[str, File] = {}
        self.dirs: dict[str, Dir] = {}

    def get_size(self) -> int:
        return sum([file.size for file in self.files.values()]) + sum(
            [directory.get_size() for directory in self.dirs.values()])

    def get_path(self) -> str:
        path = [self.dir_name]
        location = self
        while location.parent is not None:
            path.append(location.parent.dir_name)
            location = location.parent

        return "/".join(path[::-1])

    def __str__(self):
        return f"{self.get_path()} size={self.get_size()}"

    def __repr__(self):
        return f"{self.get_path()} size={self.get_size()}"


def process_inputs(terminal_stream: str) -> dir:
    base_dir = Dir(None, "")
    current_dir = base_dir

    print("Processing inputs")

    for action_data in terminal_stream.split("$ "):
        action_data = action_data.strip()
        action = action_data.split("\n")[0].split(" ")
        response = action_data.split("\n")[1:]

        match action:
            case ["cd", "/"]:
                current_dir = base_dir
            case ["cd", ".."]:
                current_dir = current_dir.parent
            case ["cd", directory]:
                current_dir = current_dir.dirs[directory]
            case ["ls"]:
                for result in response:
                    result = result.split(" ")

                    if result[0] == 'dir':
                        if result[1] not in current_dir.dirs.keys():
                            current_dir.dirs[result[1]] = Dir(current_dir, result[1])
                    else:
                        current_dir.files[result[1]] = File(current_dir, result[1], int(result[0]))
    print("Processing finished")
    return base_dir


def generate_list_of_dirs(current_dir) -> list[Dir]:
    if len(current_dir.dirs.keys()) == 0:
        return [current_dir]

    result = [current_dir]
    child_dirs = current_dir.dirs.values()

    for child_dir in child_dirs:
        result.extend(generate_list_of_dirs(child_dir))

    return result


def part_1(filesystem: Dir):
    MAX_DIR_SIZE = 100_000
    list_of_dirs = generate_list_of_dirs(filesystem)

    sum_of_small_dirs = 0

    for directory in list_of_dirs:
        dir_size = directory.get_size()
        if dir_size <= MAX_DIR_SIZE:
            sum_of_small_dirs += dir_size

    print(f"Part 1:\nSum of dirs <= {MAX_DIR_SIZE}: {sum_of_small_dirs}")


def part_2(filesystem: Dir):
    AVAILABLE_SPACE = 70_000_000
    REQUIRED_SPACE = 30_000_000

    current_free_space = AVAILABLE_SPACE - filesystem.get_size()
    min_to_delete = REQUIRED_SPACE - current_free_space

    result = math.inf

    list_of_dirs = generate_list_of_dirs(filesystem)
    for directory in list_of_dirs:
        dir_size = directory.get_size()
        if dir_size >= min_to_delete and dir_size < result:
            result = dir_size
    print(f"Part 2:\nSize of directory to delete: {result}")


if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        buffer = input_file.read()

    filesystem = process_inputs(buffer)

    part_1(filesystem)
    part_2(filesystem)
