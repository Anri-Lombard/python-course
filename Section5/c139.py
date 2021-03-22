def is_palindrome(sentence):
    return sentence[::-1].casefold() == sentence.casefold()


def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char

    return string[::-1].casefold() == string.casefold()


user_sentence = input("Please enter a word tho check: ")
if palindrome_sentence(user_sentence):
    print(f"'{user_sentence}' is a palindrome")
else:
    print(f"'{user_sentence}' is not a palindrome")
