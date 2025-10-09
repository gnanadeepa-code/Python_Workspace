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
def nSum(n):
    #code here
    ans = 0
    for i in range(n):
        print("n is less than or equal to 1 :",n)
        ans += n
        print("ans is :",ans)
        n -= 1
        print("n after decrement is :",n)
    return ans
print(nSum(5))

#Different ways to calculate sum of first n natural numbers
from functools import reduce

def sum_formula(n):
    return n * (n + 1) // 2

def sum_loop(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def sum_recursion(n):
    if n == 1:
        return 1
    else:
        return n + sum_recursion(n - 1)

def sum_reduce(n):
    return reduce(lambda x, y: x + y, range(1, n + 1))

def sum_list_comprehension(n):
    return sum([i for i in range(1, n + 1)])

def main():
    print("\nChoose a method to calculate the sum:")
    print("1. Formula")
    print("2. Loop")
    print("3. Recursion")
    print("4. Reduce")
    print("5. List Comprehension")

    choice = int(input("Enter your choice (1-5): "))
    n = int(input("Enter a number: "))

    if choice == 1:
        print("Sum using formula:", sum_formula(n))
    elif choice == 2:
        print("Sum using loop:", sum_loop(n))
    elif choice == 3:
        print("Sum using recursion:", sum_recursion(n))
    elif choice == 4:
        print("Sum using reduce:", sum_reduce(n))
    elif choice == 5:
        print("Sum using list comprehension:", sum_list_comprehension(n))
    else:
        print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()