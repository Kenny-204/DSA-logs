import math

# Linear search


# def linear_search(array,item):
#     for i in range(len(array)):
#         if array[i] == item :
#             return i
#     return
# print(linear_search(array,9))


# Binary search
array = [1,3,4,5,6]

def binary_search(array,item):
    left = 0
    right = len(array) -1
    
    while left < right:
        middle = math.floor((left+right)/2)
        if array[middle] == item:
            return middle
        if array[middle] > item:
            right = middle 
        if array[middle] < item:
            left = middle
    return -1
    
        
print(binary_search(array,3))