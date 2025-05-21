# def pascal_triangle(num):
#     output = []
#     if num == 1:
#         output.append([1])
#         return output
#     if num == 2:
#         prev = pascal_triangle(1)
#         prev.append([1, 1])
#         return prev
#     prev = pascal_triangle(num - 1)
#     latest_entry = prev[-1]
#     new = [1]
#     for i in range(len(latest_entry)):
#         if i == len(latest_entry) - 1:
#             new.append(1)
#         else:
#             new.append(latest_entry[i] + latest_entry[i + 1])
#     prev.append(new)
#     return prev
# print(pascal_triangle(10))

################# CORRECTION ###################3
def pascal_triangle(num):
    output = []
    if num == 1:
        output.append([1])
        return output
    new = [1]
    prev = pascal_triangle(num - 1)
    for i in range(len(prev[-1])):
        if i == len(prev[-1]) - 1:
            new.append(1)
        else:
            new.append(prev[-1][i] + prev[-1][i + 1])
    prev.append(new)
    return prev


print(pascal_triangle(5))
