class WeekDayError(Exception):
    pass


class Weeker:
    __names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        try:
            self.__current = Weeker.__names.index(day)  # in __current we store the index of the given day
            # .index function returns the index at which it finds the given day
        except ValueError:
            raise WeekDayError

    def __str__(self):
        return Weeker.__names[self.__current]  # from __names we return the day from the __current index

    def add_days(self, n):
        self.__current = (self.__current + n) % 7  # rewrite __current based on how many days we want to add

    def subtract_days(self, n):
        self.__current = (self.__current - n) % 7  # rewrite __current based on how many days we want to substract


# test
try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
