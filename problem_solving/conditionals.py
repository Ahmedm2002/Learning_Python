# Problem 1 Solution

def get_life_stage():
  age = int(input('Enter Age: '))
  # age = 22
  life_stage = str()

  if age <= 13:
    life_stage = 'Child'
  elif age > 13 and age <= 19:
    life_stage = 'Teenager'
  elif age > 19 and age <= 59:
    life_stage = 'Adult'
  else:
    life_stage = 'Senior'
  print(f'You are a {life_stage}')

# get_life_stage()  

# Problem 2 Solution


def movie_ticket_price():
  age = int(input('Enter your age: '))
  # age = 6
  is_wednesday = True
  ticket_price = 12 if age >= 18 else 8
  if is_wednesday:
    ticket_price  -=  2
  print(f'Ticket Price: ${ticket_price}')

# movie_ticket_price()

# Problem 3 Solution

def get_student_grade():
  student_score = int(input('Enter your score: '))
  student_grade = str()

  if student_score >= 101 or student_score < 0:
    print('Enter Valid Score')
    exit()

  if student_score >= 90:
    student_grade = 'A'
  elif student_score >= 80:
    student_grade = 'B'
  elif student_score >= 70:
    student_grade = 'C'
  elif student_score >= 60  :
    student_grade = 'D'
  else:
    student_grade = 'Fail'
  print(f'Grade : {student_grade}')

# get_student_grade()


# Problem 9 Solution 

def get_leap_year(input_year):
  
  input_year = int(input_year)
  
  if (input_year % 400 == 0) or (input_year % 4 == 0 and input_year % 100 != 0):
    print(f'{input_year} is a leap year')
  else:
    print(f'{input_year} is not a leap year')
  
# get_leap_year(2002)