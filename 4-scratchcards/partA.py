def solution() -> int:
    answer = 0

    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
        for line in lines:
            winning = set(line.split(':')[1].split('|')[0].split())
            numbers = set(line.split(':')[1].split('|')[1].split())
            matching = winning.intersection(numbers)

            if len(matching) > 0:
                answer += 2 ** (len(matching) - 1)

    return answer


if __name__ == "__main__":
    print(solution())