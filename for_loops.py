# for loops are useful for repeating actions
# for a set amount of times, or perform an
# action on each element of a set array

# we set up a simple for loop repeating x times
# like this:

x = 10
for iteration in range(x):
    print(iteration)

# we can loop through arrays in two ways, and
# sadly we need to know both

array = ["hi", "there", "buddy"]

for element in range(len(array)):  # len(array) means array length
    print(element)  # we use this way when we need to know the index, or position, of our element

for element in array:
    print(element)  # this is the quickest and easiest but a little limited

# that's all
