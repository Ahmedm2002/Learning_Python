# Function Basic Syantax

def num_square(num:int):
  result = num * num
  print(f'Square Root: {result}')
  return  result

# num_square(5)

# Multiple Parametsers

def get_sum(num1:int , num2:int):

  print(f'{num1} + {num2} = {num1 + num2}')

# get_sum(3,4)

# Polymorphism in Function

def multiply(para1, para2):
  return para1 * para2

# print(multiply(6,7))
# print(multiply(6,'a'))
# print(multiply('b',4))

# Returning multiple values

from math import pi

def get_circle_stats(radius:float):
  circumference = (2 * pi) * radius
  area = pi * (radius * radius)

  return circumference, area

crircumference , area = get_circle_stats(10)

# print(f'Circumference: {round(crircumference,2)}, Area: {round(area,2)}')

# Default Parameters

def greetings(name = 'Anonymous'):
  return f'Welcome Mr.{name}'

# print(greetings('Ahmed Mujtaba'))
# print(greetings())


#  lambda function or in simple words funcs which don't have any name

# Calculate cube of a number using a lambda function

cube = lambda x : x ** 3
# print(f'Cube: {cube(3)}')


# Function with *args 

# take variable num of numbers and return their sum

def get_sum(*args):
  # print(f'Args: {args}')
  # print(f'Args length: {len(args)}')
  # print(f'Args dataType: {type(args)}')
  
  return sum(args)

# print(f'Sum: {get_sum(1,2,5,4,2)}')

# Function with **kwargs
# function which accept key:value arguments

def print_kwargs(**kwargs):
  for key , value in kwargs.items():
    print(f'{key}: {value}')

# print_kwargs(name = "John", age = 24)
# print_kwargs(name = "Daniel", profession = 'Software Enginner')
# print_kwargs(name = "Daniel")

# Generator function with yield

# write yield funtion that yields even numbers upto a limit

def even_generator(limit):
  for i in range(2, limit + 1, 2):
    yield i

# for even_nums in even_generator(20):
#   print(even_nums)

#  yield generates/produces/yields a value also save the state of the funtion in memory so when next time called it starts for the same thing it has left


# Recursive Function to calculate factorial

def get_factorial(n):
  if n == 0 : return 1
  return n * get_factorial(n-1)

print(f'Factorial of 4: {get_factorial(4)}')
print(f'Factorial of 5: {get_factorial(5)}')