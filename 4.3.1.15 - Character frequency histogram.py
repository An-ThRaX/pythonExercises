import random, string, os
from os import strerror


def get_random_string(length):  # define a function to generate a random text to be used
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


sample = open("samplefile.txt", 'wt')  # create an open a file
sample.write(get_random_string(20))  # populate it with the random generator from above
sample.close()

counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}  # create a dict where we store the count of each letter
file_name = input("Choose a file: ")

try:
    f = open(file_name, 'rt')  # read through the file and count each char appearance
    for line in f:
        for char in line:
            if char.isalpha():
                counters[char.lower()] += 1
    f.close()
    for char in counters.keys():  # sort all the key which have values to be printed
        cnt = counters[char]
        if cnt > 0:
            print(char, '->', cnt)
except IOError as e:
    print("I/O Error", strerror(e.errno))

os.remove("samplefile.txt")  # delete the created file
