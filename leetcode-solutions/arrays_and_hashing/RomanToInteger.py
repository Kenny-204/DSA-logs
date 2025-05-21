dictionary = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

s = "VII"


def roman_to_integer(roman):
    output = 0
    i = 0
    while i < len(roman):

        if i == len(roman):
            return output

        if i == len(roman) - 1:
            output += dictionary.get(roman[i])
            return output
        else:

            if dictionary.get(roman[i]) < dictionary.get(roman[i + 1]):
                output += dictionary.get(roman[i + 1]) - dictionary.get(roman[i])
                print(output, i)
                if i == len(roman) - 2:
                    return output
                i += 2

            if dictionary.get(roman[i]) >= dictionary.get(roman[i + 1]):
                output += dictionary.get(roman[i])
                i += 1
                print(output, i)

    return output


print(roman_to_integer(s))
#     # i+=2
# for i in range(len(roman)):
#     if i == len(roman)-1:
#         output += dictionary.get(roman[i])
#     else:

#         if dictionary.get(roman[i]) < dictionary.get(roman[i + 1]):
#             output += dictionary.get(roman[i + 1]) - dictionary.get(roman[i])
#             print(output,i)
#             i+=2
#         if dictionary.get(roman[i]) >= dictionary.get(roman[i + 1]):
#             output +=dictionary.get(roman[i])
#             print(output,i)
#     # i+=2
