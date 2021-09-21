### Task 4.2
text = "Tennet"
def palindrome_or_not(text):
    """ function that check whether a string is a palindrome or not."""
    if text.lower() == text.lower()[::-1]:
        return "It's a palindrome"
    else:
        return "It's not a palindrome"
print(palindrome_or_not(text))