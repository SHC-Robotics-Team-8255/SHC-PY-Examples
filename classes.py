# classes are a way we can bundle and organize
# variables and functions (or methods)

# we use classes to simulate and represent
# real or abstract objects

# lets declare a class blueprint
# keep in mind in order to use a class
# we have to make it. This is just a blueprint

class Car:
    wheels = 4  # we declare something common to all cars
    color = None

    def __init__(self):  # init for initialize, "__" for native method
        self.on = False  # each time we make it, its default state is off

    def turn_on(self):
        self.on = True  # lets change the default state

    def turn_off(self):
        self.on = False

    def is_on(self):
        return self.on  # lets read the default state


# lets instantiate (make) a car
my_car = Car()  # yes, we called it like a function

my_car.turn_on()  # i turned on my car
print(my_car.is_on())

your_car = Car()  # yep, we can make as many cars as we want with our blueprint

# lets leave your car off

print(your_car.is_on())

print(my_car.wheels, your_car.wheels)  # even though the "on" property can vary,


# the wheels property will stay the same between the two

# in other words, "wheels" is a property of the blueprint,
# and "on" of the made car

# classes can also "inherit" from another
# this means they build off of a simpler class

class HondaAccord2003(Car):
    color = "Rainbow"

    # since we did not override the wheels property, it will stay 4

    def turn_on(self):  # now we override the "turn_on" function
        pass  # yes, I overrid it so it no longer turns on


that_car = HondaAccord2003()

that_car.turn_on()
your_car.turn_on()

print(that_car.is_on())  # even though we did not override this function, it exists because of inheritance
print(my_car.is_on())
print(your_car.is_on())

# great, now we got 2 generic cars and one not working rainbow honda