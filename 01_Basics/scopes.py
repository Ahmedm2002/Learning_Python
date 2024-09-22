name = 'Daniel'
def func_scope():
  # name = 'Joe Root'
  print(name)

# func_scope()
# print(name)

#  this variable is saved in the memory directly
name = 'John Doe'

# in most languages the scope is in {} and in python identation is the scope for a variable

# a varaible scope inside a function is just like a box in a memory where a variiable is stored it can be accessed inside the box but can't be accessed by outer memory

# Each scope is like a new box in a memory and it can contain multiple rooms i.e the others scopes inside the function can access the variable

# Ghar ke bat bahir mat jane chayae


x = 99

def func_scope2(y):
  # x = 10
  z = x + y
  return z

# print(func_scope2(1))

def func_scope3():
  global x
  x = '😂 I have been Changed inside func_scope3() using the global keyword'

# func_scope3()

# def func_scope4():
#   global laptop_company
#   laptop_company = 'Hp' 
#   print(laptop_company)


# print(f'Global Laptop Company: {laptop_company}')
# func_scope4()

# ❌ don't use global keyword inside a function as it modifies the original variable and working with a team makes it confusing that which function has modified the variable

def func1():
  x = 101
  def func2():
    # This is a room inside the box func1() if x is not present then it see in the func1() scope and then global scope
    print(x)
  return func2
    
# result = func1()
# result()


# A Closure in Python is a function object that remembers values in enclosing scopes even if they are not present in memory. 

def outer_func(x):
  def inner_func(y):
    return y ** x
  return inner_func

# power = outer_func(3)
# print(power(2))

def divident(x):
  def divisor(y):
    return float(x / y)
  return divisor

a = divident(99)   # Stores defination of the inner function in this case divisor and also takes backpack (khane ka saman) in this case its x 
b = divident(300)

print(a) # => also takes the value 99 and holds it  
print(b) # => also takes the value 300 and holds it  



# def divident(99):
#   def divisor(y):
#     return float(99 / y)
#   return divisor


# for i in range(1,11):
#   print(round(a(i), 2))


