def solution() -> int:
    matrix = []
    seen_set = set()
    answer = 0
    
    with open('input.txt') as f:
        for line in f:
            matrix.append([x for x in line.strip()])

    i = 0
    j = 0
    while i < len(matrix) and j < len(matrix[0]):
        if matrix[i][j] == '*':
            first_num_string = ""
            first_num_location = (0, 0)
            second_num_string = ""
            second_num_location = (0, 0)

            for direction in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)]:
                if i + direction[1] < 0 or j + direction[0] < 0 or i + direction[1] >= len(matrix) or j + direction[0] >= len(matrix[0]):
                    continue
                
                k = i + direction[1]
                l = j + direction[0]
                num_string = ""
                
                if matrix[k][l].isnumeric():
                    num_string += matrix[k][l]                    

                    l = j + direction[0] + 1
                    while l < len(matrix[0]) and matrix[k][l].isnumeric():
                        num_string += matrix[k][l]
                        l += 1

                    l = j + direction[0] - 1
                    while l > 0 and matrix[k][l].isnumeric():
                        num_string = matrix[k][l] + num_string
                        l -= 1                        

                if first_num_string == "" and (k, l + 1) not in seen_set:
                    first_num_string = num_string
                    first_num_location = (k, l + 1)
                elif second_num_string == "" and (k, l + 1) not in seen_set and (k, l + 1) != first_num_location:
                    second_num_string = num_string
                    second_num_location_num_location = (k, l + 1)

            if first_num_string != "" and second_num_string != "":
                answer += int(first_num_string) * int(second_num_string)
                seen_set.add(first_num_location)
                seen_set.add(second_num_location)

        if j >= len(matrix[0]) - 1:
            i += 1
            j = 0
        else:
            j += 1

    return answer


if __name__ == '__main__':
    print(solution())