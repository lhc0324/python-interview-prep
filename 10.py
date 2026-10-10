#简单的fastpai接口


from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
  name:str
  price:float
  quantity: int = 1

@app.get("/health")
def health():
  return {"status":"ok"}

@app.get("/item/{item_id}")
def get_item(item_id: int, q : Optional[str] = None):
  if item_id <= 0:
    raise HTTPException(status_code=400,detail="item_id 必须为正数")
  return {"item_id":item_id ,"q": q}

@app.post("/items",status_code=201)
def create_item(item: Item):
  return {"name": item.name,"total": item.price * item.quantity}
