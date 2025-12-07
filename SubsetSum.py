'''
Input: arr[] = [5, 6, 7]
Output: [0, 5, 6, 7, 11, 12, 13, 18]
Explanation: The possible subset sums are 0 (no elements), 5, 6, 7, and their combinations.'''
def subset_sums(arr):
    n = len(arr)
    print("Input array:", arr)
    print("Number of elements in array:", n)
    result = set()
    for i in (arr):
        print("Processing element:", i)
        result.add(i)
        print("Current subset sums:", result)
        current_sums = list(result)
        print("Current sums to be combined with", i, ":", current_sums)
        for s in current_sums:
            result.add(s + i)
            print("Adding new subset sum:", s + i)
    result.add(0)  # Adding the sum of the empty subset
    print("Final subset sums including empty subset:", result)

#subset_sums([5, 6, 7])

def factorial(n):
    tot=1
    if n == 0:  # Base case
        print("Reached base case with n =", n)
        print("tot =", tot)
        return 1
    else:       # Recursive case
        print("Calculating factorial of", n)
        tot = n * factorial(n - 1)
        print("Intermediate tot for n =", n, "is", tot)
        return tot

print(factorial(5))

a="Deepa"
a.count