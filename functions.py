# functions are extremely important - this will be a long file :(


# we've probably all seen mathematical functions like
# f(x) = x + 1

# functions in coding can be a lot like that.
# we can tell functions to give us a result
# based on the inputs we give it

# we declare funtions with "def" for define

def function(x):  # function definition
    return x + 1


two = function(1)  # function call
print(two)


def add(x, y):
    return x + y


five = add(two, 3)
print(five)

counter = 0


def add_to_counter():
    global counter  # we have to state we want to use the
    # variable counter that is not in our indent level (scope)
    counter += 1


add_to_counter()
print(counter)


# we saw there a basic function blueprint:
# def name(arguments):
#     code...

# however, functions are more versatile than that
# we dont even need to pass any arguments to a function,
# nor do we need to expect a result

# say we want to get a custom built array

def get_array():  # no arguments!
    return ["pretend", "this", "is", "random"]


# say we want no return value

def say_hi(name):
    print("Hi, " + name)


say_hi("reader")

# in fact, the print statement is also a function call.
