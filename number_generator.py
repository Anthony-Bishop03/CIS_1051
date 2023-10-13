import random

def user_input():
    iterations = int(input("How many times would you like to generate a number between 2 and 12?: "))
    return iterations

def generate_numbers(iterations):
    total_iterations = 0

    print("These are the numbers accompanied by how many times they were generated:")
    for value in range(2, 13):
        count = 0
        for i in range(iterations):
            result = random.randint(2, 12)
            if result == value:
                count += 1
            total_iterations += 1

        percent = round((count / iterations) * 100, 2)
        print("Value: " + str(value) + ", Generated: " + str(count) + ", Percentage: " + str(percent) + "%")

    print("\nTotal number of iterations: " + str(total_iterations))

def main():
    generate_numbers(user_input())
if __name__ == "__main__":
   main()