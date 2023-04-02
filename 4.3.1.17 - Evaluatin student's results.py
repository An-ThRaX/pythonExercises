from os import strerror


class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    # Write your code here.
    def __init__(self, message):
        StudentsDataException.__init__(self, message)


class FileEmpty(StudentsDataException):
    # Write your code here.
    def __init__(self, message):
        StudentsDataException.__init__(self, message)

inputx = ''
fullname= ''
dict = {}
source_name = "C:\\Users\\cipri\\PycharmProjects\\pythonLearning\\notes.txt"

try:
    source = open(source_name, 'rt')  # open the file and write all the lines from the source file as a list
    inputx = source.readlines()
    source.close()
    if len(inputx) == 0:
        raise FileEmpty('Error: this file is empty.')
    for x in range(len(inputx)):  # split each line into indiv elements
        temp = inputx[x].split()
        if len(temp) != 3:  # if the line has more than 3 elements, raise an exception
            raise BadLine("Error: Badline on the input file on line: " + str(x+1))
        fullname = temp[0] + ' ' + temp[1]  # concat the first 2 elems to get the full name
        if fullname not in dict:  # verify if the name is already in the dict, if not -> append it; if yes -> add up
            dict[fullname] = float(temp[2])
        else:
            dict[fullname] += float(temp[2])
except FileEmpty as fe:
    print(fe)
    exit(1)
except BadLine as bl:
    print(bl)
    exit(2)
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)
print('\n')
for key in sorted(dict.keys()):
    print(key, dict[key])
