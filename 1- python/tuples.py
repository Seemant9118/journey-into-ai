# tuples : A tuple is an immutable data type in python.
# tuples are immutable
my_tuple = (1, 2, 2, 3, 4, 5)
print(my_tuple)
print(type(my_tuple))

# tuple methods
print(my_tuple.count(2)) # returns count of occurrences of value
print(my_tuple.index(3)) # returns index of first occurrence of value
# my_tuple[1] = 10 # TypeError: 'tuple' object does not support item assignment
# my_tuple.append(6) # AttributeError: 'tuple' object has no attribute 'append'
# my_tuple.remove(2) # AttributeError: 'tuple' object has no attribute 'remove'
# my_tuple.pop() # AttributeError: 'tuple' object has no attribute 'pop'
# my_tuple.clear() # AttributeError: 'tuple' object has no attribute 'clear'
# my_tuple.sort() # AttributeError: 'tuple' object has no attribute 'sort'
# my_tuple.reverse() # AttributeError: 'tuple' object has no attribute 'reverse'
# my_tuple.extend((6,7)) # AttributeError: 'tuple' object has no attribute 'extend'
# my_tuple.insert(1, 10) # AttributeError: 'tuple' object has
# my_tuple.copy() # AttributeError: 'tuple' object has no attribute 'copy'
# my_tuple.remove(2) # AttributeError: 'tuple' object has no attribute 'remove'
print(my_tuple[1]) # 2
print(my_tuple[1:4]) # (2, 3, 4)    