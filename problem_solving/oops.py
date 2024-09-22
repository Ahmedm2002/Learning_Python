# Basic Class syantax of a car and create instance of it

class Car:     # General Practice => Classes name start with capital letter

  # __init__ is also called constructor

  def __init__(self, brand, model, owner): # This is a blank form and we can make instances of the car class accordingly
    self.model = model
    self.brand = brand
    self.owner = owner

  # Add Method to the car class that prints full name of car brand, model and owner

  def get_details(self):        # the self keyword establihes a link b/w funs & attributes (variables)
    return f'This is a {self.brand} {self.model} owned by {self.owner}'
  
# inherit electric car from car and add an attribute named batter_size

class Electric_car(Car):
  def __init__(self, brand, model, owner, battery_size):
    super().__init__(brand, model , owner)
    self.battery_size = battery_size
  
  def get_details(self):
    return super().get_details() + f' with {self.battery_size} battery'

car1 = Car('Audi', 'A5', 'Alison Anderson')
car2 = Car('Honda', 'Civic 2023', 'Joe Daniel')

model3 = Electric_car('Tesla', 'Model 3', 'Jane Smith', '85 kWh')
print(model3.get_details())