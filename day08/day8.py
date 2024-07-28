from typing import cast


def get_column(grid: list[list[int]], col_id: int) -> list:
    return [row[col_id] for row in grid]


def part_1(grid: list[list[int]]) -> None:
    row_count = len(grid)
    col_count = len(grid[0])

    # All edge trees are visible
    visible_trees = 2 * row_count + 2 * col_count - 4

    for row_id in range(1, row_count - 1):
        row = grid[row_id]
        for col_id in range(1, col_count - 1):
            tree_height = grid[row_id][col_id]

            column = get_column(grid, col_id)

            left = row[:col_id]
            right = row[col_id + 1:]
            up = column[:row_id]
            down = column[row_id + 1:]

            tree_visible = any(
                [
                    all([height < tree_height for height in left]),
                    all([height < tree_height for height in right]),
                    all([height < tree_height for height in up]),
                    all([height < tree_height for height in down]),
                ]
            )
            visible_trees += tree_visible

    print(f"Part 1:\nTrees visible {visible_trees}")


def calculate_view_distance(view: list[int], tree_height: int) -> int:
    view_distance = 1
    for tree in view:
        if tree < tree_height:
            view_distance += 1
        else:
            break
    return min(view_distance, len(view))


def part_2(grid: list[list[int]]) -> None:
    row_count = len(grid)
    col_count = len(grid[0])

    best_scenic_score = 0

    for row_id in range(0, row_count - 1):
        row = grid[row_id]
        for col_id in range(0, col_count - 1):
            tree_height = grid[row_id][col_id]

            column = get_column(grid, col_id)

            left = row[:col_id]
            right = row[col_id + 1:]
            up = column[:row_id]
            down = column[row_id + 1:]
            left_view_distance = calculate_view_distance(left[::-1], tree_height)
            right_view_distance = calculate_view_distance(right, tree_height)
            up_view_distance = calculate_view_distance(up[::-1], tree_height)
            down_view_distance = calculate_view_distance(down, tree_height)

            scenic_score = left_view_distance * right_view_distance * up_view_distance * down_view_distance

            if scenic_score > best_scenic_score:
                best_scenic_score = scenic_score

    print(f"Part 2:\nBest scenic score {best_scenic_score}")


if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        buffer = input_file.read().strip()

    grid = buffer.split("\n")
    for row_index in range(len(grid)):
        grid[row_index] = [int(char) for char in grid[row_index]]

    grid = cast(list[list[int]], grid)

    part_1(grid)
    part_2(grid)
