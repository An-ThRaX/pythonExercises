# new Caesar's cypher
text = input('Please write your message here: ')
key = input('Please enter an encoding key - from 1 to 25: ')
# check if input is int; else, retry until it is
while True:
    try:
        while str(key).isnumeric() is False:  # no numbers
            key = input("Previous input is invalid. Enter again: ")
        while int(key) not in range(1, 26):  # is not in the given range
            key = int(input("Previous input is not in the specified range. Enter again: "))
        break
    except:
        key = input("Try again. ")

cipher = ''
key = int(key)  # turn the input to int
for char in text:  # iterate the given text
    if not char.isalpha():  # if a non alpha-numeric char is found, skip and move to next
        cipher += char
        continue

    code = ord(char) + key  # determine the encrypted letter (add the key to the ord of real letter)
    if code > ord('Z') and char == char.upper():  # if the new ASCII code is higher than 'Z' ord and the initial
        # letter is an upper letter, then see below
        code = ord(char) + key - ord('Z') + ord('A') - 1  # from the current ord (char ord + key) subtract the Z ord,
        # add the A ord and subtract 1 more to get the desired lower case ord

    if code > ord('z') and char == char.lower():
        code = ord(char) + key - ord('z') + ord('a') - 1  # do the same, but get upper case ord
    cipher += chr(code)
print(cipher)