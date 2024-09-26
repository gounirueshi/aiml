import random

def roll_dice(num_dice=1):
    results = []

    for _ in range(num_dice):
        result = random.randint(1, 6)
        results.append(result)

    print(f"Rolling {num_dice} dice...")
    print("Results:", results)
    print("Total:", sum(results))

    return results

# Corrected main function check
if __name__ == "__main__":
    number_of_dice = int(input("Enter the number of dice to roll: "))
    roll_dice(number_of_dice)
