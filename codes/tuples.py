
my_tuple = (1, 2, 3, 4, 5, 2, 3, 2)

# count() - Returns the number of times a specified value occurs in the tuple
count_2 = my_tuple.count(2)
print("Count of 2:", count_2)

# index() - Searches the tuple for a specified value and returns the position of where it was found
index_3 = my_tuple.index(3)
print("Index of first occurrence of 3:", index_3)

# len() - Returns the length of the tuple
length = len(my_tuple)
print("Length of tuple:", length)

# max() - Returns the largest element in the tuple
maximum = max(my_tuple)
print("Maximum value:", maximum)

# min() - Returns the smallest element in the tuple
minimum = min(my_tuple)
print("Minimum value:", minimum)

# sorted() - Returns a sorted list of the tuple
sorted_tuple = sorted(my_tuple)
print("Sorted tuple:", sorted_tuple)

# sum() - Returns the sum of all elements in the tuple
total = sum(my_tuple)
print("Sum of elements:", total)

# any() - Returns True if any element in the tuple is True
any_true = any(my_tuple)
print("Any True:", any_true)

# all() - Returns True if all elements in the tuple are True
all_true = all(my_tuple)
print("All True:", all_true)

# tuple() - Converts a list into a tuple
my_list = [6, 7, 8]
tuple_from_list = tuple(my_list)
print("Tuple from list:", tuple_from_list)
