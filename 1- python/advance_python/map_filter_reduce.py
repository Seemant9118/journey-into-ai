# map method
# Map applies a function to all the items in an input_list.
# SYNTAX : map(function, input_list)
# the function can be lambda function

l1 = [1,2,3,4,5]

square = lambda x:x*x

sqaured_list = map(square,l1)

print(list(sqaured_list))


# filter method
# Filter creates a list of items for which the function returns true.

# SYNTAX : list(filter(function,input_list))
# the function can be lambda function

def even_no(n):
    if n % 2 == 0:
        return True

even_list = filter(even_no,l1)
print(list(even_list))

# reduce method
# Reduce applies a rolling computation to sequential pair of elements.

from functools import reduce

compute_fn = lambda a,b : a + b

computed_res = reduce(compute_fn,l1)

print(computed_res)