######################################
############ STACK ##################


class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        self.data.pop()

    def read(self):
        self.data[-1]


############## LINTER ###############
# text = "(var x = [1,2,3)]"
text = "({()(){}(hi[ji{dj}]))"


def linter(text):
    stack = []

    opening_brackets = {"(": ")", "{": "}", "[": "]"}
    closing_brackets = {")": True, "}": True, "]": True}

    for char in text:
        if char in opening_brackets:
            stack.append(char)
        if char in closing_brackets:
            if not stack:
                return "Error"
            prev_entry = stack.pop()
            if opening_brackets.get(prev_entry) != char:
                return "Error"
    return "no error"


print(linter(text))


#############################
########### QUEUES ##########


class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, element):
        self.data.append(element)

    def dequeue(self):
        self.data.pop(0)

    def read(self):
        self.data[0]
        
        
