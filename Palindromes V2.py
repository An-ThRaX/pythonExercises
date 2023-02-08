# palindromes 2nd attempt
text = input('Please insert your palindrome: ').lower()
while len(text) == 0:
    text = input('Please insert a valid palindrome: ').lower()
text = "".join(text.split())
text = list(text)
text2 = []
for i in range(len(text)):
    text2.append(text[len(text) - i - 1])
if text == text2:
    print("It's a palindrome")
else:
    print("It's not a palindrome")
