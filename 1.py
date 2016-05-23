# -*- coding: utf-8 -*-


def sum_of_mulitiples(multiples_numbers, below_number):
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
    """
    multiples_numbers = set(multiples_numbers)
    result = 0
    for i in range(1, below_number):
        if is_multiplies(multiples_numbers, i):
            result += i
    return result


def is_multiplies(multiples_numbers, number):
    return any(number % item == 0 for item in multiples_numbers)


print sum_of_mulitiples([3, 5], 1000)
