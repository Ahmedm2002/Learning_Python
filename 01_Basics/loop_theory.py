# for i in range(1,11):
#   print(i)

file = open('loop_theory.py')

file.readline()

# for line in file:
#   print(line)

# while True:
#   line = file.readline()
#   if not line: break
#   print(line, end='')

list1 = [1,2,3,4,5]

list_iterator = iter(list1)

# for x in range(len(list1)):
#   print(list_iterator.__next__())

print(list1 is list_iterator)


# iter() => tells that is the object iteratebale or not if yes it returns the address of the first element of that prticualr data types

num = 12
iter_num = iter(num)
print(iter_num)