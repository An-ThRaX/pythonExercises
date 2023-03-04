# # 1. Write a Python program to import a built-in array module and display the namespace of the said module.
#
# import array
#
# for name in array.__dict__:
#     print(name)
#
# # 2. Write a Python program to create a class and display the namespace of that class.
#
#
# class Sample:
#     pass
#
#
# for name in Sample.__dict__:
#     print(name)
#
# # 3. Write a Python program to create an instance of a specified class and
# #
# # 1.   List item
# # 2.   List item
# #
# # display the namespace of the said instance.
#
#
# class Sample:
#     def __init__(self, student_id, student_name, class_name):
#         self.student_id = student_id
#         self.student_name = student_name
#         self.class_name = class_name
#
#
# student = Sample('V12', 'Marcel', 'V')
# print(
#     student.__dict__)   # __dict__ attribute displays the names and values of all the instance variables;
#                         # NOTE: does not display the methods or class variables
#
#
# # 4. 'builtins' module provides direct access to all 'built-in' identifiers of Python.
# # Write a Python program that imports the abs() function using the builtins module,
# # displays the documentation of the abs() function and finds the absolute value of -155.
#
#
# import builtins
#
# help(builtins.abs)
# print("Absolute value of -155 is:", builtins.abs(-155))
#
#
# from builtins import abs
# help(abs)
# print("Absolute value of -155 is:", abs(-155))
#
# # 5. Define a Python function student(). Using function attributes display the names of all arguments.
#
#
# def student(name):
#     return f'name: {name}'
#
#
# print(student('Marcela'))
#
#
# # 6. Write a Python function student_data () that will print the ID of a student (student_id).
# # If the user passes an argument student_name or student_class the function will print the student name and class.
#
#
# def student_data(student_id, student_name = None, student_class = None):
#     print(f"Student id: {student_id}")
#     if student_name is not None:
#         print(f"Student name: {student_name}")
#     if student_class is not None:
#         print(f"Student class: {student_class}")
#
#
# student_data(student_id='V12')
# student_data(student_id='V12', student_name='Jane Doe')
# student_data(student_id='V12', student_name='Jane Doe', student_class='V')
#
#
# # 7. Write a simple Python class named Student and display its type. Also, display the __dict__ attribute keys
# # and the value of the __module__ attribute of the Student class.
#
#
# class Student():
#     def __init__(self, student_id, student_name, student_class):
#         self.student_id = student_id
#         self.student_name = student_name
#         self.student_class = student_class
#
#     def student_info(self):
#         return f'Student Id: {self.student_id}\nStudent name: {self.student_name}\nStudent class: {self.student_class}'
#
#
# print(f'The type of the Student class is: {type(Student)}')
# print(f'The keys of the Student class are: {Student.__dict__.keys()}')
# print(f'The value of the module attribute of Student class is: {Student.__module__}')
#
#
# # 8. Write a Python program to create two empty classes, Student and Marks. Now create some instances and check
# # whether they are instances of the said classes or not. Also, check whether the said classes are subclasses of the
# # built-in object class or not.
#
#
# class Student:
#     pass
#
#
# class Mark:
#     pass
#
#
# student = Student()
# mark = Mark()
#
# print(f'Is student an object of the Student Class? ', isinstance(student, Student))
# print(f'Is student an object of the Mark Class? ', isinstance(student, Mark))
# print(f'Is Mark an object of the Mark Class? ', isinstance(mark, Mark))
# print(f'Is Mark an object of the Student Class? ', isinstance(mark, Student))
# print('\nChecking whether the said classes are subclasses of the built-in Object class or not.')
# print(f'Is Student a subclass of the Object Class? ', issubclass(Student, object))
# print(f'Is Mark a subclass of the Object Class? ', issubclass(Mark, object))
#
#
# # 9. Write a Python class named Student with two attributes student_name, marks. Modify the attribute values
# # of the said class and print the original and modified values of the said attributes.
#
#
# class Student:
#     student_name = 'Jon Doe'
#     marks = 93
#
#
# student = Student()
# print('Student name: ', getattr(student, 'student_name'))
# print('Student marks: ', getattr(student, 'marks'))
# setattr(Student, "student_name", "Dave Doe")
# setattr(Student, "marks", 89)
# print('\nStudent name: ', getattr(student, 'student_name'))
# print(f"Student marks: {getattr(student, 'marks')}")
#
#
# # 10. Write a Python class named Student with two attributes student_id, student_name. Add a new attribute
# # student_class and display the entire attribute and the values of the class. Now remove the student_name attribute
# # and display the entire attribute with values.
#
#
# class Student:
#     student_id = 'V12'
#     student_name = 'MJ'
#
#
# print("Original attributes and their values: ")
# for attr, value in Student.__dict__.items():
#     if not attr.startswith('_'):
#         print(f"{attr} -> {value}")
# print('\nAfter adding a new attribute: ')
# Student.student_class = 'V'
# for attr, value in Student.__dict__.items():
#     if not attr.startswith('_'):
#         print(f"{attr} -> {value}")
# print('\nAfter deleting an attribute: ')
# del Student.student_name
# # delattr(Student, 'student_name')
# for attr, value in Student.__dict__.items():
#     if not attr.startswith('_'):
#         print(f"{attr} -> {value}")
#
#
# # 11. Write a Python class named Student with two attributes: student_id, student_name.
# # Add a new attribute: student_class. Create a function to display all attributes and their values in the Student class.
#
#
# # class Student():
# #   student_id = 'V12'
# #   student_name = 'MJ'
#
# # Student.student_class = 'V'
#
# # def showDetails(items):
# #   for attr, value in items.__dict__:
# #     print(f"Attribute {attr} has the value {value}")
#
# class Student:
#     def __init__(self, student_id, student_name):
#         self.student_id = student_id
#         self.student_name = student_name
#         self.student_class = None
#
#     def display(self):
#         print(f'Student Id: {self.student_id}')
#         print(f'Student name: {self.student_name}')
#         if self.student_class is not None:
#             print(f'Student class: {self.student_class}')
#
#
# student1 = Student(12, 'Marcel')
# student1.display()
# print()
# student1.student_class = 'Mathematics'
# student1.display()
#
#
# # 12. Write a Python class named Student with two instances student1, student2 and assign values to the instances'
# # attributes. Print all the attributes of the student1, student2 instances with their values in the given format.
#
#
# class Student:
#     def __init__(self, student_id, student_name):
#         self.student_id = student_id
#         self.student_name = student_name
#         self.student_class = None
#
#     def print_attr(self):
#         attrs = self.__dict__
#         for key, value in attrs.items():
#             print(f"{key} -> {value}")
#
#
# student1 = Student(1, "Marcel")
# student2 = Student(2, "Marcela")
# student2.marks_language = 85
# student2.marks_science = 93
# student2.marks_math = 95
# student1.print_attr()
# student2.print_attr()
#
#
# # ## Python class, Basic application
#
# # 1. Write a Python class to convert an integer to a Roman numeral.
# # 2. Write a Python class to convert a Roman numeral to an integer.
#
# class IntToRomanConvertor:
#     def int_to_roman(self, num):
#         val = [1000, 900, 500, 400,
#                100, 90, 50, 40,
#                10, 9, 5, 4,
#                1]  # define a list with all the integers for each roman symbol
#         symb = ['M', 'CM', 'D', 'CD',
#                 "C", "XC", "L", "XL",
#                 "X", "IX", "V", "IV",
#                 "I"]  # define a list with all the roman symbols
#         roman_num = ''  # create the string were the roman will be saved
#         stepper = 0  # create a stepping agent - for the val list
#         while num > 0:  # while the argument's values is over 0 do below
#             for j in range(num // val[stepper]):  # find the floor division betweer the arg num and
#                 # the representative of the val list
#                 # if a floor division is positive do below
#
#                 roman_num += symb[stepper]
#                 num -= val[stepper]
#             stepper += 1  # if a floor division is ZERO, increase the stepper
#             # untill we can do the operations inside the above for function
#         return roman_num  # eventually, the number builds up
#
#
# class RomanToIntConvertor:
#     def roman_to_int(self, num):
#         rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
#                    'M': 1000}  # create a dictionary with each roman symbol and it's digit referal
#         int_val = 0  # initialise the digit number to zero
#         for i in range(len(num)):  # itterate depending of the roman number's length
#             if i > 0 and rom_val[num[i]] > rom_val[
#                 num[i - 1]]:  # if i is under zero -> add the roman's value to the digit: row 34
#                 # if i is over zero and roman[i] is higher than roman[i-1]
#                 int_val += rom_val[num[i]] - 2 * rom_val[
#                     num[i - 1]]  # add to the digit the roman[i] and substract 2 * roman[i-1]
#             else:  # in case the if statement is again false ( the comparison fails), than add the roman[i] to the digit
#                 int_val += rom_val[num[i]]
#         return int_val  # eventually, the digit builds up
#
#
# # test
# import random
#
# for i in range(100):
#     num = random.randint(1, 5002)
#     roman = IntToRomanConvertor().int_to_roman(num)
#     digit = RomanToIntConvertor().roman_to_int(roman)
#     print(f"{i + 1}. Integer to Roman: {num} -> {roman}\
#         \n{i + 1}' Roman to Integer: {roman} -> {digit}\n")
#
#
# # 3. Write a Python class to check the validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These
# # brackets must be closed in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{"
# # are invalid.
#
#
# class CheckParantheses():
#     def check_paranth(self, string):
#         stack, pars = [], {"(": ")", "{": "}", "[": "]"}
#         for char in string:
#             if char in pars:
#                 stack.append(char)
#                 print(f'{char} - {stack}')
#             elif len(stack) == 0 or pars[stack.pop()] != char:
#                 return False
#         return len(stack) == 0
#
#
# # test
# print(CheckParantheses().check_paranth("()[{)}"))
#
#
# # 4. Write a Python class to get all possible unique subsets from a set of distinct integers. Go to the editor
# # Input : [4, 5, 6]
# # Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]
#
#
# class Subset():
#     def sub_set(self, sset):
#         return self.subsetsRecur([], sorted(sset))
#
#     def subsetsRecur(self, current, sset):
#         if sset:
#             return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:] )
#         return [current]
#
#
# print(Subset().sub_set([6, 5, 4]))
#
#
# # 5. Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum
# # equals a specific target number.
# # Note: There will be one solution for each input and do not use the same element twice. Go to the editor
# # Input: numbers= [10,20,10,40,50,60,70], target=50
# # Output: 2, 3

class Pair:
    def two_elements(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return lookup[target - num], i
            lookup[num] = i


print('index1 = %d, index2 = %d' % Pair().two_elements((10, 20, 10, 30, 40, 50, 60, 70), 50))
