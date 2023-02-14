def read_int(prompt, minimum, maximum):  # prompt will be the text chosen by the user when the function is called
    doIt = True  # flag to hold the loop active
    while doIt:
        try:
            user_input = int(input(prompt))  # input a number and check if it is int
            if user_input in range(minimum, maximum+1):  # verify if the input is within the min and max boundaries
                doIt = False  # if is in range, flag changes and loop is terminated
                return user_input  # the function returns the number to be processed
            else:
                raise AssertionError  # if not in range, assertion is failed and runs to the exception
        except ValueError:  # if the user input is not int, it will reach here and return to the input
            print("Error: wrong input ")
        except AssertionError:
            print("Error: the value is not within permitted range ({}..{}) ".format(minimum, maximum))
            #  it will inform the user that the input is not in the desired range
        except:
            doIt = True  # in case anything else happens, it will restart the loop


v = read_int("Enter a number from -10 to 10: ", -10, 10)
print("The number is:", v)
