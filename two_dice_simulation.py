from random import randint
from collections import Counter


def dice_role():
    return sum([randint(1, 6), randint(1, 6)])


# print(dice_role())


def main():
    rolls = []
    for i in range(1000):
        rolls.append(dice_role())
    dic = Counter(rolls)
    # print(dic)
    expected = {2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89, 7: 16.67,\
                8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78}
    print(f"{'Total':<20} {'Simulated percent':<20}{'Expected percent':<20}")
    for k in range(2, 13):
        print("{:<20} {:<20} {:<20}".format(k, dic[k]/10, expected[k]))


if __name__ == "__main__":
    main()
