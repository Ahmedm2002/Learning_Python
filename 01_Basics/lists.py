# List == Array in other languages

# in list keys are pre-defined and in dictionaries we define the keys and their values

mobile_companies = ['Apple', 'Samsung', 'Huawei', 'Realme', 'Infinix', 'Techno']

# print(mobile_companies[2])

# print(len(mobile_companies))

n = 5

# print(mobile_companies[:(int (n / 2) * 3) - 1])

# jump = 2

# print(mobile_companies[:n:jump])

# print(mobile_companies[2])

more_companies = mobile_companies[2:3]
more_companies.append('RedMe')
# print(more_companies)

# mobile_companies[1:2] = 'Samsung Inc'   ❌ it perceives each character as a different value 
# print(mobile_companies)

mobile_companies[1:2] = ["Samsung Inc"]
mobile_companies[1:3] = ["Samsung Inc", "Huawei Ptv ltd"]

# print(mobile_companies)

mobile_companies[1:1] = ['Nokia', 'Google']
# print(mobile_companies)

# Insert nothing => delete operation 

# mobile_companies[1:3] = []

# print(mobile_companies)

def printList(list1):
  for value in list1:
    print(value, end="\t")
  # printList('\n')

mobile_companies.remove('Realme')
# print(mobile_companies)

mobile_companies_copy = mobile_companies
mobile_companies_copy[0] = 'Blalalal'

# printList(mobile_companies)
# print(f'Mobile companies id: {id(mobile_companies)}')
# print('\n')
# print(f'Copy Mobile companies id : {id(mobile_companies_copy)}')


# print(mobile_companies_copy is mobile_companies)

a = 'Hello'
b = 'hello'

# print(a == b)
# print(a is b)
# print(f'Id A: {id(a)}')
# print(f'Id B: {id(b)}')

# print(range(10))

# x = range(10)
# print(x)

squared_nums = [ round(num**2.4,3) for num in range(0,11,3)]
print(squared_nums)