#1. return if low > high
#2. stack overflow
#3. if high = 0 return 0
#4. 

array  = [1,2,3,[4,5,6],7,[8,[9,10,11,[12,13,14]]],[15,16,17,18,19,[20,21,22,[23,24,25,[26,27,29]],30,31],32],33]

def print_numbers(array):
    for value in array:
        if isinstance(value,list):
            print_numbers(value)
        else :print(value)
    
print_numbers(array)

## would come back to this 

# dont really get 