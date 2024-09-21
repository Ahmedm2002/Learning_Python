import math
import random
import copy

def fullName(firstName:str, lastName:str):
  print(f'{firstName.capitalize()} {lastName.capitalize()}')

# fullName('ahmed','mujtaba')

car1 = 'Honada'
car2 = 'Toyota'
car3 = 'Suzuki'
car4 = 'Audi'
car5 = 'Ferrari'

# Variables are also called attributes

# print(dir(car1))

# print(dir)

methods = list(dir(car1))

# for method in methods:
#   print(method)


choices1 = [9,45,78,342,78,32,87,3,934,134,12.567,3245.567]
choices2 = choices1.copy()
choices2.reverse()
# for i in range(20):
#   print(f'Choice {i}: {random.choice(choices)}')


# print(dir(math))


def get_Maths_Methods():
  mathsMethods = list(dir(math))
  print('Methods in Maths Library')
  for mthMethod in mathsMethods:
      print(mthMethod)

def get_Random_Methods():
  print('Methods in Random Library')
  randomMethods = list(dir(random))
  for rand_Method in randomMethods:
     print(rand_Method) 

def get_Copy_Methods():
   print('Methods in Copy Library')
   copy_Methods = list(dir(copy))
   for copy_method in copy_Methods:
      print(copy_method)

# get_Maths_Methods()
# get_Random_Methods()
# get_Copy_Methods()

# is checks the memory address are equal

# print(f'\n\nOriginal List: {choices1}\n\n')

# random.shuffle(choices1)

# print(f'Shuffle Method: {choices1}\n\n')
# print(f'Reverse Method: {choices2}\n\n')

tup = tuple(('Ahmed', 15, 'BsCS Sem 5', '40707223021'))

# print(tup[0])

# tup[0] = 'Ahmed Mujtaba'

# print(choices1.pop())

a = 10
b = 20


print(f'a: {a} \tb: {b}')

a = a + b
#  a = 30 , b = 20
b = a - b 
#  a = 30 , b = 10
a = a - b 
#  a = 20 , b = 10 

print(f'a: {a} \tb: {b}')

def returnDiff(n):
   # return 15 - n
   return int(56 / n)

# print(returnDiff(8))
# print(returnDiff(7))

"""
Weekend Tasks
1. Complete Python
2. Watch 5 vidoes of Os             4/5  Done
3. Watch 5 vidoes of Stats          0/5  Done
4. Watch 20 videos of Algorithms    3/20 Done
"""