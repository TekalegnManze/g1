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


