"""
Loops
Loops allow you to execute a block of code multiple times. Python has two primitive loop commands:

- for loops: Iterate over a sequence such as a list, tuple, dictionary, set, or string.
- while loops: Execute a set of statements as long as a condition is true.
"""

# Example of a 'for' loop over a list:
# This loop will print each item in the fruits list one by one.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Example of a 'for' loop using 'range':
# This will print numbers 0 to 5 as range generates numbers from 0 up to (but not including) 6.
for x in range(6):
    print(x)

# Example of a 'for' loop with a specified starting point:
# Range starts at 2 and goes up to (but not including) 6, so this prints numbers 2 to 5.
for x in range(2, 6):
    print(x)

# Example of a 'for' loop with a range and a step value:
# Starts at 2, increments by 3 each time, and stops before reaching 30.
for x in range(2, 30, 3):
    print(x)

# Example of a 'for' loop with an 'else' statement:
# The else block is executed after the loop completes its iteration over the range.
for x in range(6):
    print(x)
else:
    print("Finally finished!")

# Example of a nested 'for' loop:
# Combines each adjective with each fruit, resulting in a print out of every possible combination.
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)

# Example of a 'for' loop with a 'break' statement:
# The loop will exit as soon as it encounters the fruit "banana".
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

# Example of a 'for' loop with a 'continue' statement:
# The continue statement causes the loop to skip the rest of its body and move on to the next iteration if it encounters "banana".
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# Example of a 'for' loop with 'range' that uses a 'break' statement:
# This loop will print numbers from 0 to 3 and then break, so it won't print 4 or 5.
for x in range(6):
    print(x)
    if x == 3:
        break

# Example of a 'for' loop with 'range' that uses a 'continue' statement:
# This loop skips printing the number 3 but continues with the rest of the range.
for x in range(6):
    if x == 3:
        continue
    print(x)
