# palindrome - verify that 1st and last are equal - go on
def is_palindrome(txt):
    for i in range(int(len(txt) / 2)):  # iterate from 0 to half the text's length
        if txt[i] != txt[len(txt) - i - 1]:  # check if first and last are not equal, and so on
            return False  # when 2 indexes are found !=, return False
    return True


text = input('Please insert your palindrome: ').lower()  # convert all to lower case
while len(text) == 0:
    text = input('Please insert a valid palindrome: ').lower()  # make sure the string is not empty
text = "".join(text.split())  # take out all the spaces
if is_palindrome(text):
    print("It's a palindrome")
else:
    print("It's not a palindrome")


# title
# palindromes 2nd attempt - transposition the text into a new list and check if they are equal

# text = input('Please insert your palindrome: ').lower()
# while len(text) == 0:
#     text = input('Please insert a valid palindrome: ').lower()  # make sure the string is not empty
# text = "".join(text.split())  # take out all the spaces
# text = list(text)
# text2 = []
# for i in range(len(text)):
#     text2.append(text[len(text) - i - 1])  # duplicate the initial string, but transposition all indexes
# if text == text2:
#     print("It's a palindrome")
# else:
#     print("It's not a palindrome")
