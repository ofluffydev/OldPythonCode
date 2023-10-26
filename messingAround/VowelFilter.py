def extract_vowels(input_str):
    vowels = ('a','e','i','o','u')
    result = ""
    for char in input_str:
        if char.lower() in vowels:
            result+= char
    return result

print(extract_vowels(input(str("Input? "))))