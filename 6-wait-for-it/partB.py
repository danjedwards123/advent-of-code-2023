def solution() -> int:
    answer = 0

    with open("input.txt", "r") as f:
        lines = f.readlines()
        
        time = int("".join(lines[0].split(":")[1].split()))
        distance = int("".join(lines[1].split(":")[1].split()))

        for i in range(1, int(time / 2 + 1)):
            if i * (time - i) > distance:
                answer += 2

    return answer


if __name__ == "__main__":
    print(solution())