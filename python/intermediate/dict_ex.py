# dictionary -{"key" : "value"}

info = {
       "name" : "subham kumar",
       "place" : "dhanbad",
       "age" : 25,
       "love" : ["movie", "game"]
       }

print(info)       
print(info["place"])
info.update({"hate" : "alcohol"})
print(info)

print("I live at ",info.get("plac","my home"))    # use get function to not get error if any key is not found and print default value.
print("I live at ",info.get("place","my home"))

print(dir(info)) # to fetch all things we can do in dict..
print(info.get.__doc__)

#iterate in dict
for key,value in info.items():
  print(key,value)