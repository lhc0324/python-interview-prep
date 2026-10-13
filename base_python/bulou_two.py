# 需求：待办事项（todo）接口
#   GET  /todos                  返回全部待办
#   POST /todos                  新增。请求体是 JSON：{"title": "买牛奶"}
#                                返回新建的那一条（含 id 和 done）
#   PUT  /todos/{todo_id}/done   把指定待办标记为已完成；找不到返回 404

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

todos = []
for i in range(1, 6):
    todos.append({"id": i, "title": "任务" + str(i), "done": False})


class TodoIn(BaseModel):
    title: str


@app.get("/todos")
def list_todos():
    return todos


@app.post("/todos")
def create_todo(payload : TodoIn):
    new_id = len(todos) + 1
    new_todo = {"id": new_id, "title": payload.title, "done": False}
    todos.append(new_todo)
    return new_todo


@app.put("/todos/{todo_id}/done")
def mark_done(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            todo["done"] = True
            return {"ok": True,"todo":todo}
    raise HTTPException(status_code=404,detail="待办不存在")