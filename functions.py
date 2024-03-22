some_value = 99


def default_param_example(param='defaultValue'):
    print(f'my param is {param}')


def __returning_function(seed=1) -> int:
    return seed


def returning_function_example():
    print(f'the return value is : {__returning_function()}')


# Keyword arguments
def named_param_example():
    default_param_example(param='anotherValue')


def __vararg_function(*items: int) -> int:
    total = 0
    for item in items:
        total += item
    return total


def __kwargs_function(**kwargs):
    for key, value in kwargs.items():
        print(f"Key: {key}, Value: {value}")


# Varargs = arbitrary arguments
def vargarg_example():
    print("** integer sum **")
    total = __vararg_function(4, 54, 1, 6, 7, 12, 34, 123, 3)
    print(f"the total is: {total}")


def global_variables_cant_be_modified_in_functions():
    some_value = 3
    print(f'the value is {some_value}')


def global_variables_can_be_modified_using_global_in_functions():
    global some_value
    some_value = 55
    print(f'the value is {some_value}')
