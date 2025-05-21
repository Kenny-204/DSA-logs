string = "  hello  world  "


def reverse_word_in_string(string):
    return ' '.join(string.split()[::-1])
    

print(reverse_word_in_string(string))
