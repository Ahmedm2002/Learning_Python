# Looping Positive Number

def cal_positive_nums():
  numbers = [1,2,3,4,-5,7,-56,-32,2,-1]
  positive_nums = 0
  for num in numbers:
    if num > 0:
      positive_nums += 1
  print(f'Positive Numbers in List: {positive_nums}')

# cal_positive_nums()

# Calculate sum upto given number

def calculate_sum(n):
  sum = 0
  for x in range(1,n+1):
    if x % 2 == 0:
      sum += x
  print(f'Sum Upto {n}: {sum}')

# calculate_sum(5)

# Calculating table upto 10 but skipping 5

def get_table(n):
  for i in range(1, 11):
    if i == 5: continue
    print(f'{n} x {i} = {n*i}')

# get_table(10)

# Printing String in reverse order

def reverse_string(string:str):
  reversed_string = ''
  for char in string:
    reversed_string = char + reversed_string
  print(f'Reversed String: {reversed_string}')

# reverse_string('Ahmed')

# Find first Non repeating char

def find_non_repeated_char(string:str):
  for char in string:
    if string.count(char) == 1:
      print(f'Frist Non Repeating Char: {char}')
      break

# find_non_repeated_char('teeter')

# Finding Factorial using while loop

def find_factorial(n):
  i = 1
  factorial = 1
  while i <= n:
    factorial = factorial * i
    i += 1
  
  # Or 
  # you can use this syantaxx 
  # while n > 0:
  #     factorial *= n
  #     n -= 1

  print(f'Factorial of {n}: {factorial}')\

  
  
# find_factorial(5)

# Keep asking user for input if number is between 1 to 10

def validate_input():
  while True:
    input_value = int(input('Enter a number between 1 and 10: '))
    # if input_value >= 1 and input_value <=10:
    if 1 <= input_value <= 10:
      print('Thanks')
      break
    else:
      print('\nInvalid num, try again\n')

# validate_input()


# Loop for Prime Number Checker

def is_prime(n):
  # divide_count = int(0)
  # for x in range(1, n+1):
  #   if n % x == 0:
  #     divide_count += 1
  # if divide_count <= 2:
  #   print(f'{n} is a Prime number')
  # else: 
  #   print(f'{n} is not a Prime number')

  # OR

  prime = True

  for i in range(2,n):
    if (n % i) == 0:
      prime = False
      break
  
  if prime : print(f'{n} is a Prime number')
  else :  print(f'{n} is not a Prime number')
   
prime_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# for x in prime_nums:
#   is_prime(x)

# print duplicate and exit the loop for a list

def check_duplicate(list1:list):
  # for value in list1:
  #   if list1.count(value) > 1:
  #     print(f'Duplite: {value}')
  #     break

  # OR

  unique_values = set()
  for item in list1:
    if item in unique_values:
      print(f'Duplicate: {item}')
      break
    unique_values.add(item)


list2 = ['Apple', 'Huawei', 'Samsung', 'Apple']

# check_duplicate(list2)

# Implementing exponential backoff

import time

def exponential_backoff():
  wait_time = 1
  max_retries = 5
  user_attempt = 0
  while user_attempt < max_retries:
    print(f'Attempts: {user_attempt + 1}, Wait Time: {wait_time + 1}')
    time.sleep(wait_time)
    wait_time *= 2
    user_attempt += 1

# exponential_backoff()