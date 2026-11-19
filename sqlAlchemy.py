from sqlalchemy import create_engine,Column,String,Integer
from sqlalchemy.orm import sessionmaker,declarative_base,Session
from fastapi import FastAPI,Depends

app=FastAPI()

DATABASE_URL="sqlite:///./test.db"

engine=create_engine(
  DATABASE_URL,
  connect_args={"check_same_thread":False}
)

sessionLocal=sessionmaker(bind=engine)

Base=declarative_base()

class Todo(Base):
  __tablename__="todos"
  id=Column(Integer,primary_key=True,index=True)
  title=Column(String)
  completed=Column(Integer)
  
Base.metadata.create_all(bind=engine)
  

def get_db():
  db=sessionLocal()
  try:
    yield db
  finally:
    db.close()
      

  
  
  
          