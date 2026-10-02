""" name = input("What is your name? ")
print("Nice to meet you, " + name)
age = int(input("What is your age? "))
print(f"Oh its good to know  {age}")
address = input("What is your address? ")
print("Really your adress is  %s" %(address) ) """
""" 
 name ="Odysses" #name of the user 
age =19 #age of the user
location="Ktm" #location of the user

print("My name is " + name + "my age is" + str(age) + "address is" + location) # Printing all the information using concate

print (f"My name is {name} and my age is {age} and address is {location}") # Printing all the information using f-string

print("my name is %s and age is %d and address is %s " %(name,age,location)) # Printing all the information using % formatting

print("My name is {0} and age is {1}" . format(name,age)) # Printing all the information using .format() """

# This is single-line comment using +/

"""  This is multiple line comment, shift+alt+A  """

""" num1 = int(input("Enter first number: "))
num2 = int(input("ENter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))

sum1 = num1 + num2
print(f"The sum of first 2 numbers is: {sum1}" )

sum2 = num3 + num4
print(f"The sum of last 2 numbers is: {sum2} and its type is {type(sum2)}") """
 # This will return True because 0.1 is a non-zero value

#2nd class one
print(chr(67))

username= "sumit"
password="123456"
print(username== "sum" and password=="123456") #this will return False because username is not equal to "sum"
print(username== "sumit" and password=="123456") #this will return True because both username and password are correct
print(username== "sumit" or password=="123456") #this will return True because username is correct

print(5 | 4) #bitwise OR
print(5 & 4) #bitwise AND
print(5 ^ 4) #bitwise XOR

print (5 << 1) #left shift
print(5 >> 1) #right shift