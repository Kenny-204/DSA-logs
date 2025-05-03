# 1.

array = ["ab", "c", "def", "ghij"]


def total_no_characters(array):
    if len(array) == 1:
        return len(array[0])
    return len(array[0]) + total_no_characters(array[1:])


# print(total_no_characters(array))

# 2.
array2 = [1, 2, 3, 4, 5]


def return_even(array):
    if len(array) == 1:
        if array[0] % 2 == 0:
            return array
        else:
            return []

    if array[0] % 2 == 0:

        return [array[0]] + return_even(array[1:])
    else:
        remains = return_even(array[1:])
        return remains


# print(return_even(array2))


# 3.
def triangular_number(num):
    if num == 1:
        return 1

    return num + triangular_number(num - 1)


# print(triangular_number(7))

# 4.

string = "abcdefghijklmnopqrstuvwxyz"


def index_of_x(string, index=0):
    if string[0] == "x":
        return index
    return index_of_x(string[1:], index + 1)


# print(index_of_x(string))

# 5.


def unique_paths(row, column):
    return unique_paths(row - 1, column - 1)
