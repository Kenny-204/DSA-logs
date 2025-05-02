#selection sort

array = [4,2,7,1,3]

def selection_sort(array):
    for i in range(len(array)):
        low = 0
        for j in range(len(array)):
            if array[j] < array[low]:
                low = j
            array[0],array[low] = array[low],array[0]
    return array

print(selection_sort(array))
print(array)    
    