import random

def user_input():
    dice_rolls = int(input("How many times would you like to roll the dice?: "))
    return dice_rolls

def roll_dice(dice_rolls):
    total_rolls = 0
    print("Value   Rolls   Actual %   Expected %   Difference")
    print("-------------------------------------------------")

    roll_counts = [0] * 13

    for _ in range(dice_rolls):
        result = random.randint(1, 6) + random.randint(1, 6)
        total_rolls += 1
        roll_counts[result] += 1

    for value, count in enumerate(roll_counts[2:], start=2):
        expected_percent = 1 / 11 * 100  # Calculate the expected percentage
        actual_percent = count / total_rolls * 100
        difference = actual_percent - expected_percent
        print(f"{value:5} {count:7} {actual_percent:.2f}% {expected_percent:.2f}% {difference:.2f}%")

    print("\nTotal number of rolls:", total_rolls)

def main():
    rolls = user_input()
    roll_dice(rolls)

if __name__ == "__main__":
    main()
