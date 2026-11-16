from fastapi import FastAPI,Depends,Header,HTTPException

app=FastAPI()

# def common_logic(data):
#   return {
#     "message":"Common logic executed"
#   }
  
# @app.get("/home")
# def home(data=Depends(common_logic)):
#   return data 

# @app.get("/dashboard")
# def dashboard(data=Depends(common_logic)):
#   return data

def verify_token(token:str=Header(None)):
  if token!="mySecret":
    raise HTTPException(
      status_code=404,
      detail="Unauthorized"
    )
  return {
    "user":"Authorized User"
  }  
  
@app.get("/secure-data")
def secure_data(user=Depends(verify_token)):
  return {
    "message":"Secure data accessed",
    "user":user
  }  

