def is_palindrome(word):
    word = word.replace(" ","").lower()
    if word == word[::-1]:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")

name = input("Input a phrase to find if it's a palindrome: ")
is_palindrome(name)