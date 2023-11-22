"""
Conditional Statements
Conditional statements allow you to execute certain pieces of code based on a condition.
The most common conditional statements are if, elif (else if), and else.

Using conditional statements, we can direct the flow of our program to execute different 
code blocks depending on the values and logic we define.
"""

# Initialize two variables for comparison
x = 20
y = 30

# 'if' statement to evaluate whether x is greater than y
# If this condition is true, the print statement inside the 'if' block will execute.
if x > y:  
    print("x is greater than y")  # Executes if x is greater than y

# 'if...else' statement to evaluate a condition and execute one block if it's true,
# and another block if it's false.
# If x is greater than y, the first print statement is executed.
# If x is not greater than y, the print statement in the 'else' block is executed.
if x > y:  
    print("x is greater than y")  
else:  
    print("x is less than or equal to y")  # Executes if x is less than or equal to y

# 'if...elif...else' statement for multiple conditions to check in sequence.
# 'if' checks whether x is greater than y, 'elif' checks if x is equal to y,
# and 'else' covers all other possibilities.
# Only the first true condition has its block executed.
if x > y:  
    print("x is greater than y")  
elif x == y:  
    print("x is equal to y")  # Executes if x is equal to y and previous condition was false
else:  
    print("x is less than y")  # Executes if both 'if' and 'elif' conditions were false

# Note: The flow of execution in a conditional statement goes from top to bottom.
# Once a true condition is found, the block beneath it is executed, and the rest
# of the conditions are not evaluated. This is why the 'else' block can only
# execute if all preceding conditions are false.
