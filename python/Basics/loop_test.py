for i in range(5):
  
  env = input("Enter the environment:")
  print("The User Input variable is",env)

  if env == "prd":
    print("Dont't deploy on Friday")
  elif env == "stg":
    print("Take backup and Test well")
  else:
    print("Deploy on any day")  