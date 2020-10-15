
# IF statements allow us to check a value and act accordingly
# we can use conditional operators to check equality

# if condition:
#     action()

# check operators.py for more information on conditional operators

password = "password123"

if password == "password123":
    print("password correct")  # this part is indented, so it is part of the conditional
print("this will be printed regardless")  # is part is not, so it is run every time

# you can also use the reserved word "is"

if password is "password123":
    print("this works too")

# this only really works with strings though! 

# we can check numbers too-

number = 10
if number > 1:
    print("the number is greater than 1")

# we can also define actions for when the condition is not true

if number <= 9:
    print("the number less than or equal to 9")
else:
    print("the number is not equal to 9")

# we can also define additional checks

if number < 10:
    print("the number is less than 10")
elif number == 10:
    print("the number is equal to 10")
else:
    print("the number is greater than 10")  # since we have checked all other possibilities, this MUST be true


# if we check boolean values, we can simplify our statement

this_is_true = True
if this_is_true == True:
    print("It is true! But this is bad form")

# This is redundant, since "True" is already "True", there is
# no point in checking if it is "True". Just do

if this_is_true:
    print("It is true! And in good form")

# if statements are powerful and are critical in every
# coding language ever made. In fact, a language is not
# considered "complete" until these exist
