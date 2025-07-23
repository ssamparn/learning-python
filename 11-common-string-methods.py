# Common Python String Methods

x = 10 # int type
s = 'abc' # string type
print(type(x), type(s))

# When you are working with strings, for example, you have access to a set of methods which are predefined
# actions that you can perform on your string object.
# These methods, upper() and lower() as well as the ones described below, are non-destructive.
# They don't modify the original string, but instead return a modified copy.
# For example, if we print model_output, we'll still see the original string, not the modified version.

model_output = 'AI is the future OF everyThing!'
print(model_output.upper())
print(model_output.lower())
print(model_output)

# strip(): In Python, the strip() method is used to remove leading and trailing characters (by default, whitespace) from a string.
response = '      Hello,  Human'
print(response)
print(response.strip())
print(response.replace('Hu','').strip())

#replace(): In Python, the replace() method is used to replace a specified substring with another substring in a string.
text = 'ML is a critical component of modern AI. ML techniques are advancing rapidly.'
updated_text = text.replace('ML', 'Machine Learning')
print(text)
print(updated_text)

# count(): In Python, the count() method is used to count the number of occurrences of a specified value in a string, list, tuple, or other iterable.
# For Strings
text = 'AI is the future OF everyThing!. Embrace the future of AI!'
print(text.count('AI'))  # Output: 2
print(text.count('future'))  # Output: 2

# For Lists
fruits = ["apple", "banana", "apple", "cherry"]
print(fruits.count("apple"))  # Output: 2

# split(): In Python, the split() method is used to split a string into a list based on a specified delimiter.
# Syntax: string.split(separator, maxsplit)
text = "Hello world from Python"
words = text.split()
print(words)  # ['Hello', 'world', 'from', 'Python']

# join(): In Python, the join() method is used to combine elements of an iterable (like a list or tuple) into a single string, using a specified separator.
# Syntax: separator.join(iterable)

# Join a list of words with spaces:
words = ["Hello", "world", "from", "Python"]
sentence = " ".join(words)
print(sentence)  # Output: Hello world from Python

# Join a list of words with commas:
items = ["apple", "banana", "cherry"]
csv = ",".join(items)
print(csv)  # Output: apple,banana,cherry

# Join Characters
chars = ['P', 'y', 't', 'h', 'o', 'n']
word = "".join(chars)
print(word)  # Output: Python


# removeprefix(): In Python, the removeprefix() method is used to remove a specified prefix from the beginning of a string, if it exists.
# Syntax: string.removeprefix(prefix)
text = "unhappy"
result = text.removeprefix("un")
print(result)  # Output: happy

# Note: If the prefix does not match then the output remain unchanged

# removesuffix(): To remove a suffix instead, use removesuffix()
filename = "report.pdf"
print(filename.removesuffix(".pdf"))  # Output: report
