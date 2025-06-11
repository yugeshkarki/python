# Sample dictionary
person = {
    'name': 'John',
    'age': 30,
    'city': 'Kathmandu'
}

# 1. clear()
person.clear()
print("After clear():", person)

# 2. copy()
person = {'name': 'John', 'age': 30, 'city': 'Kathmandu'}
person_copy = person.copy()
print("After copy():", person_copy)



# 3. get()
age = person.get('age')
print("Age:", age)

# 4. items()
items = person.items()
print("Items:", items)

# 5. keys()
keys = person.keys()
print("Keys:", keys)

# 6. pop()
removed_value = person.pop('age')
print("Removed value:", removed_value)
print("After pop():", person)



# 7. update()
person.update({'email': 'john@example.com'})
print("After update():", person)

# 8. values()
values = person.values()
print("Values:", values)
