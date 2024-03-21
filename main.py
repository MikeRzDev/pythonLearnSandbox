from control_structures import *
from functions import *


def menu():
    selection: str = ""

    while True:
        print("""**** Python Fundamentals ****
            1. Control Structures
            2. Range
            3. Function
            4. 
            4. Returning Function""")
        selection = input("your selection (anything else will end the program): ")
        if selection == '1':
            control_structure_example()
        elif selection == '2':
            range_example()
        elif selection == '3':
            my_function()
        elif selection == '4':
            my_int_function_example()
        else:
            break
        print("\n")


if __name__ == '__main__':
    menu()
