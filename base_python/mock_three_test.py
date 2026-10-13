import mock_three
from fastapi.testclient import TestClient

client = TestClient(mock_three.app)

r = client.get("/items?page=1&size=10")
a = client.get("/items?page=2&size=0")
b = client.get("/items?page=0&size=10")


print(r.status_code,r.json())
print(a.status_code,a.json())
print(b.status_code,b.json())