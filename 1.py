# -*- coding: utf-8 -*-


def sum_of_mulitiples(multiples_numbers, below_number):
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
    """
    multiples_numbers = set(multiples_numbers)
    flags = [0] * below_number
    for index in range(1, len(flags)):
        if is_multiplies(multiples_numbers, index):
            flags[index - 1] = 1
    return sum_of_flags(flags)


def sum_of_flags(flags):
    result = 0
    for index, number in enumerate(flags):
        if number == 1:
            result += (index + 1)
    return result


def is_multiplies(multiples_numbers, number):
    return any(number % item == 0 for item in multiples_numbers)


print sum_of_mulitiples([3, 5], 1000)
