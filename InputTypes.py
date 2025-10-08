#Python Basics
#Single line comment

print("Hello World :)")
#String replication
print("*Deepa*" * 10)
#String concatenation
print("Gnana" + "Deepa" )
print('''THIS IS 
MULTIline string with 3 quotes. 
without giving escape charater.''')

#\a makes a sound
print('\a')
#\n - new line . \t tab space

print("you are best. \n hello","world")

#separation argument instead of default space we can replace it
print("hello","world",sep='_',end="\t")

#End argument by default is new line to print next statement , but we can replace it
print("End argument used with tab escape character instead of new line")

#Datatypes
#Variables are case sensitive
#Variable names should not start with number or special character except _
a="Deepa" #String
b=10 #Integer
c=10.5 #Float
d=3+4j #Complex
e=True #Boolean
f=None #NoneType
print(type(a),type(b),type(c),type(d),type(e),type(f))
#Type casting
x=10
y=5.5
z="20"
print(type(x),type(y),type(z))
#implicit type casting
x=x+y #int + float = float . THis is type promotion
print(type(x))
#explicit type casting
x=float(x) #int to float
y=int(y) #float to int
z=int(z) #string to int
print(type(x),type(y),type(z))
print(x,y,z)
#input function
name=input("Enter your name: ")
age=input("Enter your age: ")
print("Hello",name,"you are",age,"years old")
#By default input function takes input as string
#Type casting input
age=int(input("Enter your age: "))  
print("Next year you will be",age+1,"years old")
#Multiple inputs
x,y,z=input("Enter 3 values separated by space: ").split()
print("Values are:",x,y,z)
#Type casting multiple inputs   
x,y,z=map(int,input("Enter 3 values separated by space: ").split())
print("Values are:",x,y,z)

#Taking list as input from user
li = input("Enter elements separated by space: ").split()
print("List:", li)

# Taking list of integers as input from user
a = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    a.append(element)

print("List:", a)
print("List type:", type(a))

li = [x.split(",") for x in input("Enter nested list (use commas and semicolons): ").split(";")]
print("Nested List:", li)   

"""
Great question, Deepa! Let's break down the difference between these two Python expressions:

---

### 🧠 1. `map(int, input("Enter 3 values separated by space: ").split())`

- **Purpose**: Converts each value from the input string into an integer.
- **How it works**:
  - `input(...)` → gets a string like `"10 20 30"`
  - `.split()` → splits it into a list: `["10", "20", "30"]`
  - `map(int, ...)` → applies `int()` to each item: `[10, 20, 30]` (as a map object)

✅ **Use case**: When you want to read multiple integers at once.

```python
a, b, c = map(int, input("Enter 3 values separated by space: ").split())
```

---

### ❌ 2. `int(input("Enter 3 values separated by space: ").split())`

- **Purpose**: Tries to convert a **list** directly into an integer.
- **How it works**:
  - `input(...)` → gets a string like `"10 20 30"`
  - `.split()` → becomes `["10", "20", "30"]`
  - `int(...)` → throws an error because `int()` can't convert a list directly.

🚫 **Result**: Raises a `TypeError` like:
```plaintext
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
```

---

### 🔍 Summary

| Expression | Behavior | Works? | Use Case |
|-----------|----------|--------|----------|
| `map(int, input().split())` | Converts each input to int | ✅ Yes | Reading multiple integers |
| `int(input().split())` | Tries to convert list to int | ❌ No | Invalid usage |

---

If you're building full-stack apps and handling form inputs, this kind of parsing will come in handy. Want a quick cheat sheet for common input patterns in Python?

Basic Input Patterns
1. Single Integer
n = int(input("Enter a number: "))


2. Multiple Integers (space-separated)
a, b, c = map(int, input("Enter 3 numbers: ").split())


3. List of Integers
nums = list(map(int, input("Enter numbers: ").split()))



🔠 String Input Patterns
4. Single String
name = input("Enter your name: ")


5. Multiple Strings (space-separated)
first, last = input("Enter first and last name: ").split()


6. List of Strings
words = input("Enter words: ").split()



📋 Mixed Input Patterns
7. Integer + String
age, name = input("Enter age and name: ").split()
age = int(age)


8. Tuple of Inputs
data = tuple(map(int, input("Enter values: ").split()))



🧮 Advanced Input Patterns
9. 2D List (Matrix)
rows = int(input("Enter number of rows: "))
matrix = [list(map(int, input().split())) for _ in range(rows)]


10. Dictionary from Input
pairs = input("Enter key:value pairs separated by space: ").split()
d = dict(pair.split(":") for pair in pairs)




"""
