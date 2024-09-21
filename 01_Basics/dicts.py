# In dictionaries we define the key and the value pairs

student = {
  "name" : "John Daniel",
  "roll_no" : 324123,
  "father_name" : "Daniel Doe"
}

# if student.get("asdf") == None:
#   print("No Such field in the dictionary")

student["roll_no"] = 23040234

# print(student)

# for field in student:
  # print(f'{field}: \t{student[field]}')

# print(type(student.items()))

# for key , value in student.items():
#   print(f'{key}: {value}')

# if "name" in student:
#   print(f"name is present {student["name"]}")

student['Class'] = 'BsCS Semester 5'

# print(student)
# student.popitem()
# print(student)

# del student['Class']
# print(student)


nested_dicts = {
  "list1" : [1,2,3,4],
  "list2" : [5,6,7,8],
  "list3" : [23,312,543]
}

# for list in nested_dicts:
#   for val in nested_dicts[list]:
#     print(val)

family = {
  "child1" : {
    "name" : "John",
    "age"  : 5
  },
  "child2" : {
    "name" : "Roy",
    "age"  : 21
  },
  "child3" : {
    "name" : "Erick",
    "age"  : 12
  }
}

# print(family)

# for child in family:
#   print(child, family[child])
#   for child_detail in family[child]:
#     print(child_detail, family[child][child_detail])

nums = {x:x**2 for x in range(11)}

# for num in nums:
#   print(num, nums[num])

# nums.clear()
# print(nums)

keys = ["a", 'b', "c"]
values = ["apple", "boat", "cat"]
 
defalult_value = 'alphabet'

# for value in values:
#   new_dict = dict.fromkeys(keys,value)

# print(new_dict)