# Goal- To get the env variable from the user and print it.

env = input("Enter the environment:")

print("The User Input variable is",env)

##-----Type casting of the user input variable

# a = int(input("Enter the num 1: "))
# b = int(input("Enter the num 2: "))
# print(type(a),type(b))
# print("The sum of the two numbers is",a+b)
# print("The difference of the two numbers is",a-b)
# print("The product of the two numbers is",a*b)
# print("The division of the two numbers is",a/b)

##-----conditional statements
if env == "prd":
  print("Dont't deploy on Friday")
elif env == "stg":
  print("Take backup and Test well")
else:
  print("Deploy on any day")   
