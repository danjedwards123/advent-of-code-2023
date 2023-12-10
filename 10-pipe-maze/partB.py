from collections import deque

def solution() -> int:
    answer = 0
    loop_coords = set()

    valid_directions = {
        'S': {
            (1, 0): set(['|', 'L', 'J']),
            (-1, 0): set(['|', '7', 'F']),
            (0, 1): set(['-', 'J', '7']),
            (0, -1): set(['-', 'L', 'F']),
        },
        '|': {
            (1, 0): set(['|', 'L', 'J']),
            (-1, 0): set(['|', '7', 'F']),
        },
        '-': {
            (0, 1): set(['-', 'J', '7']),
            (0, -1): set(['-', 'L', 'F']),
        },
        'L': {
            (-1, 0): set(['|', '7', 'F']),
            (0, 1): set(['-', 'J', '7']),
        },
        'J': {
            (-1, 0): set(['|', '7', 'F']),
            (0, -1): set(['-', 'L', 'F']),
        },
        '7': {
            (1, 0): set(['|', 'L', 'J']),
            (0, -1): set(['-', 'L', 'F']),
        },
        'F': {
            (1, 0): set(['|', 'L', 'J']),
            (0, 1): set(['-', 'J', '7']),
        },
    }

    with open('input.txt', 'r') as f:
        matrix = [[cols for cols in row.strip()] for row in f.readlines()]
        dfs_matrix = [[0 if matrix[row_i][col_i] == '.' else 1 for col_i, _ in enumerate(row)] for row_i, row in enumerate(matrix)]
        
        starting_point = ()
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 'S':
                    starting_point = (row, col)
                    break
            if starting_point != ():
                break


    queue = deque([starting_point])
    while len(queue) > 0:
        current_node = queue.popleft()
        loop_coords.add(current_node)

        finished_search = True
        for direction in valid_directions[matrix[current_node[0]][current_node[1]]]:
            new_node = (current_node[0] + direction[0], current_node[1] + direction[1])

            if not(new_node[0] >= 0 and new_node[0] < len(matrix) and new_node[1] >= 0 and new_node[1] < len(matrix[0])):
                continue

            if dfs_matrix[new_node[0]][new_node[1]] == 1 \
                and matrix[new_node[0]][new_node[1]] in valid_directions[matrix[current_node[0]][current_node[1]]][direction]:
                    queue.append(new_node)
                    dfs_matrix[new_node[0]][new_node[1]] = dfs_matrix[current_node[0]][current_node[1]] + 1
                    finished_search = False

        if finished_search:
            matrix[starting_point[0]][starting_point[1]] = '7'
            for row in range(len(matrix)):
                inside = False
                for col in range(len(matrix[row])):
                    if (row, col) in loop_coords and (matrix[row][col] == '|' or matrix[row][col] == "F" or matrix[row][col] == "7"):
                        inside = not inside
                    elif (row, col) not in loop_coords and inside:
                        answer += 1

            return answer

    return -1


if __name__ == '__main__':
    print(solution())