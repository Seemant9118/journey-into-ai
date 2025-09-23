# dictionary merge and update Newer vs Earlier

# Newer
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
# Merging dictionaries using the merge operator (Python 3.9+)
merged_dict = dict1 | dict2
print("Merged Dictionary:", merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}

# Updating dictionary using the update operator (Python 3.9+)
dict1 |= dict2
print("Updated Dictionary:", dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}
# Note: The merge operator (|) creates a new dictionary, while the update operator (|=) modifies the existing dictionary in place.

# Earlier
# we can use the update() method to achieve similar results
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1.update(dict2)
print("Updated Dictionary using update():", dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}
# To merge two dictionaries and create a new one, you can use the {**dict1, **dict2} syntax
dict1 = {'a': 1, 'b': 2}    
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}
print("Merged Dictionary using unpacking:", merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}

# In both cases, if there are overlapping keys, the values from the second dictionary will overwrite those from the first.


