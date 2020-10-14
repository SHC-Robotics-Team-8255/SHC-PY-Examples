
# operators can be used to compare or modify variables
# for a more complete list, visit:
# https://www.w3schools.com/python/python_operators.asp

# conditional operators compare two things and then
# evalute to True or False

my_name = "jack"  # no its not but pretend it is

# to compare, we can use "==" or "is". Remember to use
# two equal signs otherwise python will think you want
# to REASSIGN the variable, not compare

is_my_name_jack = my_name == "jack"
is_my_name_jack = my_name is "jack"  # both of these do the same: compare my_name and "jack"

print(is_my_name_jack)  # True!

# this works with numbers too

number = 10

# using "is" here is not recommended
is_the_number_9 = number == 9

print(is_the_number_9)  # False!

# There are quite a few conditional operators:
# == : equality
# != : non-equality
# > : greater than
# >= : greater than or equal to
# < : lesser than
# <= : lesser than or equal to

# Other operators can modify, not just compare

# Addition of values and/or variables: "+"
welcome_message = "Hello, " + my_name  # strings can only use addition operators
nine_plus_ten = 9 + 10

# Subtraction (-)
five_minus_two = 5 - 2
twelve_minus_number = 12 - number

# Multiplication (*)
eight_times_six = 8 * 6

# Division (/)
ugly_decimal = 1 / 3

# There is a shortcut for a specific case

price = 10.0

price = price + 2.0  # this isnt very cool

# so lets fix it

price += 2.0  # completely equivalent and shorter- great!

# this works with all the math operators

price -= 2.0
price *= 10
price /= 5

# now price == 60 or something like that i dont know

# % : remainder operator (modulus)

# 3 % 2 = 1
# 4 % 4 = 0
# 10 % 3 = 1
# 11 % 12 = 11
# 6 % 4 = 2

price %= 7  # works too
