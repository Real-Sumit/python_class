#Operators in python

a = 10
b = 3

# Arithmetic operators
print(a + b)   # 13: addition
print(a - b)   # 7: subtraction
print(a * b)   # 30: multiplication
print(a / b)   # 3.333...: division
print(a // b)  # 3: floor division
print(a % b)   # 1: modulus (remainder)
print(a ** b)  # 1000: exponentiation

# Comparison operators
print(a == b)  # False: equal to
print(a != b)  # True: not equal to
print(a > b)   # True: greater than
print(a < b)   # False: less than
print(a >= b)  # True: greater than or equal to
print(a <= b)  # False: less than or equal to

# Logical operators
print(a > 5 and b < 5)  # True: and
print(a > 5 or b > 5)   # True: or
print(not (a > 5))      # False: not

# Assignment operators
number = 5               # = assigns a value
number += 2
print(number)            # 7: += adds and assigns
number -= 1
print(number)            # 6: -= subtracts and assigns
number *= 2
print(number)            # 12: *= multiplies and assigns
number /= 3
print(number)            # 4.0: /= divides and assigns

# Bitwise operators
print(5 & 3)   # 1: bitwise AND
print(5 | 3)   # 7: bitwise OR
print(5 ^ 3)   # 6: bitwise XOR
print(~5)      # -6: bitwise NOT
print(5 << 1)  # 10: left shift
print(5 >> 1)  # 2: right shift

# Membership operators
print("p" in "python")      # True: in
print("z" not in "python")  # True: not in

# Identity operators
first = [1, 2]
second = first
third = [1, 2]
print(first is second)      # True: same object
print(first is not third)   # True: different objects

# Conditional expression
print("even" if a % 2 == 0 else "odd")  # even