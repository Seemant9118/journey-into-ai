#string declaration
a="abc"
b='abcd'
c='''abcde'''
d="""abcdef"""

#string slicing
print(a[0])   # 'a'
print(b[1:3]) # 'bc'
print(c[:4])  # 'abcd'
print(d[2:])  # 'cdef'
print(d[-1])  # 'f'
print(d[-3:-1]) # 'de'

# slicing with skip value
print(d[::-1]) # 'fedcba'
print(d[::2])  # 'ace'

#string functions
str = "hello world"
print(len(str))          # 11
print(str.upper())       # 'HELLO WORLD'
print(str.lower())       # 'hello world'
print(str.strip())       # 'hello world'
print(str.split())       # ['hello', 'world']
print(str.replace("world", "Python")) # 'hello Python'
print(str.find("lo"))    # 3
print(str.find("z"))     # -1
print(str.index("lo"))   # 3
# print(str.index("z"))    # ValueError: substring not found
print(str.count("l"))    # 3
print(str.startswith("he")) # True
print(str.endswith("ld"))   # True  
print(str.isalpha())     # False
print(str.isdigit())     # False
print(str.isalnum())     # False
print(str.isspace())     # False

# escape sequences characters
letter = '''
Dear <|Name|>,
You are selected! on
<|Date|>'''

print(letter)
prefix = input('Enter prefix: ')
name = input('Enter your name: ')
date = input('Enter date: ')
letter = letter.replace('Dear', prefix)
letter = letter.replace('<|Name|>', name)
letter = letter.replace('<|Date|>', date)
print(letter)