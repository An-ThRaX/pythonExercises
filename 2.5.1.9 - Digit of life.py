def digit_of_life(date):
    total = 0
    length = len(str(total))
    for digit in date:
        total += int(digit)
    if length > 1:
        for digit in date:
            total += int(digit)
    return total


birth_date = input('Please write your date in format "YYYYMMDD" or any other similar: ')
print(digit_of_life(birth_date))
