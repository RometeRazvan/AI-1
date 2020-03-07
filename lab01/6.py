def most_common(number_list):
    number_dict = dict()
    for number in number_list:
        if number in number_dict:
            number_dict[number] += 1
        else:
            number_dict[number] = 1

    max_number = [-1, -1]
    for number in number_dict:
        if max_number == [-1, -1]:
            max_number = [number, number_dict[number]]
        if number_dict[number] > max_number[1]:
            max_number = [number, number_dict[number]]
    if max_number[1] > len(number_list)/2:
        return max_number
    return [-1, -1]


assert (most_common([2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]) == [2, 6])
assert (most_common([8, 7, 5, 2, 3, 1, 2]) == [-1, -1])
