choice = input("Do you want to print the table of a number? (yes/no): ")

while choice != "no":
  num = int(input("Enter the number to print the table: "))
  #formatter- f"" is used to format the string and print the value of the variable in the string.  
  for i in range(1,11):
    print(f"{num} * {i} = {num*i}")

  choice = input("Do you want to print the table of another number? (yes/no): ")  

  