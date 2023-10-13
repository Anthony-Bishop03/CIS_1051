import random


def user_input():
    dice_rolls = int(input("How many times would you like to roll the dice?: "))
    return dice_rolls


def roll_dice(dice_rolls):
    total_rolls = 0
    print("Value   Rolls   Percentage")
    print("-------------------------")

    roll_counts = [0] * 13

    for _ in range(dice_rolls):
        result = random.randint(1, 6) + random.randint(1, 6)
        total_rolls += 1
        roll_counts[result] += 1

    for value, count in enumerate(roll_counts[2:], start=2):
        percent = count / total_rolls * 100
        print(f"{value:5} {count:7} {percent:.2f}%")

    print("\nTotal number of rolls:", total_rolls)


def main():
    rolls = user_input()
    roll_dice(rolls)


if __name__ == "__main__":
    main()
