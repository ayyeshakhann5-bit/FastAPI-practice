from fastapi import FastAPI,Request
import time

app=FastAPI()

# @app.middleware("http")
# async def my_middleware(request:Request,call_next):
#   print("Request Received")
  
#   response=await call_next(request)
#   print("Response Sent")
  
#   return response

@app.middleware("http")
async def log_middleware(request:Request,call_next):
  startt_time=time.time()
  responce=await call_next(request)
  
  process_time=time.time()-startt_time
  
  print(f"time:{process_time} | Path:{request.url.path}")
  
  return responce
  
  
  
  