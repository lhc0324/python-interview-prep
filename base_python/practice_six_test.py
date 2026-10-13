import practice_six
from fastapi.testclient import TestClient

client = TestClient(practice_six.app)

a = client.get("/report/summary")
b = client.get("/report/by-region")
r = client.get("/report/top")

print(a.status_code,a.json())
print(r.status_code,r.json())
print(b.status_code,b.json())