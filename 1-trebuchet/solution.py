def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)


def solution() -> int:
    word_to_num = {
      "one" : 1,
      "two" : 2,
      "three" : 3,
      "four" : 4,
      "five" : 5,
      "six" : 6,
      "seven" : 7,
      "eight" : 8,
      "nine" : 9,
    }

    num_to_word = {
      1 : "one",
      2 : "two",
      3 : "three",
      4 : "four",
      5 : "five",
      6 : "six",
      7 : "seven",
      8 : "eight",
      9 : "nine",
    }
    
    f = open('input.txt', 'r')

    answer = 0

    for line in f:
        word_locations = {
          "one" : -1,
          "two" : -1,
          "three" : -1,
          "four" : -1,
          "five" : -1,
          "six" : -1,
          "seven" : -1,
          "eight" : -1,
          "nine" : -1,
        }

        for word in word_locations.keys():
            word_locations[word] = list(find_all(line, word))

        word_locations = {k: v for k, v in word_locations.items() if len(v) > 0}        

        first_word = word_to_num[min(word_locations, key=lambda x: min(word_locations[x]))] if word_locations else -1
        second_word = word_to_num[max(word_locations, key=lambda x: max(word_locations[x]))] if word_locations else -1

        first_num = -1
        second_num = -1

        for i in range(len(line)):
            if line[i].isnumeric():
                if first_num == -1:
                    first_num = i
                second_num = i

        first = line[first_num] if first_word == -1 or first_num < min(word_locations[num_to_word[first_word]]) else first_word
        second = line[second_num] if second_word == -1 or second_num > max(word_locations[num_to_word[second_word]]) else second_word

        answer += int(str(first) + str(second))

    f.close()
    return answer


if __name__ == '__main__':
    print(solution())