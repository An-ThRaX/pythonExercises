# We need a class able to count seconds. Easy? Not as much as you may think as we're going to have some specific expectations.

# Read them carefully as the class you're about write will be used to launch rockets carrying international missions to Mars.
# It's a great responsibility. We're counting on you!
#
# Your class will be called Timer. Its constructor accepts three arguments representing hours (a value from range [0..23]
# - we will be using the military time), minutes (from range [0..59]) and seconds (from range [0..59]).
#
# Zero is the default value for all of the above parameters. There is no need to perform any validation checks.
#
# The class itself should provide the following facilities:
#
# objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the
# following form: "hh:mm:ss", with leading zeros added when any of the values is less than 10;
# the class should be equipped with parameterless methods called next_second() and previous_second(), incrementing the time
# stored inside objects by +1/-1 second respectively.
import random


def format_digit(digit):
    if digit < 10:  # if the digit is under 10, format the return so it will print with a "0" in front of the digit
        return f"0{digit}"  # the format function returns str
    else:
        return str(digit)


class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):  # define the constructor and it's parameters
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    def __str__(self):  # write a function to print the result using the below defined formating function
        return f"{format_digit(self._hours)}:{format_digit(self._minutes)}:{format_digit(self._seconds)}"

    def next_second(self):
        self._seconds += 1
        if self._seconds == 60:  # if seconds reach 60, replace with 0 and increment minutes
            self._seconds = 0
            self._minutes += 1
            if self._minutes == 60:  # if minutes reach 60, replace with 0 and increment hours
                self._minutes = 0
                self._hours += 1
                if self._hours == 24:  # if hours reach 24, replace with 0
                    self._hours = 0

    def prev_second(self):
        self._seconds -= 1
        if self._seconds == -1:  # if seconds reach -1, replace with 59 and decrement minutes
            self._seconds = 59
            self._minutes -= 1
            if self._minutes == -1:  # if minutes reach -1, replace with 59 and decrement hours
                self._minutes = 59
                self._hours -= 1
                if self._hours == -1:  # if hours reach -1, replace with 23
                    self._hours = 23


for i in range(100):  # testing the class above
    h = random.randint(1, 24)
    m = random.randint(1, 60)
    s = random.randint(1, 60)
    timer = Timer(h, m, s)
    print('Initial time: ', timer)
    timer.next_second()
    print('Adding one second: ', timer)
    timer.prev_second()
    print('Removing one second: ', timer, end='\n\n')


