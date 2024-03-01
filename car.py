class Car:

    def __init__(self,brand,model,year,color) :
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
    
    def drive(self):
        print("This car is driving!")

    def stop(self):
        print("The car is stopped!")

car_1 = Car("Aston Martin", "DB11", "2019","Black")

print(car_1.brand)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_2=Car("Lamborghini","Aventador","2013","Orange")

print(car_2.brand)
print(car_2.model)
print(car_2.year)
print(car_2.color)