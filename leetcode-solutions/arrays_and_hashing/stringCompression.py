# chars = ["a", "a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "c", "c", "c"]
# chars = ["a"]

chars = [
    "a",
    "b",
    "b",
    "c",
]


def string_compression(chars):
    first = 0
    second = 1
    count = 1
    num = 0

    def formatCount(count):
        if count < 10:
            return [str(count)]
        else:
            return list(str(count))

    if len(chars) == 1:
        return 1

    while second < len(chars):
        if chars[first] == chars[second]:
            count += 1
            chars.pop(second)
        elif chars[first] != chars[second]:
            num += count
            if count > 1:
                chars[second:second] = [*formatCount(count)]
                if count < 10:
                    first += 2
                    second += 2
                else:
                    first += 3
                    second += 3
            else:
                first += 1
                second += 1
            count = 1
    num += count
    if count > 1:
        chars.extend([*formatCount(count)])
    return num


print(string_compression(chars))

#######################################
# first = 0
# second = 1
# count = 1
# num = 0

# def formatCount(count):
#     if count < 10:
#         return [str(count)]
#     else:
#         return list(str(count))

# if len(chars) == 1:
#     return 1

# while second < len(chars):
#     if chars[first] == chars[second]:
#         # num += 1
#         count += 1
#         chars.pop(second)
#     elif chars[first] != chars[second]:
#         num += count
#         if count > 1:
#             chars[second:second] = [*formatCount(count)]
#             count = 1
#             if chars[second + 1].isalpha():
#                 first += 2
#                 second += 2
#             else:
#                 first += 3
#                 second += 3
#         else:
#             first += 1
#             second += 1

# num += count
# chars.append(*formatCount(count))
# return num


####################
#       output = []
#     first = 0
#     second = 1
#     count = 1

#     def formatCount(count):
#         if count < 10:
#             return [str(count)]
#         else:
#             return list(str(count))

#     if len(chars) == 1:
#         return chars
#     while second < len(chars):
#         if len(output) == 0:
#             output.append(chars[first])
#         if len(output) > 0 and output[-1] != chars[first]:
#             output.append(chars[first])

#         if chars[first] == chars[second]:
#             count += 1
#             second += 1
#         elif chars[first] != chars[second]:
#             if count > 1:
#                 output += formatCount(count)
#             count = 1
#             first = second
#             second += 1

#     output += formatCount(count)
#     chars = output
#     return chars
