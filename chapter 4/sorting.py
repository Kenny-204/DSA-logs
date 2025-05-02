# Bubble sort

array = [4,2,7,1,3]

def swap(first,second):
    temp = 0
    temp =array[second]
    array[second] = array[first]
    array[first] = temp
    print(array)
    
def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            if array[j] >array[j+1]:
                array[j] ,array[j+1] = array[j+1] ,array[j]
    return array
                
            
    
    
# print(bubble_sort(array))

###################################################################
## Exercise

def greatest_number(array):
    for i in array:
        is_i_val_the_greatest = True
        for j in array:
            if j>i:
                is_i_val_the_greatest = False
        if is_i_val_the_greatest : return i

# array = [4,2,7,1,3]
def greatest_number2(array):
    high = 0
    for i in range(len(array)):
        if array[i] > high:
            high = array[i]
    return high

print(greatest_number2(array))