# TypeError
# len(123)

# No TypeError
len("Hello") # 5

# Type Checking
print(type("abc")) # String
print(type(123))   # Integer
print(type(3.14))  # Float
print(type(True))  # Boolean

# Type Conversion
str()
int()
float()
bool()

name_of_the_user = input("Enter your name")
length_of_name = len(name_of_the_user)

print(type("Number of letters in your name: "))  # str
print(type(length_of_name))  # int

print("Number of letters in your name: " + str(length_of_name))
