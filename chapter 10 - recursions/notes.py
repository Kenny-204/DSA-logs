def countdown(number):
    if number == 0:
        return
    print(number)
    countdown(number - 1)


# print(countdown(10))


def factorial(number):
    if number == 0 or number == 1:
        return 1
    return number * factorial(number - 1)


print(factorial(4))
