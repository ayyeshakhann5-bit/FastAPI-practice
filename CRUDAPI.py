from sqlalchemy import create_engine,Column,String,Integer
from sqlalchemy.orm import sessionmaker,declarative_base,Session
from fastapi import FastAPI,Depends,HTTPException

app=FastAPI()
#DATABASE URL
DATABASE_URL="sqlite:///./test.db"

#Engine create (DB Connection)
engine=create_engine(
  DATABASE_URL,
  connect_args={"check_same_thread":False}
)
#Session(for DB operations)
sessionLocal=sessionmaker(bind=engine)

#Base(for medel)
Base=declarative_base()

#Table Model
class Todo(Base):
  __tablename__="todos"
  id=Column(Integer,primary_key=True,index=True)
  title=Column(String)
  completed=Column(Integer)
  
#Table create  
Base.metadata.create_all(bind=engine)
  
#Dependency for DB session  
def get_db():
  db=sessionLocal()
  try:
    yield db
  finally:
    db.close()
    

  
  
def get_db():
  db=sessionLocal()
  try:
    yield db
  finally:
    db.close()
    
@app.post("/todos")
def create_user(title:str,db:Session=Depends(get_db)):
  todo=Todo(title=title,completed="False")
  db.add(todo)  
  db.commit()
  db.refresh(todo)
  return{
    "message":"Todo Created",
    "data":todo
  }
  
@app.get("/todos")
def get_user(db:Session=Depends(get_db)):
  todos=db.query(Todo).all()
  
  return{
    "Total":len(todos),
    "data":todos
  } 
  
@app.get("/todos/{todo_id}")
def get_user_id(todo_id=int,db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id==todo_id).first()
    
    if not todo:
     raise HTTPException(status_code=404,detail="Todo Not Found")
    return todo
  
  
#Update

@app.put("/todos/{todo_id}")
def update_user(todo_id=int,title=str,db:Session=Depends(get_db)):
  todo=db.query(Todo).filter(Todo.id==todo_id).first()  
  
  if not todo:
    raise HTTPException(status_code=404,detail="Todo not found")
  todo.title=title
  db.commit()
  db.refresh(todo)
  return {
    "message":"Todo updated",
    "data":todo
  }
  
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int,db:Session=Depends(get_db)):
  todo=db.query(Todo).filter(Todo.id==todo_id).first()
  if not todo:
      raise HTTPException(status_code=400,detail="Todo Not found")
 
  db.delete(todo)
  
  db.commit()
  
  return{
    "message":"Todo Deleted"
  }


  
  
    
          