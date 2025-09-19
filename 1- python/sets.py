# sets : A set is an unordered collection of unique elements.

# properties of set
# 1. It is unordered.
# 2. It is mutable.
# 3. It is unindexed.
# 4. Cannot contain duplicate elements.

my_set = {1, 2, 2, 3, 4, 5}
print(my_set)
print(type(my_set))

# set methods
my_set.add(6) # adds an element to the set
print(my_set)
my_set.remove(2) # removes an element from the set, raises KeyError if element not found
print(my_set)
my_set.discard(10) # removes an element from the set, does nothing if element not found
print(my_set)
my_set.pop() # removes and returns an arbitrary element from the set
print(my_set)
print(len(my_set)) # returns the number of elements in the set
print(3 in my_set) # checks if an element is in the set
print(10 in my_set) # checks if an element is in the set
my_set.clear() # clears the set
print(my_set)
# my_set[0] # TypeError: 'set' object is not subscriptable
# my_set[0] = 10 # TypeError: 'set' object does not support item assignment
# my_set[1:3] # TypeError: 'set' object is not subscriptable
my_set.update({7, 8, 9}) # updates the set with elements from another set
print(my_set)
my_set.update([10, 11, 12]) # updates the set with elements from a list
print(my_set)

my_set2 = {11, 12, 13, 14, 15}
print(my_set2)

print(my_set.union(my_set2)) # returns a new set with elements from both sets
print(my_set.intersection(my_set2)) # returns a new set with elements common to both

print(my_set.difference(my_set2)) # returns a new set with elements in the first set but not in the second
print(my_set2.difference(my_set)) # returns a new set with elements in the second

print(my_set.symmetric_difference(my_set2)) # returns a new set with elements in either set but not in both

print(my_set.isdisjoint(my_set2)) # checks if two sets have no elements in common
print(my_set.issubset(my_set2)) # checks if the first set is a subset of the second
print(my_set.issuperset(my_set2)) # checks if the first set is a
print(my_set2.issuperset(my_set)) # checks if the second set is a superset of the first
# my_set.sort() # AttributeError: 'set' object has no attribute 'sort'
# my_set.reverse() # AttributeError: 'set' object has no attribute 'reverse'    
# my_set.insert(1, 10) # AttributeError: 'set' object has no attribute 'insert'
# my_set.copy() # AttributeError: 'set' object has no attribute 'copy'
# my_set.remove(2) # AttributeError: 'set' object has no attribute 'remove'
# my_set.pop() # AttributeError: 'set' object has no attribute 'pop'
# my_set.clear() # AttributeError: 'set' object has no attribute 'clear'
# my_set.extend({16,17}) # AttributeError: 'set' object has no attribute 'extend'
# my_set.append(18) # AttributeError: 'set' object has no attribute '
# my_set.count(3) # AttributeError: 'set' object has no attribute 'count'
# my_set.index(3) # AttributeError: 'set' object has no attribute '
# print(my_set[1]) # TypeError: 'set' object is not subscriptable
# print(my_set[1:4]) # TypeError: 'set' object is not
# print(my_set[1]) # TypeError: 'set' object is not subscriptable
# print(my_set[1:4]) # TypeError: 'set' object is not
# print(my_set[1]) # TypeError: 'set' object is not subscriptable
# print(my_set[1:4]) # TypeError: 'set' object is not
# print(my_set[1]) # TypeError: 'set' object is not subscriptable
# print(my_set[1:4]) # TypeError: 'set' object is not subscriptable
# print(my_set[1]) # TypeError: 'set' object is not subscript
# print(my_set[1:4]) # TypeError: 'set' object is not subscriptable
# print(my_set[1]) # TypeError: 'set' object is not subscript
# print(my_set[1:4]) # TypeError: 'set' object is not subscriptable
# print(my_set[1]) # TypeError: 'set' object is not subscriptable
