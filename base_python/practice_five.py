from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

items = [
    {"id": 1, "name": "Python入门", "price": 59, "category": "book"},
    {"id": 2, "name": "机械键盘", "price": 399, "category": "hardware"},
    {"id": 3, "name": "FastAPI实战", "price": 79, "category": "book"},
    {"id": 4, "name": "显示器支架", "price": 129, "category": "hardware"},
]


class Item(BaseModel):
    name: str
    price: float
    category: str


@app.get("/items")
def list_items(category: str = None):
    if category is None:
        return items
    
    result = []
    for item in items:
        if item["category"] == category:
            result.append(item)
    return result


@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="商品不存在")


@app.post("/items")
def add_item(item: Item):
    new_item = item.model_dump()
    max_id = 0
    for count in items:
        if count["id"] > max_id:
            max_id = count["id"]
    new_item["id"] = max_id + 1
    items.append(new_item)
    return new_item