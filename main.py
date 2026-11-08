from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

#Home Route
# @app.get("/")
# def home():
#     return {"message": "Hello, World!"}
  
  
# #about  
# @app.get("/about")
# def about():
#     return {"message": "This is the about page."}
  
# #user route

# @app.get("/users")

# def users():
#     return {
#       "users":["Ayesha","khan"]
      
#     }
    
# @app.get("/users/{user_id}")

# def get_user(user_id:int):
#    return {"user_id":user_id}

# @app.get("/users")
# def get_users(name: str=None):
#     return {"Name":name}

# @app.get("/products")
# def products(limit:int=10):
#     return {"limit":limit}

# @app.get("/items")
# def items(name:str=None,price:int=10):
#     return {"name":name,"price":price}

# class User(BaseModel):
#     name:str
#     age:int

# @app.post("/create-user")

# def create_user(user:User):
#     return{
#         "message":"User created successfully",
#         "data":user
#     }

# class User(BaseModel):
#     name:str
#     age:int
#     email:str
    
# @app.post("/create_user")

# def create_user(user:User):
#     return {
#         "message":"User created successfully",
#         "data":user
#     }    

class Address(BaseModel):
    city:str
    pincode:int
    
class User(BaseModel):
    name:str
    age:int
    email:str
    address:Address
    
@app.post("/create_user")

def craete_user(user:User):
    return user        