sentence = input("Please write any sentence you want with random words capitalized, then I will try to extract the "
                 "capital letters: ")
uppercase_letters = ""

for char in sentence:
    if char.isupper():
        uppercase_letters += char

print(uppercase_letters)
