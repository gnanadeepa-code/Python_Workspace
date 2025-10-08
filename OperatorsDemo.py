a = 10
b = 3

# Arithmetic Operators
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)

# Comparison Operators relational operators
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater Than:", a > b)
print("Less Than:", a < b)
print("Greater Than or Equal To:", a >= b)
print("Less Than or Equal To:", a <= b)
# Logical Operators
print("Logical AND:", a > 5 and b < 5)
print("Logical OR:", a > 5 or b > 5)    
print("Logical NOT:", not(a > 5 and b < 5))
# Assignment Operators
c = a  # c = 10
c += b # c = c + b
print("c after += :", c)
c -= b # c = c - b
print("c after -= :", c)
c *= b # c = c * b
print("c after *= :", c)
c /= b # c = c / b
print("c after /= :", c)
c %= b # c = c % b
print("c after %= :", c)
c **= b # c = c ** b
print("c after **= :", c)
c //= b # c = c // b
print("c after //= :", c)
# Bitwise Operators
x = 5  # 0b0101
y = 3  # 0b0011
print("Bitwise AND:", x & y)  # 0b0001
print("Bitwise OR:", x | y)   # 0b0111
print("Bitwise XOR:", x ^ y)  # 0b0110
print("Bitwise NOT:", ~x)      # -0b0110
print("Left Shift:", x << 1)   # 0b1010
print("Right Shift:", x >> 1)  # 0b0010
# Membership Operators
list1 = [1, 2, 3, 4, 5]
print("3 in list1:", 3 in list1)    
print("6 not in list1:", 6 not in list1)
# Identity Operators
a = 10
b = 10
print("a is b:", a is b)
print("a is not b:", a is not b)
b = 20
print("a is b after changing b:", a is b)
print("a is not b after changing b:", a is not b)
b = a
print("a is b after assigning a to b:", a is b)
print("a is not b after assigning a to b:", a is not b)
# Operator Precedence
result = a + b * 2  # Multiplication first, then addition   
print("Result of a + b * 2:", result)
result = (a + b) * 2  # Parentheses change precedence   
print("Result of (a + b) * 2:", result)
# Ternary Operator
max_value = a if a > b else b
print("Maximum value using ternary operator:", max_value)
# Chained Comparison
x = 15
print("10 < x < 20:", 10 < x < 20)  # True
print("10 < x < 15:", 10 < x < 15)  # False
print("10 <= x <= 15:", 10 <= x <= 15)  # True
print("10 < x <= 15:", 10 < x <= 15)  # False
print("10 <= x < 15:", 10 <= x < 15)  # False
print("10 < x < 25:", 10 < x < 25)  # True
print("10 <= x < 25:", 10 <= x < 25)  # True
print("10 < x <= 25:", 10 < x <= 25)  # True
print("10 <= x <= 25:", 10 <= x <= 25)  # True
# Augmented Assignment with Multiple Operators  
d = 5
d += 3  # d = d + 3
print("d after += 3:", d)
d *= 2  # d = d * 2 
print("d after *= 2:", d)
d -= 4  # d = d - 4
print("d after -= 4:", d)
d /= 2  # d = d / 2
print("d after /= 2:", d)
d **= 3 # d = d ** 3
print("d after **= 3:", d)
d //= 4 # d = d // 4
print("d after //= 4:", d)
d %= 3  # d = d % 3
print("d after %= 3:", d)
# Combining Logical and Comparison Operators
a = 10
b = 20
c = 15
print("a < b and b > c:", a < b and b > c)
print("a < b or b < c:", a < b or b < c)
print("not(a < b and b > c):", not(a < b and b > c))
print("a < b < c:", a < b < c)  # Chained comparison    --False
print("a < b > c:", a < b > c)  # Chained comparison    --True
print("a < b <= c:", a < b <= c)  # Chained comparison  --False         
