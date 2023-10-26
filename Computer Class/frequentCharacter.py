input_string = input("Enter a string: ").lower()
letters = {}
for character in input_string:
    if character in letters:
        letters[character] += 1
    else:
        letters[character] = 1

most_frequent_letter = ''
highest_frequency = 0
for letter, frequency in letters.items():
    if frequency > highest_frequency:
        most_frequent_letter = letter
        highest_frequency = frequency

if highest_frequency > 1:
    print("The most repeated character was: %s, and it was repeated %d times." % (most_frequent_letter, highest_frequency))
else:
    print("No characters were repeated more than once")
