from collections import Counter
from functools import cmp_to_key

def solution() -> int:
    strength = {
        "A": 13,
        "K": 12,
        "Q": 11,
        "J": 10,
        "T": 9,
        "9": 8,
        "8": 7,
        "7": 6,
        "6": 5,
        "5": 4,
        "4": 3,
        "3": 2,
        "2": 1
    }

    answer = 0

    with open("input.txt", "r") as f:
        lines = f.readlines()

        hands = [line.strip().split(" ")[0] for line in lines]
        bids = [int(line.strip().split(" ")[1]) for line in lines]

        grouped_hands = {
            "five_kind": [],
            "four_kind": [],
            "full_house": [],
            "three_kind": [],
            "two_pair": [],
            "one_pair": [],
            "high_card": []
        }

        for i in range(len(hands)):
            card_count = Counter(hands[i])
            if len(card_count.keys()) == 1:
                grouped_hands["five_kind"].append((hands[i], bids[i]))
            elif len(card_count.keys()) == 2:
                if 4 in card_count.values():
                    grouped_hands["four_kind"].append((hands[i], bids[i]))
                else:
                    grouped_hands["full_house"].append((hands[i], bids[i]))
            elif len(card_count.keys()) == 3:
                if 3 in card_count.values():
                    grouped_hands["three_kind"].append((hands[i], bids[i]))
                else:
                    grouped_hands["two_pair"].append((hands[i], bids[i]))
            elif len(card_count.keys()) == 4:
                grouped_hands["one_pair"].append((hands[i], bids[i]))
            else:
                grouped_hands["high_card"].append((hands[i], bids[i]))

        def sort_hand(handA, handB):
            if handA[0][0] != handB[0][0]:
                return strength[handA[0][0]] - strength[handB[0][0]]
            elif handA[0][1] != handB[0][1]:
                return strength[handA[0][1]] - strength[handB[0][1]]
            elif handA[0][2] != handB[0][2]:
                return strength[handA[0][2]] - strength[handB[0][2]]
            elif handA[0][3] != handB[0][3]:
                return strength[handA[0][3]] - strength[handB[0][3]]
            else:
                return strength[handA[0][4]] - strength[handB[0][4]]

        for key in grouped_hands.keys():
            grouped_hands[key] = sorted(grouped_hands[key], key=cmp_to_key(sort_hand), reverse=True)

        i = len(hands)
        for key in grouped_hands.keys():
            for hand in grouped_hands[key]:
                answer += hand[1] * i
                i -= 1

    return answer


if __name__ == "__main__":
    print(solution())