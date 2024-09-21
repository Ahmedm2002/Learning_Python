# In Python the number is a group of objects like booleans, decimal, fraction, complex numbers and sets 
import math
x = 2
y = 3
z = 4

# repr

list1 = [1,2,3,4,5]

# print(repr(list1))

# reprMethods = list(dir(repr))
# for method in reprMethods: 
#   print(f'{method}\t')

# name = 'John Doe'
# print(repr(name))
# print(name)

# text = 'Hi! there'
# print(repr(text))

# num = int(12)

def get_math_functions():
  math_funcs = list(dir(math))
  for math_func in math_funcs:
    print(math_func)

# get_math_functions()

# Imagionay Numbers

num = 2 + 3j

# print(num)
# print(type(num))
# print(num * 3)

def get_complex_methods():
  complex_methods = list(dir(complex))
  for complex_method in complex_methods:
    print(complex_method)

# get_complex_methods()

# print(num.imag)
# print(num.real)
# print(num.conjugate())


#  Octal Numbers 

# print(0o45)
# print(0x45)
# print(0b111)

# print(oct(23))
# print(hex(15))
# print(bin(11))

# print(int('1000', 2))
# print(int('1000', 8))
# print(int('1000', 16))

import random

# for x in range(20):
#   print(random.randint(1,101))

list1 = [1,2,3,4,5,6,7,8,9,10]

# for x in range(51):
#   print(random.choice(list1))

# random.shuffle(list1)
# print(list1)

# print(0.1 + 0.1 + 0.4)
# print(0.1 + 0.1 + 0.3 - 0.3)

# import decimal 
# from decimal import Decimal

# print(Decimal('0.1')  + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))

# Part of Mathematics Sets

setOne = {1,2,3,4}
# print(type(setOne))
# print(setOne| {1,4,34})

# print(type({}))
# print(type(set()))

# print(type(False))

def get_bool_methods():
  bool_methods = list(dir(bool))
  for bool_method in bool_methods:
    print(bool_method)

# get_bool_methods()

def get_dict_methods():
  dict_methods = list(dir(dict))
  for dict_method in dict_methods:
    print(dict_method)

# get_dict_methods()