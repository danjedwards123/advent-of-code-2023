def solution() -> int:
    answer = 0
    card_totals = {}

    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
        card_totals = {num + 1: 1 for num in range(len(lines))}

        for i in range(len(lines)):
            winning = set(lines[i].split(':')[1].split('|')[0].split())
            numbers = set(lines[i].split(':')[1].split('|')[1].split())
            matching = winning.intersection(numbers)

            for j in range(len(matching)):
                card_totals[i + j + 2] += card_totals[i + 1]

    for value in card_totals.values():
        answer += value

    return answer 


if __name__ == "__main__":
    print(solution())