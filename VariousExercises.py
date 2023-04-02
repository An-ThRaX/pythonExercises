# Write a generator function that yields the first n numbers of the Fibonacci sequence.
def fibo(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


# Test
# for i in fibo(15):
#     print(i)


# Write a generator function that takes a list of integers as input and yields only the even numbers.
def even(lst):
    for n in lst:
        if n % 2 == 0:
            yield n


# Test
# for i in even([x for x in range(20)]):
#     print(i)


# Write a generator function that takes a string as input and yields each word in the string.
def words_in_strings(string):
    for word in string.split():
        yield word


# Test
# for i in words_in_strings('It is my pleasure to meet you!'):
#     print(i)

# Write a generator function that takes a list of integers as input and yields the running total of the numbers.
def running_total(numbers):
    total = 0
    for i in numbers:
        total += i
        yield total


# Test
# for total in running_total([x for x in range(10)]):
#     print(total)

# Write a generator function that takes two lists of integers as input and yields the pairwise sums of
# the numbers in the two lists.

def pair_sum(lst1, lst2):
    pair_sum = 0
    for i, j in lst1, lst2:
        pair_sum = lst1[i] + lst2[j]
        yield pair_sum


# Test
lst1 = [x for x in range(0, 6)]
lst2 = [x for x in range(6, 11)]
for total in pair_sum(lst1, lst2):
    print(total)


# Write a convertor for decimals to binary
def decToBin(num):
    binary = []
    while num > 0:
        a = int(num % 2)
        binary.append(a)
        num = (num - a) / 2
    string = ''
    for j in binary[::-1]:
        string += str(j)
    return string


for i in range(1, 101):
    print(f'{i}: {decToBin(i)}')



