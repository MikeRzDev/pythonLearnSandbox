from control_structures import *
from functions import *


def menu():
    while True:
        print("""**** Python Fundamentals ****
            1. Control Structures
            2. Range
            3. Function with Default Parms
            4. Function with Named Params
            5. Function Returning Value
            6. Function with VarArgs""")
        selection = input("your selection (anything else will end the program): ")
        if selection == '1':
            control_structure_example()
        elif selection == '2':
            range_example()
        elif selection == '3':
            default_param_example()
        elif selection == '4':
            named_param_example()
        elif selection == '5':
            returning_function_example()
        elif selection == '6':
            vargarg_example()
        else:
            break
        print("\n")


if __name__ == '__main__':
    menu()
