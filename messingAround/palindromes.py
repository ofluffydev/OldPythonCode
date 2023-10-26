word = input("Enter a word: ").lower()
flipped_word = word[::-1]
if word == flipped_word:
    print("Word is a palindrome.")
else:
    print("Word is not a palindrome")