from math import lcm

def solution() -> int:
    steps = 1

    with open('input.txt', 'r') as f:
        lines = f.readlines()

        path = list(lines[0].strip())
        mapping = {}

        for i in range(2, len(lines)):
            parts = lines[i].split('=')
            lr_map = parts[1].strip().replace('(', '').replace(')', '').split(', ')
            mapping[parts[0].strip()] = (lr_map[0], lr_map[1])

        locations = [x for x in mapping.keys() if x[2] == 'A']
        steps_to_finish = [0 for _ in range(len(locations))]

        for i in range(len(locations)):
            direction_index = 0
            location = locations[i]
            while location[2] != "Z":
                if path[direction_index] == 'L':
                    location = mapping[location][0]
                else:
                    location = mapping[location][1]

                steps_to_finish[i] += 1
                direction_index = (direction_index + 1) % len(path)

    return lcm(*steps_to_finish)


if __name__ == '__main__':
    print(solution())