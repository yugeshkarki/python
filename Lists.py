
fruits = ['apple', 'banana', 'cherry', 'date']

# append() - Adds an element to the end of the list
fruits.append('elderberry')
print("After append:", fruits)

# extend() - Adds multiple elements to the end of the list
fruits.extend(['fig', 'grape'])
print("After extend:", fruits)

# insert() - Adds an element at a specific index
fruits.insert(2, 'blackberry')
print("After insert:", fruits)

# remove() - Removes the first occurrence of a value
fruits.remove('banana')
print("After remove:", fruits)

# pop() - Removes and returns an element at a given index
removed_fruit = fruits.pop(3)
print(f"Removed fruit: {removed_fruit}")
print("After pop:", fruits)

# clear() - Removes all elements from the list
fruits.clear()
print("After clear:", fruits)

# count() - Returns the number of occurrences of a value
fruits = ['apple', 'banana', 'cherry', 'apple', 'apple']
apple_count = fruits.count('apple')
print("Count of 'apple':", apple_count)

# index() - Returns the index of the first occurrence of a value
banana_index = fruits.index('banana')
print("Index of 'banana':", banana_index)

# sort() - Sorts the list in ascending order
fruits.sort()
print("After sort:", fruits)

# reverse() - Reverses the order of the list
fruits.reverse()
print("After reverse:", fruits)

# copy() - Returns a shallow copy of the list
fruits_copy = fruits.copy()
print("Copied list:", fruits_copy)
