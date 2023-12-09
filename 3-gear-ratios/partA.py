def solution() -> int:
    matrix = []
    answer = 0

    with open('input.txt') as f:
        for line in f:
            matrix.append([x for x in line.strip()])


    i = 0
    j = 0
    num_string = ""
    add_to_answer = False
    while i < len(matrix) and j < len(matrix[0]):
        while j < len(matrix[0]) and matrix[i][j].isnumeric():
            if num_string == "":
                for direction in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1)]:
                    if i + direction[1] < 0 or j + direction[0] < 0 or i + direction[1] >= len(matrix) or j + direction[0] >= len(matrix[0]):
                        continue

                    to_check = matrix[i + direction[1]][j + direction[0]]
                    if not to_check.isnumeric() and to_check != '.':
                        add_to_answer = True
                        break
            else:
                for direction in [(0, 1), (0, -1)]:
                    if i + direction[1] < 0 or j + direction[0] < 0 or i + direction[1] >= len(matrix) or j + direction[0] >= len(matrix[0]):
                        continue

                    to_check = matrix[i + direction[1]][j + direction[0]]
                    if not to_check.isnumeric() and to_check != '.':
                        add_to_answer = True
                        break
            num_string += matrix[i][j]
            j += 1
        else:
            if num_string != "":
                for direction in [(0, 1), (0, 0), (0, -1)]:
                    if i + direction[1] < 0 or j + direction[0] < 0 or i + direction[1] >= len(matrix) or j + direction[0] >= len(matrix[0]):
                        continue

                    to_check = matrix[i + direction[1]][j + direction[0]]
                    if not to_check.isnumeric() and to_check != '.':
                        add_to_answer = True
                        break

            if add_to_answer:
                answer += int(num_string)
            num_string = ""
            add_to_answer = False

        if j >= len(matrix[0]) - 1:
            i += 1
            j = 0
        else:
            j += 1

    return answer


if __name__ == '__main__':
    print(solution())