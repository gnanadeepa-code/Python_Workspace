# Conditional statements
x = 10
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")
# Nested if
y = 5
if x > 0:
    if y > 0:
        print("x and y are positive")
    else:
        print("x is positive but y is not positive")
# Ternary operator
result = "x is positive" if x > 0 else "x is not positive"
print(result)
# Loops
# For loop
for i in range(5):  # 0 to 4
    print(i, end=' ')
print()
# For loop with else    
for i in range(5):
    print(i, end=' ')
else:
    print("\nLoop completed")
# While loop
count = 0
while count < 5:
    print(count, end=' ')
    count += 1
print()
# While loop with else
count = 0
while count < 5:
    print(count, end=' ')
    count += 1
else:
    print("\nWhile loop completed")
# Nested loops
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
# Break statement
for i in range(10):
    if i == 5:
        break
    print(i, end=' ')
print("\nLoop exited with break")
# Continue statement
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=' ')
print("\nLoop continued with continue")
# Pass statement
for i in range(5):
    if i == 3:
        pass  # Placeholder for future code
    print(i, end=' ')
print("\nLoop with pass statement")
# Nested loops with break
for i in range(3):
    for j in range(3):
        if j == 2:
            break
        print(f"i={i}, j={j}")
# Nested loops with continue
for i in range(3):
    for j in range(3):
        if j == 1:
            continue
        print(f"i={i}, j={j}")
# Nested loops with pass
for i in range(3):
    for j in range(3):
        if j == 0:
            pass  # Placeholder for future code
        print(f"i={i}, j={j}")
print("Loop with pass statement in nested loop")
# Infinite loop (commented out to prevent execution)
# while True:
#     print("This is an infinite loop")
#     break  # Just to prevent actual infinite loop during execution    
# Looping through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Looping through a string
for char in "hello":
    print(char)
# Looping through a dictionary
person = {"name": "Alice", "age": 30}
for key, value in person.items():
    print(f"{key}: {value}")
# Using range with start, stop, step
for i in range(1, 10, 2):  # Odd numbers from 1 to 9
    print(i, end=' ')
print()
for i in range(10, 0, -1):  # Countdown from 10 to 1
    print(i, end=' ')
print()
# Using enumerate in loops
for index, value in enumerate(fruits):
    print(f"Index: {index}, Value: {value}")
# Using zip in loops
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
# List comprehension with loops
squares = [x**2 for x in range(10)]
print("Squares:", squares)
# Nested list comprehension
matrix = [[j for j in range(3)] for i in range(3)]
print("Matrix:", matrix)
# Looping with conditions
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("Even Squares:", even_squares)
# Looping through a set
unique_numbers = {1, 2, 2, 3, 4, 4, 5}
for num in unique_numbers:
    print(num)