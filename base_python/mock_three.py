# 需求：
#   GET /items?page=1&size=10
#   - page 从 1 开始计（第 1 页就是第一页）
#   - 返回 {"page": .., "size": .., "total": 总条数, "items": [本页数据]}
#   - page 超出范围 → items 返回空列表，不报错
#   - page < 1 或 size < 1 → 返回 400

from fastapi import FastAPI, HTTPException

app = FastAPI()

items = []
for i in range(1, 26):
    items.append({"id": i, "name": "商品" + str(i)})


@app.get("/items")
def list_items(page: int = 1, size: int = 10):
    if page < 1 or size < 1:
        raise HTTPException(status_code=400,detail="不存在的页")
    
    start = (page - 1) * size
    end = start + size
    result = items[start:end]
    return {"page": page, "size": size, "total": len(items), "items": result}