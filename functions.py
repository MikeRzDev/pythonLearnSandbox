def default_param_example(param='defaultValue'):
    print(f'my param is {param}')


def returning_function(seed=1) -> int:
    return seed


def returning_function_example():
    print(f'the return value is : {returning_function()}')


def named_param_example():
    default_param_example(param='anotherValue')
