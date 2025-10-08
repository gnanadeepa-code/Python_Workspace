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

##### Testing code snippets ##########
x = input("Enter a number: ")  # Taking input from user
y = input("Enter another number: ")  # Taking input from user
print(type(x), type(y)) # By default input is string
print(x+y)  # Concatenation of strings
x = int(x)  # Type casting to integer
print(x+5)
