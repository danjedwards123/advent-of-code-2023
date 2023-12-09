def solution() -> int:
    f = open('input.txt', 'r')

    answer = 0

    for line in f:
        max_red = 0
        max_green = 0
        max_blue = 0

        line_parts = line.split(":")    
        for game_round in line_parts[1].split(";"):
            for balls in game_round.split(","):
                pick = balls.split()
                if pick[1] == "blue":
                    max_blue = max(max_blue, int(pick[0]))
                elif pick[1] == "green":
                    max_green = max(max_green, int(pick[0]))
                elif pick[1] == "red":
                    max_red = max(max_red, int(pick[0]))

        answer += (max_red * max_green * max_blue)

    f.close()

    return answer


if __name__ == '__main__':
    print(solution())