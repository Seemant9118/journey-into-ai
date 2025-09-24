# formats in python 
# old method to inject value into string, now we generally use 'f' string method to inject
# Formats the values inside the string into a desired output.

a = "{} is a good {}".format("harry", "boy") #1.
b = "{1} is a good {0}".format("harry", "boy") #2.

print(a)
print(b)
# output for 1:
# harry is a good boy
# output for 2:
# boy is a good harry 