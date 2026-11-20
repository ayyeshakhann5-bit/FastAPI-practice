from fastapi import FastAPI,Header,HTTPException,Depends
from datetime import datetime, timedelta, timezone
from jose import jwt,JWTError
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from passlib.context import CryptContext

app=FastAPI()

#JWT Config
SECRET_KEY="mysecret"

ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

#password hashing setup
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

#OAuthSetup
oauth2_schema=OAuth2PasswordBearer(tokenUrl="login")

#Dummy user DB

fake_user_db={
  "admin":{
    "username":"admin",
    "hashed_password":pwd_context.hash("1234")
  }
}

#Hash Password

def hash_password(password:str):
  return pwd_context.hash(password)

def verify_password(plain_password,hash_password):
  return pwd_context.verify(plain_password,hash_password)

def create_token(data:dict):
  to_encode=data.copy()
  expire = datetime.now(timezone.utc) + timedelta(minutes=30)
  to_encode.update({
    "exp":expire
  })
  
  token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return token

@app.post("/login")
def login(form_data:OAuth2PasswordRequestForm=Depends()):
  user=fake_user_db.get(form_data.username)
  if not user or not verify_password(form_data.password,user["hashed_password"]):
    raise HTTPException(
      status_code=400,
      detail="Invalid Username or Password"
    )
    
  access_token=create_token({"sub":form_data.username})
  
  return {
    "access_token":access_token,
    "token_type":"bearer"
  }
  
  #token verify
def verfify_token(token:str=Depends(oauth2_schema)):
  try:
      payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])   
      username:str=payload.get("sub")
      if username is None:
       raise HTTPException(
        status_code=401,
        detail="Invalid token"
      )

      return username
  except jwt.JWTError:
    raise HTTPException(
      status_code=401,
      detail="Invalid token"
    )   
    
#Protected Route

@app.get("/protected")
def protected_route(username:str=Depends(verfify_token)):
  return {
    "message":"Hello,you have access to this protected route",
    "user":username
  }
    
       