import random
import string
from collections import Counter


# Number Guessing Game
def guessing_game():
    best_score = 0

    while True:
        secret_number = random.randint(1, 100)
        attempts = 0
        max_attempts = 7
        score = 100

        print("\nGuess a number between 1 and 100!")

        while attempts < max_attempts:
            try:
                guess = int(input("Enter your guess: "))

                if guess < 1 or guess > 100:
                    print("Enter a number between 1 and 100.")
                    continue

                attempts += 1

                if guess == secret_number:
                    print("Correct! You won!")
                    score = 100 - (attempts - 1) * 10
                    print("Your score:", score)

                    if score > best_score:
                        best_score = score

                    break

                elif guess < secret_number:
                    print("Too low! Try again.")

                else:
                    print("Too high! Try again.")

            except ValueError:
                print("Invalid input! Enter a whole number.")

        else:
            score = 0
            print("Game over! The number was:", secret_number)

        print("Best score:", best_score)

        again = input("Play again? (yes/no): ").lower()

        if again != "yes":
            break


# Word Counter
def word_counter():
    filename = input("Enter file name (example: sample.txt): ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

        # Convert text to lowercase
        text = text.lower()

        # Remove punctuation
        text = text.translate(str.maketrans("", "", string.punctuation))

        # Split text into words
        words = text.split()

        if not words:
            print("The file is empty!")
            return

        # Count word frequency
        word_count = Counter(words)

        print("\n--- Word Frequency ---")
        print("Total words:", len(words))
        print("Unique words:", len(word_count))

        print("\nTop 10 Most Common Words:")
        print("-------------------------")

        for word, count in word_count.most_common(10):
            print(f"{word:<15} {count}")

    except FileNotFoundError:
        print("File not found! Please check the file name.")


# Main Menu
def main():
    while True:
        print("\n===== PYTHON TOOLKIT =====")
        print("1. Number Guessing Game")
        print("2. Word Frequency Counter")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            guessing_game()

        elif choice == "2":
            word_counter()

        elif choice == "3":
            print("Thank you for using Python Toolkit!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
