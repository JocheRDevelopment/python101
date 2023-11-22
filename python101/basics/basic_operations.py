"""
Arithmetic operators: Used with numeric values to perform common mathematical operations.
Assignment operators: Used to assign values to variables.
Comparison operators: Used to compare two values.
Logical operators: Used to combine conditional statements.
Identity operators: Used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.
Membership operators: Used to test if a sequence is presented in an object.
Bitwise operators: Used to compare (binary) numbers on a bit level.

Arithmetic Operators
Arithmetic operators are used with numeric values to perform common mathematical operations:

Operator	Name	        Example
+	        Addition	    x + y
-	        Subtraction	    x - y
*	        Multiplication	x * y
/	        Division	    x / y
%	        Modulus	        x % y
**	        Exponentiation	x ** y
//	        Floor division	x // y

Assignment Operators
Assignment operators are used to assign values to variables:

Operator	Example	    Same As
=	        x = 5	    x = 5
+=	        x += 3	    x = x + 3
-=	        x -= 3	    x = x - 3
*=	        x *= 3	    x = x * 3
/=	        x /= 3	    x = x / 3
%=	        x %= 3	    x = x % 3
//=	        x //= 3	    x = x // 3
**=	        x **= 3	    x = x ** 3
&=	        x &= 3	    x = x & 3
|=	        x |= 3	    x = x | 3
^=	        x ^= 3	    x = x ^ 3
>>=	        x >>= 3	    x = x >> 3
<<=	        x <<= 3	    x = x << 3

Comparison Operators
Comparison operators are used to compare two values:

Operator	Name                        Example
==	        Equal                       x == y
!=	        Not equal	                x != y
>	        Greater than                x > y
<	        Less than	                x < y
>=	        Greater than or equal to	x >= y
<=	        Less than or equal to	    x <= y

Logical Operators
Logical operators are used to combine conditional statements:

Operator	Description                                                     Example
and 	    Returns True if both statements are true	                    x < 5 and  x < 10
or	        Returns True if one of the statements is true	                x < 5 or x < 4
not	        Reverse the result, returns False if the result is true	        not(x < 5 and x < 10)

Identity Operators
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

Operator	Description	                                                Example
is 	        Returns True if both variables are the same object	        x is y
is not	    Returns True if both variables are not the same object	    x is not y

Membership Operators
Membership operators are used to test if a sequence is presented in an object:

Operator	Description	                                                                        Example
in 	        Returns True if a sequence with the specified value is present in the object	    x in y
not in	    Returns True if a sequence with the specified value is not present in the object	x not in y
"""

"""
This file demonstrates the use of various operators in Python including arithmetic,
assignment, comparison, logical, identity, and membership operators.
"""

# Arithmetic Operators
# Set initial values for variables x and y
x = 10
y = 3

# Perform arithmetic operations and print the results
print("x + y =", x + y)  # Addition: Outputs 13
print("x - y =", x - y)  # Subtraction: Outputs 7
print("x * y =", x * y)  # Multiplication: Outputs 30
print("x / y =", x / y)  # Division: Outputs approximately 3.3333
print("x % y =", x % y)  # Modulus: Outputs 1 (remainder of division)
print("x ** y =", x ** y)  # Exponentiation: Outputs 1000 (x raised to the power of y)
print("x // y =", x // y)  # Floor division: Outputs 3 (division without remainder)

# Assignment Operators
# Use assignment operators to change the value of x
x += 3  # Addition assignment: x is now 13
print("x after x += 3 is", x)
x -= 3  # Subtraction assignment: returns x to 10
print("x after x -= 3 is", x)
x *= 3  # Multiplication assignment: x is now 30
print("x after x *= 3 is", x)
x /= 3  # Division assignment: x is now approximately 10.0
print("x after x /= 3 is", x)
x %= 3  # Modulus assignment: x is now the remainder of 10/3 which is 1
print("x after x %= 3 is", x)
x **= 3  # Exponentiation assignment: x is now 1 raised to the power of 3 which is 1
print("x after x **= 3 is", x)
x //= 3  # Floor division assignment: x is now 1 // 3 which is 0 (since 1/3 is less than 1)
print("x after x //= 3 is", x)

# Reset x to 10 for comparison operations
x = 10

# Comparison Operators
# Compare x and y and print the results
print("x == y is", x == y)  # Equal: False
print("x != y is", x != y)  # Not equal: True
print("x > y is", x > y)   # Greater than: True
print("x < y is", x < y)   # Less than: False
print("x >= y is", x >= y)  # Greater than or equal to: True
print("x <= y is", x <= y)  # Less than or equal to: False

# Logical Operators
# Combine boolean expressions and print the results
print("(x > 5) and (x < 15) is", (x > 5) and (x < 15))  # Logical AND: True
print("(x > 5) or (x < 15) is", (x > 5) or (x < 15))    # Logical OR: True
print("not((x > 5) and (x < 15)) is", not((x > 5) and (x < 15)))  # Logical NOT: False

# Identity Operators
# Use identity operators to compare objects' identities
z = x  # z is now the same object as x
print("x is z:", x is z)  # True because x and z are the same object
print("x is y:", x is y)  # False because x and y are not the same object (even if their values are the same)

# Membership Operators
# Use membership operators to check for membership in a sequence
fruits = ["apple", "banana"]
print("'banana' in fruits:", "banana" in fruits)  # True because 'banana' is in the list of fruits
print("'pineapple' not in fruits:", "pineapple" not in fruits)  # True because 'pineapple' is not in the list

# Note: Bitwise operators are not included as they are beyond the scope of a basic Python course.
