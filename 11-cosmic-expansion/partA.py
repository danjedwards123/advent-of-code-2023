def solution() -> int:
    answer = 0
    galaxy_locations = {}

    with open("input.txt", "r") as f:
        lines = [list(x.strip()) for x in f.readlines()]

        col_empty = [True] * len(lines[0])
        row_empty = [True] * len(lines)
        i = 0
        j = 0
        while i < len(lines) and j < len(lines[i]):
            if lines[i][j] == "#":
                col_empty[j] = False
                row_empty[i] = False

            if j == len(lines[i]) - 1:
                i += 1
                j = 0
            else:
                j += 1

        for col_index in range(len(col_empty) - 1, -1, -1):
            if col_empty[col_index]:
                for row_index in range(len(lines)):
                    lines[row_index].insert(col_index + 1, '.')

        for row_index in range(len(row_empty) - 1, -1, -1):
            if row_empty[row_index]:
                lines.insert(row_index + 1, ['.'] * len(lines[0]))

        row_index = 0
        galaxy_count = 0
        for row in range(len(lines)):
            for col in range(len(lines[row])):
                if lines[row][col] == "#":
                    galaxy_count += 1
                    galaxy_locations[galaxy_count] = (row, col)

    for i in galaxy_locations:
        for j in galaxy_locations:
            if i < j:
                continue
            answer += abs(galaxy_locations[i][0] - galaxy_locations[j][0]) + abs(galaxy_locations[i][1] - galaxy_locations[j][1])

    return answer

if __name__ == "__main__":
    print(solution())