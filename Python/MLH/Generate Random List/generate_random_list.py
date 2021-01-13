from random import randint


def generate_random_list(length):
    result = [randint(0, 100) for i in range(length)]
    return result

if __name__ == '__main__':
    print(generate_random_list(10))
