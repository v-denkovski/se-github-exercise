lst = [13, 6, 5, 5, 10]


def sum_list(numbers):
    total = 0
    for item in numbers:
        total += item
    return total


print(sum_list(lst))
