# new Caesar's cypher
text = input('Please write your message here: ')
key = input('Please enter an encoding key - from 1 to 25: ')  # check if input is int - else - redo
while True:
    try:
        while str(key).isnumeric() is False:
            key = input("Previous input is invalid. Enter again: ")
        while int(key) not in range(1, 26):
            key = int(input("Previous input is not in the specified range. Enter again: "))
        break
    except:
        key = input("Try again. ")

cipher = ''
key = int(key)
for char in text:
    if not char.isalpha():
        cipher += char
        continue

    code = ord(char) + key
    if code > ord('Z') and char == char.upper():
        code = ord(char) + key - ord('Z') + ord('A') - 1

    if code > ord('z') and char == char.lower():
        code = ord(char) + key - ord('z') + ord('a') - 1
    cipher += chr(code)
print(cipher)