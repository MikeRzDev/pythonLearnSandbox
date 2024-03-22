def array_operations():
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = [4, 5, 6, 7]

    # Concatenate
    result = a + c
    print(f'concatenate {result}')

    # Comparison
    result = a == b
    print(f'a is equal to b {result}')

    result = a == c
    print(f'a is equal to c {result}')

    # Add
    a += [55]
    print(f'add iterable {a}')

    # Add
    b.append(99)
    print(f'add value {b}')


def tuple_example():
    additional_info_tuple = 'Oxford University', 'Math Faculty'
    person_tuple = 'James', 'Gordon', 33
    student_with_grades_tuple = 'Mark', 'Waters', [3, 2.6, 3.8]
    print(f'the name is {person_tuple[0]}')
    print(f'the last name is {person_tuple[1]}')
    print(f'the age is {person_tuple[2]}')

    # adding values to tuple
    person_tuple += ('9345 Rodewich Drive', 'London')
    print(f'the person info is {person_tuple}')

    # concatenating tuples
    result = person_tuple + additional_info_tuple
    print(f'the new person info is {result}')

    student_with_grades_tuple[2][1] += 1.4
    print(f'the person with grades is {student_with_grades_tuple}')

    # unpack tuples
    university, faculty = additional_info_tuple
    print(f'the faculty info is {university}, {faculty}')


def regular_for():
    number_list = [3, 5, 12, 3, 5, 12, 3, 12]
    for i in range(len(number_list)):
        print(f'{i}: {number_list[i]}')
