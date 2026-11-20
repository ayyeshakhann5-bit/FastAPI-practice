from fastapi import FastAPI,HTTPException,Header,Depends
from datetime import datetime, timedelta, timezone
from jose import jwt

app=FastAPI()

SECRET_KEY="mysecret"

ALGORITHM="HS256"

def create_token(data:dict):
  to_encode=data.copy()
  expire = datetime.now(timezone.utc) + timedelta(minutes=30)
  to_encode.update({
    "exp":expire
  })
  
  token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return token

@app.post("/login")
def login(username:str,password:str):
  if username!="admin" or password!="12345":
    raise HTTPException(
      status_code=401,
      detail="Invalid Username or passord"
    )
  token=create_token({
    "sub":username
  })
  
  return{
    "access_token":token
  }
  
  #token verify
def varify_token(token:str=Header(None)):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    except:
      raise HTTPException(
        status_code=404,
        detail="Invalid or expired Token"
      )  
      
@app.get("/secure")
def secure_data(user=Depends(varify_token)):
  return{
    "message":"Secure Data Accessed",
    "user":user
  }     
       