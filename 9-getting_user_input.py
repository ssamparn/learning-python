# Getting user input:

"""
Imagine building a chatbot that can't understand a user's question, or creating an AI assistant that doesn't let users set preferences.
Without input, your code becomes a static script with no interactions.
So let's learn how to gather user input in Python and make your programs more dynamic and responsive.

Now here's an interesting aspect of input.
No matter what the user enters text, numbers, or symbols, the data is always stored as a string.
If you need to perform calculations, you'll have to convert it to type int.
"""

# Uncomment
# command = input('Ask your AI Assistant a question: ')
# print('Your question was: ', command)

# Uncomment
# training_hours = input('How many hours did you train the AI for? ')
# print('Your training hours was: ', training_hours, type(training_hours)) # Even if you enter an integer, type is still string

# Uncomment
iterations = int(input('How many iterations did you train the AI for? ')) # converting the user input to a number
datasets = int(input('How many datasets did you train the AI for? '))
total = iterations * datasets
print('Total processing units: ', total)

