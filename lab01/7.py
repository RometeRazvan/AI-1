def kth_biggest(number_list, k):
    number_list.sort()
    if len(number_list) < k:
        return -1
    return number_list[-k]


assert (kth_biggest([7, 4, 6, 3, 9, 1], 1) == 9)
assert (kth_biggest([7, 4, 6, 3, 9, 1], 2) == 7)
assert (kth_biggest([7, 4, 6, 3, 9, 1], 3) == 6)
assert (kth_biggest([7, 4, 6, 3, 9, 1], 4) == 4)
assert (kth_biggest([7, 4, 6, 3, 9, 1], 5) == 3)
assert (kth_biggest([7, 4, 6, 3, 9, 1], 6) == 1)
