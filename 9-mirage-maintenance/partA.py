def next_value(pattern: list[int]) -> int:
    if all(ele == 0 for ele in pattern):
        return 0
    
    new_pattern = []
    for i in range(1, len(pattern)):
        new_pattern.append(pattern[i] - pattern[i - 1])

    return pattern[-1] + next_value(new_pattern)


def solution() -> int:
    with open("input.txt", "r") as f:
        lines = f.readlines()
        history = [list(map(int, x.strip().split())) for x in lines]        

        next_values = [next_value(x) for x in history]
        
        return sum(next_values)


if __name__ == "__main__":
    print(solution())