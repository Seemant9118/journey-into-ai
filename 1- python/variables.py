# variable types in python
# int, float, str, bool, NoneType, complex
a=2
b=2.14
c="hello"
d=True
e=None
f=3+4j
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

# type fn to conversion
str(32) # '32'
int('32') # 32
float('32.5') # 32.5
bool(0) # False
bool(1) # True
bool('') # False
bool('hello') # True
complex(3) # (3+0j)
complex(3,4) # (3+4j)

# operators in python
# arithmetic operators: +, -, *, /, %, //, **
print(3 + 2)  # 5
print(3 - 2)  # 1
print(3 * 2)  # 6
print(3 / 2)  # 1.5
print(3 % 2)  # 1
print(3 // 2) # 1
print(3 ** 2) # 9
# comparison operators: ==, !=, >, <, >=, <=
print(3 == 2)  # False
print(3 != 2)  # True
print(3 > 2)   # True
print(3 < 2)   # False
print(3 >= 2)  # True
print(3 <= 2)  # False
# logical operators: and, or, not
print(True and False) # False
print(True or False)  # True
print(not True)       # False
print(not False)      # True
# bitwise operators: &, |, ^, ~, <<, >>
print(3 & 2)  # 2
print(3 | 2)  # 3
print(3 ^ 2)  # 1
print(~3)     # -4
print(3 << 1) # 6
print(3 >> 1) # 1
# assignment operators: =, +=, -=, *=, /=, %=, //=,
x = 3 # assignment
x += 2 # x = x + 2
print(x) # 5
