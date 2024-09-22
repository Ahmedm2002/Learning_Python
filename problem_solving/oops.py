# Basic Class syantax of a car and create instance of it

class Car:     # General Practice => Classes name start with capital letter

  totalCars = 0
  @property
  def model(self):
    return self.__model

  @staticmethod
  def general_description():
    return 'A car, or an automobile, is a motor vehicle with wheels used mainly transport people over cargo'

  # __init__ is also called constructor
  def __init__(self, brand, model, owner): # This is a blank form and we can make instances of the car class accordingly
    Car.totalCars += 1
    self.__model = model
    self.__brand = brand
    self.owner = owner
    
  # Encapsulation => hide from others, make it private, can be accessed with a getter/method/function

  # __variable => makes the variable private

  # Add Method to the car class that prints full name of car brand, model and owner

  def get_details(self):        # the self keyword establihes a link b/w funs & attributes (variables)
    return f'This is a {self.__brand} {self.__model} owned by {self.owner}'
  
  def get_brand(self):
    return f'{self.__brand}'
  
  def fuel_type(self):
    return f'{self.__brand} {self.__model} can be refilled with Petrol, Diesel or CNG'
# inherit electric car from car and add an attribute named batter_size

class Electric_car(Car):
  def __init__(self, brand, model, owner, battery_size):
    super().__init__(brand, model , owner)
    self.battery_size = battery_size
  
  def get_details(self):
    return super().get_details() + f' with {self.battery_size} battery'

  def fuel_type(self):
    return f'{super().get_brand()} {self.__model} is charged not refilled'


car1 = Car('Audi', 'A5', 'Alison Anderson')
car2 = Electric_car('Tesla', 'Model 3', 'Jane Smith', '85 kWh')

print(car1.model)

# print(car1.get_model()) 

# print(car1.fuel_type())
# print(car2.fuel_type())

# print(f'Total cars created: {Car.totalCars}')

# print(car1.general_description())
# print(Car.general_description())

# print(car2.get_details())
 
car2.__setattr__('Capacity', 4)
# print(car2.Capacity)

# print(car2.get_brand())
# print(car2.get_brand())


# Convention => getter starts with get & setter starts with set

# Encapsulation => only available to the class cannot be accessed outside the class 

# Polymorphism => multiple ways of using

# Decorators => enhace the functionality of the function

# Static Method => availble to the Class but not to instances