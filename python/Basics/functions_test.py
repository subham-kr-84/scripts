def sum_of_num():      #defining a function
  num1 = int(input("enter num 1: "))
  num2 = int(input("enter num 2: "))
  sum = num1 + num2
  print(f"{num1} + {num2} = {sum}")

env = input("Enter the environment:")

print("The User Input variable is",env)

if env == "prd":
  print("Dont't deploy on Friday")
elif env == "stg":
  print("Take backup and Test well")
else:
  sum_of_num()       #calling a function