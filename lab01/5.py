def double_number(ar):
    numbers = dict()
    for number in ar:
        if number in numbers and numbers[number] == 1:
            return number
        else:
            numbers[number] = 1
    return -1


assert (double_number([1, 2, 3, 4, 2]) == 2)
assert (double_number([1, 2, 3, 4, 1]) == 1)
assert (double_number([1, 2, 3, 4, 3]) == 3)
assert (double_number([1, 2, 3, 4, 4]) == 4)
assert (double_number([1, 2, 3, 4, 5]) == -1)
