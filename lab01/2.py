from math import sqrt

def euclidean_distance(a, b):
    answer = 0
    for i in range(len(a)):
        answer += abs(a[i] - b[i])**2
    return sqrt(answer)


assert (abs(euclidean_distance([1, 5], [4, 1]) - 5.0) <= 0.0001)
assert (abs(euclidean_distance([1, 4], [4, 1]) - 4.2426) <= 0.0001)
assert (abs(euclidean_distance([10, 4], [4, 1]) - 6.7082) <= 0.0001)
assert (abs(euclidean_distance([10, 4], [4, 20]) - 17.088) <= 0.0001)
