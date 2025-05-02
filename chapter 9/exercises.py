# 1. queue
# 2. 4
# 3. 2
# 4.


class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def read(self):
        return self.data[-1]

    def size(self):
        return len(self.data)


stack = Stack()

string = "abcde"


def reverse_a_string_with_stacks(string):
    output = ""
    for char in string:
        stack.push(char)

    for i in range(stack.size()):
        last = stack.pop()
        output += last
    return output


print(reverse_a_string_with_stacks(string))
