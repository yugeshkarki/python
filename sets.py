# Create a set
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)

# add() - Adds an element to the set
my_set.add(6)
print("After add(6):", my_set)

# copy() - Returns a shallow copy of the set
set_copy = my_set.copy()
print("Copied Set:", set_copy)

# discard() - Removes an element from the set if it exists
my_set.discard(3)
print("After discard(3):", my_set)

# remove() - Removes an element from the set; raises KeyError if not found
my_set.remove(4)
print("After remove(4):", my_set)



# clear() - Removes all elements from the set
my_set.clear()
print("After clear():", my_set)

# union() - Returns a set containing the union of sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)

# intersection() - Returns a set containing the intersection of sets
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)

# difference() - Returns a set containing the difference of sets
difference_set = set1.difference(set2)
print("Difference of set1 and set2:", difference_set)




