import os
import json


def add_user(name, email):
    file_path = "API/data.json"
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, "r") as file:
            data = json.load(file)
    else:
        data = []
        
    data.append({
        "name" : name,
        "email" : email
    })
    
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    
    print("User added successfully.")
    
if __name__ == "__main__":
    name = input("Enter name: ")
    email = input("Enter email: ")
    add_user(name, email)