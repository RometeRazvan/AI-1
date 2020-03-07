def produs_scalar(first_list, second_list):
    produs = 0
    for i in range(len(first_list)):
        produs += first_list[i] * second_list[i]
    return produs


assert (produs_scalar([1, 0, 2, 0, 3], [1, 2, 0, 3, 1]) == 4)
assert (produs_scalar([1, 0, 2, 0, 1], [1, 2, 0, 3, 1]) == 2)
assert (produs_scalar([1, 2, 2, 0, 3], [1, 2, 0, 3, 1]) == 8)
assert (produs_scalar([1, 0, 2, 5, 3], [1, 2, 0, 3, 1]) == 19)

