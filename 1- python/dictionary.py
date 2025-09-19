# dictionaries : Dictionary is a collection of keys-value pairs.
# properties of dictionary
# 1. It is unordered.
# 2. It is mutable.
# 3. It is indexed.
# 4. Cannot contain duplicate keys.

my_dict = {"name": "seemant", "age": 21, "city": "New Delhi"}
print(my_dict)
print(type(my_dict))

# dictionary methods
print(my_dict.keys()) # returns all keys
print(my_dict.values()) # returns all values
print(my_dict.items()) # returns all key-value pairs
print(my_dict.get("name")) # returns value for the key
print(my_dict["age"]) # returns value for the key
my_dict["age"] = 22 # updates the value for the key
print(my_dict)

my_dict["country"] = "India" # adds a new key-value pair
print(my_dict)
my_dict.pop("city") # removes the key-value pair
print(my_dict)
my_dict.popitem() # removes the last inserted key-value pair
print(my_dict)
my_dict.update({"age": 23, "city": "Delhi"}) # updates multiple key-value pairs
print(my_dict)
my_dict.clear() # clears the dictionary
print(my_dict)

# nested dictionary
my_dict = {"name": "seemant", "age": 21, "address": {"city": "New Delhi", "state": "Delhi"}}
print(my_dict)
print(type(my_dict))

print(my_dict["address"]["city"]) # New Delhi
print(my_dict["address"]["state"]) # Delhi
my_dict["address"]["city"] = "Mumbai" # updates the value for the key
print(my_dict)
my_dict["address"]["country"] = "India" # adds a new key-value pair
print(my_dict)
print(my_dict["address"].keys()) # returns all keys in nested dictionary
print(my_dict["address"].values()) # returns all values in nested dictionary
print(my_dict["address"].items()) # returns all key-value pairs in nested dictionary
my_dict["address"].pop("state") # removes the key-value pair in nested dictionary
print(my_dict)
my_dict["address"].clear() # clears the nested 
print(my_dict)

