"""
Python String:
Python string is an ordered sequences of characters enclosed in either single quotes ('...') or double quotes ("...").
They are one of the most commonly used data types in Python and support a wide range of operations.
"""
model_summary = 'This AI model predicts stock trends'
prediction_message = "AI will revolutionalize industries!"

print(model_summary)
print(prediction_message)

# What id there is a single quote inside a string

# 1. Use backslash \
first_fix = 'AI says, I\'m here to assist you'

# 2. Use double quotes
second_fix = "AI says, I'm here to assist you"

print(first_fix)
print(second_fix)

# Create a multiline string. To create a multiline string use '''
ai_response = """
Hello There!
I'm here to assist you
Feel free to ask me anything
"""
print(ai_response)

# Another way to write multiline string
ai_prompt = 'Hello There! \nI\'m here to assist you\nFeel free to ask me anything'
print(ai_prompt)

# Note: Python string are UTF-8 encoded by default, so they support characters from various languages and also emojis.

