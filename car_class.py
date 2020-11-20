class Car:
    name = ''
    color = ''

    def __init__(self, n, c):
        self.name = n
        self.color = c

    def start(self):
        print("name:", self.name)
        print("color:", self.color)
        print("Starting the car.")


my_car = Car('Corolla', 'Black')
my_car.start()
my_car1 = Car('Allion', 'Red')
my_car1.start()
my_car2 = Car('Bugatti', 'Yellow')
my_car2.year = 2000
my_car2.start()
print("Car name:", my_car2.name, "Car color:", my_car2.color, "Car year:", my_car2.year)

# Car.start(my_car)
