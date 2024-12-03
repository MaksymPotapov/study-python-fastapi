class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f'-Brand: {self.brand}\n-Model: {self.model}\n-Year of production: {self.year}')

class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type):
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type

    def start_engine(self):
        print('The engine is running')

    def display_info(self):
        super().display_info()
        print(f'-Fuel type: {self.fuel_type}')

class Bicycle(Vehicle):
    def __init__(self, brand, model, year, supported_weight):
        super().__init__(brand, model, year)
        self.supported_weight = supported_weight

    def check_weight(self, weight):
        if weight > self.supported_weight:
            print(f'Your weight exceeds the limit by: {weight - self.supported_weight}')
        else:
            print('The weight is supported')

    def display_info(self):
        super().display_info()
        print(f'-Supported weight: {self.supported_weight}')


car1 = Car('Honda', 'Civic', 1972, 'Gas')
car1.display_info()
print('-------------------------------------------')
car1.start_engine()
print('-------------------------------------------')
bike1 = Bicycle('Shimano', 'GRX', 2020, 90)
bike1.display_info()
print('-------------------------------------------')
bike1.check_weight(65)
print('-------------------------------------------')