### Recursive categories

## Repeatedly execute

a = [1, 2, 3, 4, 5]


def double_array(a, i=0):
    a[i] *= 2
    double_array(a, i + 1)


## Calculations


def factorial(number):
    if number == 1:
        return 1
    return number * factorial(number - 1)


# print(factorial(4))


def array_sum(a):
    if len(a) == 1:
        return a[0]
    return a[0] + array_sum(a[1:])


# print(array_sum(a))

string = "abcde"


def string_reversal(str):
    if len(str) == 1:
        return str[0]
    return string_reversal(str[1:]) + str[0]


# print(string_reversal(string))

stringx = "axbxcxd"


def count_x(str):
    if len(str) == 0:
        return 0

    if str[0] == "x":
        return 1 + count_x(str[1:])
    else:
        return count_x(str[1:])
    # else:
    #     if str[0] == 'x':
    #         return 1
    #     else: return 0


# print(count_x(stringx))


def staircase_problem(num):
    if num < 0:
        return 0
    if num == 0 or num == 1:
        return 1
    return (
        staircase_problem(num - 1)
        + staircase_problem(num - 2)
        + staircase_problem(num - 3)
    )


print(staircase_problem(7))


def anagram(string):
    if len(string) == 1:
        return [string]
    collection = []
    for value in anagram(string[1:]):
        for i in range(len(value) + 1):
            new_word = value[:i] + string[0] + value[i:]
            collection.append(new_word)
    return collection


print(anagram("abc"))
