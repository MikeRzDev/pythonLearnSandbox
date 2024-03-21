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


# Varargs = arbitrary arguments
def vargarg_example():
    print("** integer sum **")
    total = __vararg_function(4, 54, 1, 6, 7, 12, 34, 123, 3)
    print(f"the total is: {total}")
