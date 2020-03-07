def dec2bin(number):
    binary_string = ''
    while number >= 1:
        number, rem = divmod(number, 2)
        binary_string = str(rem)+binary_string
    return binary_string


def to_binary(n):
    binary_list = []
    for i in range(1, n + 1):
        binary_list.append(dec2bin(i))
    return binary_list


assert (to_binary(3) == ['1', '10', '11'])
assert (to_binary(4) == ['1', '10', '11', '100'])
assert (to_binary(7) == ['1', '10', '11', '100', '101', '110', '111'])
assert (to_binary(2) == ['1', '10'])
