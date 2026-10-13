import practice_five
from fastapi.testclient import TestClient

client = TestClient(practice_five.app)
a = client.get("/items")
b = client.get("/items",params={"category":"book"})
c = client.get("/items/2")
d = client.get("/items/999")
r = client.post("/items",json={"name":"鼠标","price":89,"category":"hardware"})
e = client.get("/items")

print(a.status_code,a.json())
print(b.status_code,b.json())
print(c.status_code,c.json())
print(d.status_code,d.json())
print(r.status_code,r.json())
print(e.status_code,e.json())