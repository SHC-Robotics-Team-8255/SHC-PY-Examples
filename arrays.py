# arrays are quite simply sets of the types of
# variables we covered in variables.py.

integer_array = [8, 2, 5, 2, 5]
string_array = ["hello", "q", "HI", "&*($&"]
boolean_array = [True, True, False, False, True]

# Arrays generally should all be the same type.
# However, this is not required, but highly recommended

# we can reference the elements of arrays individually.
# remember that the first element has the address of 0

integer_array[1]  # = 2
string_array[1]  # = "q"
boolean_array[1]  # True

# we can reference a range

integer_array[2:3]  # = [5, 2]
string_array[2:3]  # = ["HI", "&*($&"]
boolean_array[2:3]  # = [False, False]

# Arrays can have more than one dimension

multi_d_array = [
    [0, 2, 5, 8],
    [6, 1, 6, 1]
    [7, 2, 6, 7]
]

# This is a 2d array, with 3x4 size (12 elements)

# arrays can be used to define color. Color is stored as three
# integer values, from 0 to 255 (nothing to full), usually in the
# format (red, green, blue).

white = [255, 255, 255]
black = [0, 0, 0]
green = [0, 255, 0]
purple = [255, 0, 255]

# When we put these last two concepts together, we find we can represent
# images very well.

# 2x2 pixel image with color values:
# red, blue
# green, black

image = [
    [  # row one
        [255, 0, 0],  # red
        [0, 0, 255]  # blue
    ],
    [  # row two
        [0, 255, 0],  # green
        [0, 0, 0]  # black
    ]
]

# whew, that array was THREE-dimensional
# how do you think we would represent a video?
# hint: a video is a set of images


# yep, 4 dimensional! We have left the world of things we can physically model as an object
