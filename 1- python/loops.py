# loops in python

# while loop
i = 1
while(i <= 10):
    print(i) # Output: 1 2 3 4 5 6 7 8 9
    i = i + 1
print("while loop ended") # Output: while loop ended

# example of while loop :  print the content of a list using while loops.
li = [1, 2, 3, 4, 5]

i = 0
while(i < len(li)):
    print(li[i]) # Output: 1 2 3 4 5
    i = i + 1

# for loop
for i in li:
    print(i) # Output: 1 2 3 4 5

# range fn
# range(start, stop, step_size)
for i in range(1, 11):
    print(i) # Output: 1 2 3 4 5 6 7 8 9 10

# break statement
for i in range(1, 11):
    if i == 5:
        break
    print(i) # Output: 1 2 3 4
print("loop ended") # Output: loop ended

# continue statement
for i in range(1, 11):
    if i == 5:
        continue
    print(i) # Output: 1 2 3 4 6 7 8 9 10

# pass statement
l = [1,7,8]
for item in l:
    pass # pass is used as a placeholder for future code

