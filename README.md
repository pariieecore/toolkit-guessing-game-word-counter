# Python Toolkit – Guessing Game & Word Counter

## About the Project

This project is a simple Python-based command-line application that combines a Number Guessing Game and a Word Frequency Counter.

Users can play a guessing game with a scoring system or analyze a text file to find the most frequently used words.

## Features

### 1. Number Guessing Game
- Generates a random number between 1 and 100.
- Gives the player 7 attempts.
- Displays hints like Too High and Too Low.
- Awards points based on the number of attempts.
- Tracks the best score.
- Allows replaying the game.

### 2. Word Frequency Counter
- Reads text from a file.
- Converts text into lowercase.
- Removes punctuation.
- Counts the frequency of each word.
- Displays the top 10 most common words.
- Shows total and unique word counts.
- Handles missing and empty files.

## Scoring System

- Starting score: 100 points.
- Every incorrect guess reduces 10 points.
- Maximum score: 100 points.
- No points are awarded if the player fails to guess correctly within 7 attempts.

## Technologies Used
- Python 3
- Random Module
- Collections Module
- String Module
- File Handling

## How to Run

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Make sure `main.py` and `sample.txt` are in the same folder.
4. Open the terminal.
5. Run the command:

```bash
python main.py
```



## Concepts Learned

- Random number generation
- Python functions
- While loops and conditional statements
- Dictionaries and Counter
- File handling
- Exception handling
- String manipulation
- Sorting word frequencies

## Learning Outcome

Through this project, I learned how to use Python's random module, implement a scoring system, read text files, count word frequencies, handle errors, and create an interactive menu-driven application.

## Author

Pari Bansal
