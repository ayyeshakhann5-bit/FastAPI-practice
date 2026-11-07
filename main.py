from fastapi import FastAPI

app=FastAPI()

#Home Route
@app.get("/")
def home():
    return {"message": "Hello, World!"}
  
  
#about  
@app.get("/about")
def about():
    return {"message": "This is the about page."}
  
#user route

@app.get("/users")

def users():
    return {
      "users":["Ayesha","khan"]
      
    }
    
@app.get("/users/{user_id}")

def get_user(user_id:int):
   return {"user_id":user_id}
