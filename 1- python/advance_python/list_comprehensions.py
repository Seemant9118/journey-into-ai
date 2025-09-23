# list comprehensions in python

# List Comprehension is an elegant way to create lists based on existing lists.

# Syntax
# new_list = [expression for item in iterable if condition]
# expression → what to store in the new list
# item → each element from the iterable
# iterable → the list or collection you’re looping over
# if condition → (optional) filter to include only certain elements


existing_list = [1,7,12,11,22,5,9,3,15]
new_list = [existing_item for existing_item in existing_list if existing_item > 8]
print(new_list)  # Output: [12, 11, 22, 9, 15]

# How it works?

# Take each existing_item from existing_list.
# Check condition: if existing_item > 8.
# If condition is True, include existing_item in new_list.
# Otherwise, skip it.

# Step-by-step execution:

# 1 → not > 8 → skip
# 7 → not > 8 → skip
# 12 → yes → include
# 11 → yes → include
# 22 → yes → include
# 5 → not > 8 → skip
# 9 → yes → include
# 3 → not > 8 → skip
# 15 → yes → include