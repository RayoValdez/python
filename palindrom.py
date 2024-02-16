# Program to check for palindrome


# Function to check if a word is palindrome
def is_palindrome(word):
    word = word.lower()  # Convert to lowercase to avoid case differences
    return word == word[::-1]


# Taking input word from the user
word_input = input("Enter a word: ")


# Checking if the word is palindrome or not
if is_palindrome(word_input):
    print(f"{word_input} is a palindrome!")
else:
    print(f"{word_input} is not a palindrome.")

