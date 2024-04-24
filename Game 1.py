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
