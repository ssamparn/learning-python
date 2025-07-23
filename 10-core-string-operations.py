# Core String Operations: Indexing, Slicing, Concatenating

# 1. Indexing String: A string is an ordered sequence of UTF-8 encoded characters.
# my_string = 'P Y T H O N'
# index:       0 1 2 3 4 5

my_string = 'PYTHON'
print('Positive Indexing Starts')
print(my_string[0])
print(my_string[1])
print(my_string[2])
print(my_string[3])
print(my_string[4])
print(my_string[5])
print('Positive Indexing Ends')

# 2. Python also let us use negative index to count or iterate backwards. There is no minus zero (-0) while doing negative indexing.
print('Negative Indexing Starts')
print(my_string[-1])
print(my_string[-2])
print(my_string[-3])
print(my_string[-4])
print(my_string[-5])
print(my_string[-6])
print('Negative Indexing Ends')

# If you try to access an index beyond the range of the string, then you will get an error.
# print(my_string[20]) # IndexError: string index out of range

# Note: To avoid this, we can use the len function to get the length of the string ensuring we always stay within bounds.
n = len(my_string)
print(my_string[0:n])

# 3. Python strings are immutable, meaning they can't be modified directly.
# my_string[0] = 'X' # TypeError: 'str' object does not support item assignment

# 4. Concatenation of Strings: Combining strings.
# Concatenation is straightforward. We use the plus (+) operator to join two or more strings into a new one.
greeting = 'Hello'
role = 'AI Enthusiast'
print(greeting + ', ' + role + '!')

# Pay attention that you can't concatenate a string with a number directly. This will throw an error.
# print('Version' + 4) # TypeError: can only concatenate str (not "int") to str

# To combine a string with a number like version and 4.0, you first need to convert the number to a string.
# You do that by calling the built-in str function.
print('Version ' + str(4))

# 5. Repeating Strings: This can be handy for creating patterns or emphasizing a response.
# We use the star operator (*) to repeat a string.
separator = '\U0001F603'
print(separator * 5)

# 5. Slicing of Strings: Slicing allows to grab a range of characters known as a substring within a string.
tech = 'Machine Learning'
print(tech[:7]) # Machine
print(tech[0:7]) # Machine
print(tech[8:len(tech)]) # Learning
print(tech[8:]) # Learning
print(tech[8:1000]) # Learning

# Note: The syntax for slicing is: String[start : stop : step]
# In square brackets, where start is the index to begin at and is inclusive & stop is where to end and is exclusive.
# If you omit start, Python assumes it's zero, and if you omit stop, Python goes to the end of the string.
# A cool feature of slicing is that it doesn't throw an error if the slices go beyond the length of the string.

# The third argument in slicing is the step. It allows us to skip characters.
# For example, if we want every 2nd character in machine learning, we do like below.
print(tech[::2])

# To reverse a string in python is really easy.
print(tech[::-1])








