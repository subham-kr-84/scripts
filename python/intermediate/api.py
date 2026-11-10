import requests # pyright: ignore[reportMissingModuleSource]
import json

api_url = "https://jsonplaceholder.typicode.com/users"

def user_data():
  response = requests.get(url=api_url)
  response.raise_for_status()  # Raise an exception if the request was unsuccessful

  print(response.json())  #list
  '''
 ## if i want particular data of users.
  # for item in response.json():
  #   for key,value in item.items():
  #     if key == "id" and value == info:
  #       print(f"name: {item['name']}, Email: {item['email']}, Phone: {item['phone']}")
  '''
  with open("user_data.json", "w") as f:
    json.dump(response.json(), f, indent=4)

  print("Saved all users to user_data.json....")

user_data()
      


