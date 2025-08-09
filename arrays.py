myArray = [91,21,3,15,6,30,19]

# accessing an element - constant time O(1)
print(myArray[3]);

# Add an element at the end
myArray.append(10)

# Insert an element at the beginning or middle
myArray.insert(0, 7) # inserts 7 at the beginning of the array

# deleting elements
myArray.pop() # deletes the last element in an array

del myArray[4] # deletes an element at index 4

print(myArray)