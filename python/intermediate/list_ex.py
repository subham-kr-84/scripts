# list- Collection of diff. Data Types

# type 1 of making list
a = [10,20,30,True,6.9]
print(type(a))
a.append(50)
print(a)
print(a[0])    #1st
print(a[-1])   # 1st from last
print(len(a))

# type-2 of making list 
clouds = list()
clouds.append("AWS")
clouds.append("azure")   # to add one element
clouds.extend(["GCP","oracle","IBM"])   # to add mutiple element
print(clouds)
print(dir(clouds))  # to see what all can be done in list

print(clouds.extend.__doc__)  # to ask what extend will do in list

# loops in LIST
#iterate in list

for cloud in clouds:          #cloud-0,1,2,3,4
  if cloud == "AWS":
    print(f"{cloud}: Most used! Learn 1st.")
  elif cloud == "azure":
    print(f"{cloud}: azure is important for devops, learn after aws")
  else:
    print(f"{cloud}: Learn after AWS and azure")







