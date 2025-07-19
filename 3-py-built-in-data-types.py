# python's built in data types
from ipaddress import ip_address

# 1. Numbers: int & float
age = 40
print(age)

temperature = 20.1
print(temperature)

# 2. Booleans: Logical values, True or False (T in True & F in False are uppercase)
print(age == 40)
print(temperature < 20)

# 3. None: Represents the absence of a value. Commonly indicates the no-return or no-results value.

# 4. String: Ordered sequences of characters, stored in UTF-8 encoding.
model_name = 'Gemini'
print(model_name, type(model_name))

# 5. Lists: Ordered, mutable sequences of objects. Mutable means list object can change after it is created.
person_list = ['Dan', 40, 82.5, True] # list  type
print(person_list, type(person_list))

# 6. Tuples: Ordered, immutable sequences of objects. Immutable means object can never change after it is created.
coordinates = (40.7128, -74.0060) # tuple  type (NYC latitude and longitude)
print(coordinates, type(coordinates))

# 7. Sets: Mutable collections of unordered, unique objects
ip_addresses = {'100.0.0.1', '80.1.1.2'}
print(ip_addresses, type(ip_addresses))

# 8. FrozenSets: Immutable collections of unordered, unique objects
frozen_user_ids = frozenset([1001, 1002, 2003, 2004]) # frozen set type
print(frozen_user_ids, type(frozen_user_ids))

# 9. Dictionaries: Collections of unordered key-value pairs
person = {'name': 'Alice', 'age': 30, 'is_employed': True}
print(person, type(person))


