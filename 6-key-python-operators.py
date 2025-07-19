"""
In Python, assignment operators are used to assign values to variables.
The most basic one is =, but there are several compound assignment operators that combine an operation with assignment.

🧾 Basic Assignment
x = 10

This assigns the value 10 to the variable x.

🔁 Compound Assignment Operators:

Operator	    Example	     Equivalent To	      Description
--------------------------------------------------------------------------------
 +=	            x += 5	      x = x + 5	         Add and assign
--------------------------------------------------------------------------------
 -=	            x -= 3	      x = x - 3	       Subtract and assign
--------------------------------------------------------------------------------
 *=	            x *= 2	      x = x * 2	       Multiply and assign
--------------------------------------------------------------------------------
 /=	            x /= 4	      x = x / 4	       Divide and assign (float result)
--------------------------------------------------------------------------------
 //=	        x //= 2	      x = x // 2	   Floor divide and assign
--------------------------------------------------------------------------------
 %=	            x %= 3	      x = x % 3   	   Modulus and assign
--------------------------------------------------------------------------------
 **=	        x **= 2	      x = x ** 2	   Exponentiate and assign
--------------------------------------------------------------------------------
 &=	            x &= y	      x = x & y	       Bitwise AND and assign
--------------------------------------------------------------------------------
 `	              =`	       `x	                 = y`
--------------------------------------------------------------------------------
 ^=	            x ^= y	      x = x ^ y	       Bitwise XOR and assign
--------------------------------------------------------------------------------
 >>=	        x >>= 1 	  x = x >> 1	   Bitwise right shift and assign
--------------------------------------------------------------------------------
 <<=	        x <<= 1	      x = x << 1	   Bitwise left shift and assign
--------------------------------------------------------------------------------

🧮 List of Comparison Operators:

Operator	     Description	                Example	     Result        |
---------------------------------------------------------------------------|
  ==	            Equal to	                5 == 5	       True
---------------------------------------------------------------------------|
  !=	          Not equal to	                5 != 3	       True
---------------------------------------------------------------------------|
   >	         Greater than	                5 > 3	       True
---------------------------------------------------------------------------|
   <	           Less than	                5 < 3	       False
---------------------------------------------------------------------------|
  >=	      Greater than or equal to          5 >= 5	       True
---------------------------------------------------------------------------|
  <=	        Less than or equal to           3 <= 5	       True
---------------------------------------------------------------------------|
  is	       Identity (same object)	        a is b	      True/False
---------------------------------------------------------------------------|
 is not	        Not the same object	           a is not b	  True/False
---------------------------------------------------------------------------|
   in	        Membership (in a sequence)	  'a' in 'cat'	    True
---------------------------------------------------------------------------|
 not in	        Not in a sequence	        'x' not in 'cat'	True
---------------------------------------------------------------------------|

🔍 Identity vs Equality:
In Python, identity operators are used to compare whether two variables refer to the same object in memory, not just whether they have the same value.

🆔 Identity Operators: (is & is not)

Operator	                     Description	                             Example	      Result
--------------------------------------------------------------------------------------------------------|
  is	         Returns True if both variables point to the same object	 a is b	     True or False
--------------------------------------------------------------------------------------------------------|
 is not	         Returns True if they do not point to the same object	    a is not b	 True or False
--------------------------------------------------------------------------------------------------------|

If id(a) and id(b) turned out to be same value, then a is b would be true. id() gives the memory location of a variable.
"""
print('Start Identity operators test')
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a == c)    # True  (same content)
print(a is c)    # False (different objects)
print(a is b)    # True  (same object)
print(id(a), id(b), id(c))
print('End Identity operators test')

print('Start Compound assignment operators test')
a = 5
a += 2 # same as a = a + 2 = 7
print(a)

a -=4 # same as a = a - 4 = 3
print(a)

a *= 10 # same as a = a * 10 = 30
print(a)
print('End Compound assignment operators test')


print('Start Comparison operators test')
x, y = 10, 20

print(x == y)               # False
print(x != y)               # True
print(x < y)                # True
print(x >= 10)              # True
print('a' in 'cat')         # True
print('b' in 'cat')         # False
print(1 in [1, 2, 3, 4, 5]) # True

print('End Comparison operators test')