from functools import reduce


def process_numbers(numbers):
    even_posi_numbers = list(filter(lambda x: x > 0 and x % 2 == 0, numbers))
    squares_numbers = list(map(lambda x: x ** 2, even_posi_numbers))
    return reduce(lambda x, y: x + y, squares_numbers)


numbers = [1, 2, 3, 4, 5, -2, -4, 11, -9, 7, -100_999]

print(process_numbers(numbers))
