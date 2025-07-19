# pyhon variable naming conventions (pep8)

# 1. Allowed characters (a to z, A to Z, 0 to 9, and _)
total_count = 100 # valid

# 1st_place = 'Gold' # invalid, starts with a digit

# 2. Avoid Leading Underscores
_hidden_value = 42 # valid, but not recommended

# 3. No special characters or spaces (!, %, @, ?, ., etc)
# user-name = 'Alice' # invalid
# user name = 'Alice' # invalid

# 4. Reserved keywords (if, else, while, for)
# if = 10 # invalid, as if is a language keyword

# 5. Case Sensitivity. Be consistent in the usage of uppercase or lowercase letters to avoid confusion.
# It's common practice to use only lowercase letters for variable names.

# 6. Use descriptive Names and snake_case while naming variables.
max_value = 99 # valid as this is snakecase
total_count = total_count + _hidden_value # valid as this is snakecase
# maxValue = 'this is camelcase'

# 7. Don't shadow built-in names
# list = [1, 2, 3] # not recommended, as list is a built-in type in python.

# 8. In Python, there is not a built-in way to enforce constants.
# However, by convention we indicate that a variable is meant to be a constant by writing its name in all uppercase letters.
PI = 3.1415926
DAYS_IN_YEAR = 365
MAX_CONNECTIONS = 10
# While Python won't prevent you from changing these values, writing them in uppercase servers as signal to anyone reading your code
# that these variables are intended to remain constant.

# By adhering to the guidelines from pep8, you will make your code more readable and professional,
# which is especially important while collaborating with others or contributing to opensource projects.










