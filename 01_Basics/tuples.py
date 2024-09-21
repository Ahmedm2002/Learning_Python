# Why tuples are needed when there is list already present

#  List   =>  Mutable
#  Tuple  =>  Immutable

laptop_companies = ("Hp", "Dell", "Asus", "Macbook", "Lenovo")
other_companies = ("MSI", "Sony", "Toshiba")
# print(laptop_companies[0])
# print(laptop_companies[1:4])
# print(laptop_companies[:-1])

#  Tuple cannot be changed

all_companies = laptop_companies + other_companies

# print(len(laptop_companies))

# print(all_companies)

# if "Hp" in all_companies and "Hp" in laptop_companies:
#   print('Present in both Tuples')

# for x in laptop_companies:
#   print(x)