# Decorators are like tolls booth
# Function is passed from a box or pipe  

#  ****************** Measuring func exec time ******************

import time

def timer(func):
  def wrapper(*args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time() 
    print(f'{func.__name__} ran in {end_time - start_time}s')
    return result
  return wrapper

@timer
def sleep_func(sleep_time):
  time.sleep(sleep_time)

# sleep_func(2)
@timer
def factorial(n:int):
  if n == 0: return 1
  return n * factorial(n-1)

# print(factorial(5))

# *********************** print func name & args ***********************

def print_name_args(func):
  def wrapper(*args, **kwargs):
    print(f'Name: {func.__name__}')
    args_values = ', '.join(str(arg) for arg in args)
    kw_args_vals = ', '.join(f"Key: {key} Values: {value}" for key , value in kwargs.items())
    print(f'Args: {args_values}\nKeyword Args: {kw_args_vals}')
    return func(*args, **kwargs)
  return wrapper

@print_name_args
def sum(n:int):
  sum = 0
  for i in range(1, n+1):
    sum += i
  return sum

# print(sum(10))

# *********************** cache return value of function ***********************

def cache_func(func):
  cached_values = dict({})
  print(f'Cached Values: {cached_values}')
  def wrapper(*args, **kwargs):
    if args in cached_values:
      print(f'Result was already present in the cache')
      return cached_values[args]
    result = func(*args, **kwargs)
    cached_values[args] = result
    return result
  return wrapper

@cache_func
def delayed_sum(a,b):
  time.sleep(2)
  return a + b

print(f'Sum: {delayed_sum(2,3)}')
print(f'Sum: {delayed_sum(2,3)}')
print(f'Sum: {delayed_sum(2,3)}')