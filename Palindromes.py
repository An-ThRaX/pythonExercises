# palindrome
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

