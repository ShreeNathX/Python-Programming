#Take a character and check if it’s a vowel or consonant. 

char = input("Input one char :")

if char.lower() in 'aeiou':
    print("Vowel")
elif char.isalpha():
    print("Consonant")
else:
    print("Not a letter")
