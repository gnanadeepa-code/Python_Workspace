""" # Python 3.x program to check if an array consists 
# of even number
def contains_even_number(l):
    for ele in l:
        if ele % 2 == 0:
            print ("list contains an even number")
            break

    # This else executes only if break is NEVER
    # reached and loop terminated after all iterations.
    else:     
        print ("list does not contain an even number")

# Driver code
print ("For List 1:")
contains_even_number([1, 9, 8])
print (" \nFor List 2:")
contains_even_number([1, 3, 5])

count = 0
while (count < 1):    
    count = count+1
    print(count)
    break
else:
    print("No Break")

# Print multiplication table of 3
n = 3

for i in range(1, n + 1):
    for j in range(1, 11):
        print(i * j, end=' ')
    print()

# Function to print powers of 2

def printIncreasingPower(x):
    #code here
    print("Powers of 2 are: ",x)
    num = int(x)
    i = 1
    # Loop to jump in powers of 2
    while(i <= num):
        #code here
        y =  i*i
       # print ("value:",y)
        if(y<=num):
           #  print ("y:",y, "i:",i,"num:",num)
             print(y, end = ' ')
             i += 1
        else:
            break

        #code here

printIncreasingPower(10)

#User function Template for python3
n = int(input())

# Your code here
for i in range(1,11):
    print(n*i,end=' ') 

                       

class Solution:
    # Function to calculate factorial of a number.
    def factorial(self, n: int) -> int:
        # code here
        print("n:",n)
        tot = 1
        for i in range(1,n+1):
            tot *= i
            print("i:",i,"tot:",tot)
        return tot

ob = Solution()
print(ob.factorial(5))    """

# Your code here
def printStar(n):
    for i in range(1,n+1):
       # print("inside for i:",i)
        if(i==1 or i==n):
           # print("inside if i:",i)
            print("* " * n)
        else:
           # print("inside else i:",i)
            print("* " +"  " * (n-2) + "*")

printStar(5)


    