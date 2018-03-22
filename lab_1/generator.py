import random
import string


def generate(amount):
    with open('test_data.txt', 'w') as file:
        for i in range(amount):
            file.write(''.join(random.choice(
                string.ascii_letters + string.digits) for _ in range(
                random.randrange(3, 10))) + ';')


generate(100)
