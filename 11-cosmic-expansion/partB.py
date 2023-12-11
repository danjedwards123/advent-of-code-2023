def solution() -> int:
    answer = 0
    galaxy_locations = {}

    with open("input.txt", "r") as f:
        lines = [list(x.strip()) for x in f.readlines()]

        col_empty = [True] * len(lines[0])
        row_empty = [True] * len(lines)

        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] == "#":
                    col_empty[j] = False
                    row_empty[i] = False

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
            
            distance = abs(galaxy_locations[i][0] - galaxy_locations[j][0]) + abs(galaxy_locations[i][1] - galaxy_locations[j][1])
            for row in range(min(galaxy_locations[i][0], galaxy_locations[j][0]), max(galaxy_locations[i][0], galaxy_locations[j][0])):
                if row_empty[row]:
                    distance += 999999
            for col in range(min(galaxy_locations[i][1], galaxy_locations[j][1]), max(galaxy_locations[i][1], galaxy_locations[j][1])):
                if col_empty[col]:
                    distance += 999999

            answer += distance

    return answer


if __name__ == "__main__":
    print(solution())