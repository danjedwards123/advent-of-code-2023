def solution() -> int:
    answer = 1

    with open("input.txt", "r") as f:
        lines = f.readlines()
        
        times = [int(x) for x in lines[0].split(":")[1].split()]
        distances = [int(x) for x in lines[1].split(":")[1].split()]
        
        for i in range(len(times)):
            ways = 0
            for j in range(times[i] + 1):
                if j * (times[i] - j) > distances[i]:
                    ways += 1
            answer *= ways

    return answer


if __name__ == "__main__":
    print(solution())