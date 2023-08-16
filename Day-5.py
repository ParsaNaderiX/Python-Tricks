# namedtuples in Python can be a great alternative to defining a class manually
from collections import namedtuple

Car = namedtuple("Car", "model mileage color")
# class_name = namedtuple("class_name", "space separated objects")

# new "Car" class works as expected
my_car = Car("Suzuki", 120000, "white")

print(my_car.model)  # Suzuki
print(my_car.mileage)  # 120000

print(my_car)  # Car(model='Suzuki', mileage=120000, color='white')


# my_car.color = "black"
# it occures an AttributeError (namedtuples are immutable)
