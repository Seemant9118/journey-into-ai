# list : Python lists are containers to store a set of values of any data type.
l1 = [7,9,"seemant"]
print(l1)
print(type(l1))

# list methods
l1.append("hello") # adds at the end
print(l1)
l1.insert(1, "world") # adds at the index
print(l1)
l1.remove(9) # removes the first occurrence of value
print(l1)
l1.pop() # removes the last element
print(l1)
l1.pop(1) # removes element at index
print(l1)
l1[1] = "python" # updates the value at index
print(l1)
print(l1.index("python")) # returns index of first occurrence of value
print(l1.count("seemant")) # returns count of occurrences of value
l2 = [1,2,3]
l1.extend(l2) # extends list by appending elements from another list
print(l1)
l1.sort(key=str) # sorts the list
print(l1)
l1.reverse() # reverses the list
print(l1)
l3 = l1.copy() # returns a copy of the list
print(l3)
l1.clear() # clears the list
print(l1)

# nested list
l4 = [l1, l2]
print(l4)
print(l4[1][2]) # 3
