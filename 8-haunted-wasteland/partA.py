def solution() -> int:
    steps = 0

    with open('input.txt', 'r') as f:
        lines = f.readlines()

        path = list(lines[0].strip())
        mapping = {}

        for i in range(2, len(lines)):
            parts = lines[i].split('=')
            lr_map = parts[1].strip().replace('(', '').replace(')', '').split(', ')
            mapping[parts[0].strip()] = (lr_map[0], lr_map[1])

        direction_index = 0
        location = "AAA"
        while location != "ZZZ":
            if path[direction_index] == 'L':
                location = mapping[location][0]
            else:
                location = mapping[location][1]

            steps += 1
            direction_index = (direction_index + 1) % len(path)

    return steps


if __name__ == '__main__':
    print(solution())