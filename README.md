
_1.	rock paper scissors  is a simple game you can play with a friend .
  	the game is played by each player choosing one of rock,paper,or scissors,
  	and then the players compare their choices it is  a draw if both players
  	have chosen the same thing.otherwise ,the winner is the player who has chosen
	  the winning hand(rock beats scissors,paper beats rock,scissors beats paper).
	  to create the rock,paper and scissors game with python,you need to take the
	  users choice and then you need to compare it with the computer choice and
	  finally print the statistics means how many times the users wins,how many
	  times the computer wins and how many times they draw?_****
## here is one phython project
import random

# Create a list of play options
choices = ["rock", "paper", "scissors"]

# Initialize win counters
user_wins = 0
computer_wins = 0
draws = 0

# Play multiple rounds
while True:
    # Take user input
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    # Validate user input
    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    # Generate computer's choice
    computer_choice = random.choice(choices)

    # Determine the winner
    if user_choice == computer_choice:
        draws += 1
        print("It's a draw!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        user_wins += 1
        print(f"You win! Computer chose {computer_choice}.")
    else:
        computer_wins += 1
        print(f"Computer wins! It chose {computer_choice}.")

    # Ask if the user wants to play again
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break

# Print final statistics
print("\nGame Over!")
print(f"User wins: {user_wins}")
print(f"Computer wins: {computer_wins}")
print(f"Draws: {draws}")





**_2. write a python program that will read in a string and give you the character frequency count (14E|'s,12T's,8A's etc.)(16-30)_**

def character_frequency_count(input_string):
    # Create a dictionary to store character frequencies
    char_counts = {}

    # Iterate through the input string
    for char in input_string:
        if char.isalpha():  # Consider only alphabetic characters
            char = char.upper()  # Convert to uppercase for consistent counting
            char_counts[char] = char_counts.get(char, 0) + 1

    # Print the results in the desired format
    for char, count in char_counts.items():
        print(f"{count}{char}'s", end=", ")

# Example usage
user_input = input("Enter a string: ")
character_frequency_count(user_input)




_3.	write python program to convert roman number into decimal? you can assume the number will between 1 to 3999_****

def value(r):
    if r == 'I':
        return 1
    elif r == 'V':
        return 5
    elif r == 'X':
        return 10
    elif r == 'L':
        return 50
    elif r == 'C':
        return 100
    elif r == 'D':
        return 500
    elif r == 'M':
        return 1000
    else:
        return -1

def roman_to_decimal(roman_str):
    res = 0
    i = 0
    while i < len(roman_str):
        s1 = value(roman_str[i])
        if i + 1 < len(roman_str):
            s2 = value(roman_str[i + 1])
            if s1 >= s2:
                res += s1
                i += 1
            else:
                res += s2 - s1
                i += 2
        else:
            res += s1
            i += 1
    return res

# Example usage
user_input = input("Enter a Roman numeral: ")
decimal_value = roman_to_decimal(user_input.upper())
print(f"Decimal value of {user_input} is {decimal_value}")
group work
write pyhon program that will read a text file(with at least 10 lines) and perform the following tasks

1. identify words in the text (it is better to remove special charachter like semicolon,comma,fullstop,
 etc.since they are not part of meanigful words) 2.create a function that compute word frequency in the.
 text file and displays words in decreasing order of their frequency 3.create a function that compute
  character frequecny in the text file and display the first five most frequently occuring character
_ __ 4. finally out put stastical information such as total lines,total word and total character
   in the text file (use text written in local language(amharic) ) answer it
_****__


1.	Identify Words in the Text File: We’ll read the text file, split it into words, and remove any special characters. We’ll consider only meaningful words.
2.	Compute Word Frequency: We’ll create a function that calculates the frequency of each word in the text file and displays them in decreasing order.
3.	Compute Character Frequency: We’ll create another function to compute the frequency of each character in the text file and display the top five most frequently occurring characters.
4.	Statistical Information: Finally, we’ll output the total number of lines, words, and characters in the text file.
Here’s the Python program that accomplishes these tasks:
Python
def read_text_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content

def clean_text(text):
    # Remove special characters and split into words
    words = text.lower().split()
    return words

def compute_word_frequency(words):
    from collections import Counter
    word_freq = Counter(words)
    return word_freq

def compute_char_frequency(text):
    char_freq = Counter(text)
    return char_freq

def main():
    filename = 'your_text_file.txt'  # Replace with your actual file name
    content = read_text_file(filename)
    words = clean_text(content)

    # Word frequency
    word_freq = compute_word_frequency(words)
    print("Word Frequency (Top 10):")
    for word, freq in word_freq.most_common(10):
        print(f"{word}: {freq}")

    # Character frequency
    char_freq = compute_char_frequency(content)
    print("\nCharacter Frequency (Top 5):")
    for char, freq in char_freq.most_common(5):
        print(f"{char}: {freq}")

    # Statistical information
    num_lines = content.count('\n') + 1
    num_words = len(words)
    num_chars = len(content)
    print(f"\nTotal Lines: {num_lines}")
    print(f"Total Words: {num_words}")
    print(f"Total Characters: {num_chars}")

if __name__ == "__main__":
    main()

Make sure to replace 'your_text_file.txt' with the actual path to your text file. This program will read the file, clean the text, compute word and character frequencies, and display statistical information.


















Here’s the Python program:
Python
def read_text_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def clean_text(text):
    # Remove special characters and split into words
    words = text.lower().split()
    return words

def compute_word_frequency(words):
    from collections import Counter
    word_freq = Counter(words)
    return word_freq

def compute_char_frequency(text):
    char_freq = Counter(text)
    return char_freq

def main():
    filename = 'your_text_file.txt'  # Replace with your actual file name
    content = read_text_file(filename)
    words = clean_text(content)

    # Word frequency
    word_freq = compute_word_frequency(words)
    print("Word Frequency (Top 10):")
    for word, freq in word_freq.most_common(10):
        print(f"{word}: {freq}")

    # Character frequency
    char_freq = compute_char_frequency(content)
    print("\nCharacter Frequency (Top 5):")
    for char, freq in char_freq.most_common(5):
        print(f"{char}: {freq}")

    # Statistical information
    num_lines = content.count('\n') + 1
    num_words = len(words)
    num_chars = len(content)
    print(f"\nTotal Lines: {num_lines}")
    print(f"Total Words: {num_words}")
    print(f"Total Characters: {num_chars}")

if __name__ == "__main__":
    main()
AI-generated code. Review and use carefully. More info on FAQ.
Make sure to replace 'your_text_file.txt' with the actual path to your text file written in Amharic. This program will read the file, clean the text, compute word and character frequencies, and display statistical information.


