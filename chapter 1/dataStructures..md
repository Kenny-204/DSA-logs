# Chapter one of Common Sense Guide to Data structures

This chapter talked about data structures and why we need them partcularly about arrays and array based sets
Each data structure has four main operations in which they are described, which are,

- reading
- searching
- insertion
- deletion

## Arrays

Arrays are a data structure in which the computer assigns side by side memory locations together
arrays are zero based (i.e their positions start from zero)
using an example of an array ['itemA','itemB','itemC','itemD','ItemE']

### Reading in an Array

The computer knows the location of all the memory address, so when creating an array the computer notes the first memory address and the size of the array, then when we want to read a particular position from that array i.e array.at(2) (array at position 2)

- First the computer add that number to the memory address of its first element, this gives the computer the memory address of the position we are looking for, then the computer simply reads the value from that array

so regardless of the size of the array, it always takes one step to read from a particular position

### Searching in an Array

Now, Although the computer knows the location of all memory addresses, the computer does not know its content, so when we want to find an item from an array e.g looking for 'itemC' from our example array

- The compute first reads the value of the first position of the array (i.e array.at(0)), it sees 'ItemA' so it goes to the next position (i.e array.at(1)) till it gets to the third position (array.at(2)) and finds 'itemC'

so in this case it takes three operations (i.e reads first,second then third)

but if we had an array of 100 elements and we were looking for the 100th element, it would then take 100 steps to find the item

### Insertion in an Array

For insertion there are three cases

- Insertion at the end of the array
- Insertion at the middle
- Insertion at the beginning

So insertion at the beginning, the computer adds the new item to the end of the array
This takes one step

Insertion at the middle, the computer first adds a new element at the end of the array, then starts shifting all the items to the right till it gets to the position where we want to insert something then it inserts it 



Insertion at the beginning, its the same idea as insertion at the middle but this has to shift all the items of the array to the right

### Deletion
For deletion, when the position of the item to be deleted is found, the array deletes the item, which creates an empty space, the computer then shifts all the remaining elements to the left to fill up the space


