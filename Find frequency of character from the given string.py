def character_frequency(input_string):
    # Create an empty dictionary to store character frequencies
    frequency = {}
    
    # Iterate over each character in the string
    for char in input_string:
        # If the character is already in the dictionary, increment its count
        if char in frequency:
            frequency[char] += 1
        # If the character is not in the dictionary, add it with a count of 1
        else:
            frequency[char] = 1
            
    return frequency

# Example usage
input_string = input("Enter a string: ")
frequency = character_frequency(input_string)

# Print the frequency of each character
for char, count in frequency.items():
    print(f"'{char}': {count}")
