# string interning

import gc

# Python was specifically designed for scientists

name = 'Joe Root'

# print(name.count('Root'))

# print(name.find('Joe'))

# print(name[:4])

first_char = name[0]

# print(first_char)

# slice_name = name[:4]
# print(slice_name)

num_list = "0123456789"

# print(num_list[:9:5])
# print(num_list[:7])

# counts = name.count('o')
# print(counts)

father_name = '    Tree Root'
# print(father_name.strip())

# print(father_name.replace('Tree', 'Trunk'))

car_companies = "Ferrari, Toyota, Audi, Tesla, Honda"

provinces = ['Punjab', 'Sindth', 'Balochistan', 'KPK', 'Gilgit Baltistan']

str_provinces = ", ".join(provinces)

# print(str_provinces)
# print(f'Length: {len(str_provinces)}')

# By default splits on space

companies_list = car_companies.split(', ')
# print(companies_list)
# for x in companies_list:
#   if(x == 'Tesla'):
#     continue
#   print(x)


def get_garbage_collector_methods():
  garbage_methods = list(dir(gc))
  for method in garbage_methods:
    print(method)

# get_garbage_collector_methods()

# print(gc.get_count())

# In strings {} => called placeholders your can inject values later using the format method of the strings to add the values on the go 

# greetings = "Hi Mr.{} your age is {} and your father name is {}"

# print(greetings.format('Ahmed Mujtaba', 22, 'Abdul Waheed'))

print("He Said, \"Python is the best\"")

# to treat string as it is 

string = r"This \n is a raw\t string."
print(string)