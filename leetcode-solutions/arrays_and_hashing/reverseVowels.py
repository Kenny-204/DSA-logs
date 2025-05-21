string = "IceCream"


def reverse_vowels(string):
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    map = {}
    output = ""

    for index, letter in enumerate(string):
        if letter in vowels:
            map[index] = letter

    reversed_values = list(reversed(map.values()))
    reversed_map = {k: v for k, v in zip(map.keys(), reversed_values)}
    list_string = list(string)

    for key in reversed_map:
        list_string[key] = reversed_map.get(key)

    return output.join(list_string)


print(reverse_vowels(string))
