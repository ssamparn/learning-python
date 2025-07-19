'''
🔢 Using is with Integers:
Python caches integers, so variables assigned the same integer point to the same object in memory.

So:
a == b → compares values → True

📦 Using is with Lists:
Lists are mutable, and Python does not automatically reuse list objects, even if they have the same content.
'''
print('Start: is with Integers test')
a = 100
b = 100
print(a is b)   # True

x = int("1000")
y = int("1000")
print(x is y)   # False

print('End: is with Integers test')


print('Start: is with list test')
list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1 == list2)  # True (same content)
print(list1 is list2)  # False (different objects)

list3 = list1
print(list1 is list3)  # True (same object)
print('End: is with list test')