char = input("Enter a character: ")
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
if len(char) == 1:
    if char in vowels:
        print(f'{char} is vowel letter.')
    elif char in consonants:
        print(f'{char} is consonant letter.')
    else:
        print(f'{char} is not alphabet letter.')
else:
    print("Provide only one character.")
