#Python Basics
#Single line comment

print("Hello World :)")
#String replication
print("*Deepa*" * 10)
#String concatenation
print("Gnana" + "Deepa" )
print('''THIS IS 
MULTIline string with 3 quotes. 
without giving escape character.''')

#\a makes a sound
print('\a')
#\n - new line . \t tab space

print("you are best. \n hello","world")

#separation argument instead of default space we can replace it
print("hello","world",sep='_',end="\t")

#End argument by default is new line to print next statement , but we can replace it
print("End argument used with tab escape character instead of new line")

##### Testing code snippets ##########
x = 123  # global variable

def display():
    print("Inside display function")
   # print("X before local variable declaration x:",x)  # accesses global x
    x = 98  # local variable
    print("X after local variable declaration x:",x)   # accesses local x
    print(globals()['x'])  # accesses global x

print(x) 

a = display  # assign function to a variable
a()  # call function
print(x)
