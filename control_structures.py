def control_structure_example():
    print('Calculate mean, enter values, "end" will terminate the sequence ')
    values: list[int] = []
    while True:
        selection_string: str = input()
        if selection_string == 'end':
            break
        selection = int(selection_string)
        values.append(selection)
    total = 0
    for value in values:
        total += value
    list_count = len(values)
    mean: float = total / list_count
    print(f'the mean is {str(mean)}')


def range_example():
    step = int(input('step:'))

    for number in range(0, 10, step):
        print(number, end=' ')
