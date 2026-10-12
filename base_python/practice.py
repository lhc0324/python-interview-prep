import json

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

with open("students.json",encoding="utf-8") as f:
    students = json.load(f)

class Student(BaseModel):
    name: str
    score: int

@app.get("/")
def root():
    return {"message" : "接口运行成功"}

@app.get("/students")
def get_students():
    return students

@app.get("/students/{index}")
def index_students(index : int):
    if index < 0 or index >= len(students):
        raise HTTPException(status_code=404,detail="找不到你要找的学生")
    return students[index]

@app.post("/students")
def add_students(stu: Student):
    new_student = stu.model_dump()
    students.append(new_student)
    return new_student