from fastapi import FastAPI, HTTPException

app = FastAPI()

records = [
    {"id": 1,  "sales": "张三", "region": "华北", "amount": 500,  "status": "done"},
    {"id": 2,  "sales": "李四", "region": "华东", "amount": 800,  "status": "done"},
    {"id": 3,  "sales": "张三", "region": "华北", "amount": 500,  "status": "done"},
    {"id": 4,  "sales": "王五", "region": "华东", "amount": 2000, "status": "done"},
    {"id": 5,  "sales": "张三", "region": "华北", "amount": 500,  "status": "canceled"},
    {"id": 6,  "sales": "赵六", "region": "华南", "amount": 900,  "status": "refunded"},
    {"id": 7,  "sales": "张三", "region": "华北", "amount": 500,  "status": "done"},
    {"id": 8,  "sales": "李四", "region": "华东", "amount": 600,  "status": "done"},
    {"id": 9,  "sales": "王五", "region": "华东", "amount": 400,  "status": "done"},
    {"id": 10, "sales": "张三", "region": "华北", "amount": 500,  "status": "done"},
    {"id": 11, "sales": "张三", "region": "华北", "amount": 500,  "status": "done"},
]


@app.get("/report/summary")
def summary():
    total = 0
    count = 0
    for record in records:
        if record["status"] == "done":
            total += record["amount"]
            count += 1
    return {"total": total, "count": count}


@app.get("/report/top")
def top():
    amounts = {}
    for record in records:
        if record["status"] == "done":
            if record["sales"] not in amounts:
                amounts[record["sales"]] = 0
            amounts[record["sales"]] += record["amount"]
    if len(amounts) == 0:
        raise HTTPException(status_code=404,detail="没有完成的订单")
    else:
        top_sales = max(amounts,key=amounts.get)
        top_amount = amounts[top_sales]
        return {"sales": top_sales, "amount": top_amount}


@app.get("/report/by-region")
def by_region():
    region_map = {}
    for record in records:
        if record["status"] == "done":
            region = record["region"]
            if region not in region_map:
                region_map[region] = 0
            region_map[region] += record["amount"]
    return region_map