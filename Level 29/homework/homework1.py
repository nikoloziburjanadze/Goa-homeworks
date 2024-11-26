#1. Variables
x = 10
y = 5.5
name = "Alice"
is_active = True
temperature = -2
height = 180
weight = 70.5
age = 25
score = 100
city = "New York"


# Variable Data Types

num1 = 10

num2 = 3.14

greeting = "Hello, World!"

is_ready = True
is_sunny = False

fruits = ["apple", "banana", "cherry"]

#inputs

name = input("Enter your name: ")  
age = int(input("Enter your age: ")) 
height = float(input("Enter your height in meters: "))  
country = input("Where are you from? ")  
is_student = input("Are you a student? (yes/no): ") 
email = input("Enter your email address: ") 
favorite_color = input("What is your favorite color? ") 
phone_number = input("Enter your phone number: ") 
address = input("Enter your address: ")  
number_of_pets = int(input("How many pets do you have? "))  

# Comparson Operators

x = 10
y = 5
z = 10

print(x == y) 
print(x != y)
print(x > y)   
print(x < y)  
print(x >= z) 
print(x <= z) 
print(x == 10) 
print(y > 2)  
print(7 <= z)
print(12 != 12)

#Logical Operators

x = 5
y = 10

print(x > 3 and y < 15)
print(x < 3 or y < 15)   
print(x > 3 and y > 15) 
print(x < 5 or y == 10) 
print(x > 2 and y < 20)   
print(x == 0 or y != 40)        
print(x == 5 and y == 10) 
print(x != 5 or y == 10)  
print(x > 0 and y < 20)   
print(x == 0 or y != 10) 

# looooooops

for i in range(5):
    print(i) 

for i in range(2, 6):
    print(i) 

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i in range(0, 10, 2):
    print(i)  

for i in "hello":
    print(i)

#Conditional Statements

x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

# Nested if example
y = 10
if y > 0:
    if y < 15:
        print("y is between 0 and 15")

# Checking even or odd
number = 7
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Checking for leap year
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

#list

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(fruits[0])  # "apple"
print(fruits[1])  # "banana"

fruits[2] = "blueberry"  
print(fruits)


fruits.append("fig") 
print(fruits)

fruits.remove("banana")  
print(fruits)

print(len(fruits)) 


print(fruits[1:3])  # ["blueberry", "date"]


for fruit in fruits:
    print(fruit)

more_fruits = ["grape", "honeydew"]
all_fruits = fruits + more_fruits  
print(all_fruits)


print("apple" in fruits)  # True
print("banana" in fruits)  # False

