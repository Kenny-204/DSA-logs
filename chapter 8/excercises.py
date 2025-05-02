x = [1, 2, 3, 4, 5]
y = [0, 2, 4, 6, 8]


def intersection_of_two_arrays(x, y):
    hashmap = {}
    output = []

    if len(x) >= len(y):
        larger_array = x
        smaller_array = y
    else:
        larger_array = y
        smaller_array = x

    for i in range(len(larger_array)):
        hashmap[larger_array[i]] = True
    for i in range(len(smaller_array)):
        if smaller_array[i] in hashmap:
            output.append(smaller_array[i])
    print(output)


# intersection_of_two_arrays(x,y)


############## CORRECTION #############
def intersection_of_two_arrays(x, y):
    hashmap = {}
    output = []

    for i in range(len(x)):
        hashmap[x[i]] = True
    for i in range(len(y)):
        if y[i] in hashmap:
            output.append(y[i])
    return output


# print(intersection_of_two_arrays(x,y))

array = ["a", "b", "c", "d", "c", "e", "f"]


def return_duplicate(array):
    map = {}

    for i in range(len(array)):
        if array[i] in map:
            return array[i]
        map[array[i]] = True


# print(return_duplicate(array))

str = "The quick brown box jumped over the lazy dog"


def return_missing_letter_from_alphabet(str):
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    map = {}

    for i in range(len(str)):
        if str[i] in map:
            map[str[i]] = map.get(str[i]) + 1
        map[str[i]] = 0
    for i in range(len(letters)):
        if letters[i] not in map:
            return letters[i]


# print(return_missing_letter_from_alphabet(str))


############## CORRECTION #############
def return_missing_letter_from_alphabet1(str):
    letters = "abcdefghijklmnopqrstuvwxyz"
    map = {}

    str = str.lower()

    for char in str:
        if char.isalpha():
            map[char] = True

    for letter in letters:
        if letter not in map:
            return letter


print(return_missing_letter_from_alphabet1(str))

string = "minimum"


def first_non_duplicated_character(string):
    map = {}
    for i in range(len(string)):
        if string[i] in map:
            map[string[i]] += 1
        else:
            map[string[i]] = 1
    for i in range(len(map)):
        if map[string[i]] == 1:
            return string[i]


# print(first_non_duplicated_character(string))

############## CORRECTION #############


def first_non_duplicated_character(string):
    map = {}
    for letter in string:
        map[letter] = map.get(letter, 0) + 1
    for letter in string:
        if map[letter] == 1:
            return letter

    return map


print(first_non_duplicated_character(string))
