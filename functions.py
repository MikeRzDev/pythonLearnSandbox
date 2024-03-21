def my_function(param='defaultValue'):
    print(f'my param is {param}')


def my_int_function(seed=1) -> int:
    return seed


def my_int_function_example():
    print(f'the return value is : {my_int_function()}')


def my_function_example():
    my_function(param='anotherValue')
