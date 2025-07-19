"""
🔢 Number Types in Python:
    1. Integers (int) – Whole numbers:
    x = 10

    2. Floating-point (float) – Decimal numbers:
    x = 3.14

    3. Complex numbers (complex) – With real and imaginary parts
    z = 2 + 3j


➕➖✖️➗    Math Operators:
------------------------------------------------------
Operator  |  Description	     |  Example	| Result |
-----------------------------------------------------|
+	      | Addition	         |   5 + 3	|   8    |
-----------------------------------------------------|
-	      | Subtraction	         |   5 - 3	|   2    |
-----------------------------------------------------|
*	      | Multiplication	     |   5 * 3	|   15   |
-----------------------------------------------------|
/	      | Division (float)     |   8 / 2  |  4.0   |
-----------------------------------------------------|
//	      | Floor Division	     |   5 // 2	|   2    |
-----------------------------------------------------|
%	      | Modulus (remainder)	 |   5 % 2	|   1    |
-----------------------------------------------------|
**	      | Exponentiation       |  2 ** 3  |   8    |
------------------------------------------------------

Python Operator precedence:
In Python, operator precedence determines the order in which operations are evaluated in an expression.
Operators with higher precedence are evaluated before those with lower precedence.

🧮 Python Operator Precedence (Highest to Lowest)

Precedence Level	Operators	                                Description
-----------------------------------------------------------------------------------------------------------
1️⃣ (Highest)          ()	                                    Parentheses – override all other precedence
2️⃣	                  **	                                    Exponentiation
3️⃣	              +x, -x, ~x	                                Unary plus, minus, bitwise NOT
4️⃣	              *, /, //, %	                                Multiplication, Division, Floor Division, Modulus
5️⃣	                 +, -	                                    Addition, Subtraction
6️⃣	                <<, >>	                                    Bitwise shift operators
7️⃣	                   &	                                    Bitwise AND
8️⃣	                   ^	                                    Bitwise XOR
9️⃣	                   `
🔟	       ==, !=, >, <, >=, <=, is, is not, in, not in	        Comparisons, identity, membership
11️⃣	                  not	                                    Logical NOT
12️⃣	                  and	                                    Logical AND
13️⃣	                  or	                                    Logical OR
14️⃣ (Lowest)   =, +=, -=, etc.	                                Assignment operators


🧪 Example:

result = 3 + 4 * 2 ** 2
# Step-by-step:
# 2 ** 2 = 4
# 4 * 4 = 16
# 3 + 16 = 19

To force a different order, use parentheses:
result = (3 + 4) * 2 ** 2  # (7) * 4 = 28


🧮 Useful Math Functions
Python has a built-in math module for more advanced operations:

    import math

    math.sqrt(16)       # 4.0
    math.pow(2, 3)      # 8.0
    math.sin(math.pi/2) # 1.0
    math.log(10)        # Natural log
    math.log10(100)     # Base-10 log
"""