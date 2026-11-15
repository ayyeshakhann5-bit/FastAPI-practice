from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
users=[]

class User(BaseModel):
    name:str
    age:int
  
@app.get("/users")
def get_users():
    return users    
    
@app.post("/users")
def create_users(user:User):
    users.append(user)
    return{
        "message":"User created successfully",
        "data":user
    }
    
@app.put("/users/{user_id}")    
def updated_user(user_id:int,user:User,notify:bool=False):
  if user_id<len(users):
    users[user_id]=user
    return {
        "message":"User updated successfully",
        "data":user,
        "notify":notify
    }
  return "Error: No data found"  