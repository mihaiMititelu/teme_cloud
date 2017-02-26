import random
import third_api


def name_and_number():
    first_name = third_api.ask_for('names', random.randint(1, 3))
    second_name = third_api.ask_for('names', random.randint(1, 3))
    first_number = third_api.ask_for('numbers', random.randint(1, 3))
    second_number = third_api.ask_for('numbers', random.randint(1, 3))

    print(first_name, 'has received', first_number)
    print(second_name, 'has received', second_number)
    print('Their sum is', int(first_number) + int(second_number))


name_and_number()
