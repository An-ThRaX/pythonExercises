# palindrome - verify that 1st and last are equal - go on
def is_palindrome(txt):
    for i in range(int(len(txt) / 2)):
        if txt[i] != txt[len(txt) - i - 1]:
            return False
    return True


text = input('Please insert your palindrome: ').lower()
while len(text) == 0:
    text = input('Please insert a valid palindrome: ').lower()
text = "".join(text.split())
if is_palindrome(text):
    print("It's a palindrome")
else:
    print("It's not a palindrome")


# palindromes 2nd attempt - transposition the text into a new list and check if they are equal
# text = input('Please insert your palindrome: ').lower()
# while len(text) == 0:
#     text = input('Please insert a valid palindrome: ').lower()
# text = "".join(text.split())
# text = list(text)
# text2 = []
# for i in range(len(text)):
#     text2.append(text[len(text) - i - 1])
# if text == text2:
#     print("It's a palindrome")
# else:
#     print("It's not a palindrome")
