


orders = [
    {"user": "张三", "amount": 120, "status": "paid"},
    {"user": "李四", "amount": 300, "status": "paid"},
    {"user": "张三", "amount": 80,  "status": "unpaid"},
    {"user": "王五", "amount": 500, "status": "paid"},
    {"user": "孙七", "amount": 999, "status": "unpaid"},
    {"user": "张三", "amount": 50,  "status": "paid"},
    {"user": "李四", "amount": 100, "status": "unpaid"},
    {"user": "赵六", "amount": 0,   "status": "paid"},
]
paid_list = []


for order in orders:
    if order["status"] == "paid":
        paid_list.append(order)
        print(order)



total = {}

for order in paid_list:
    if order["user"] in total:
        total[order["user"]] += order["amount"]
    else:
        total[order["user"]] = order["amount"]

print(total)
result = sorted(total,key= lambda x:total[x],reverse=True)
if len(paid_list) == 0:
    print("没有支付成功的记录")
else:
    top_name = result[0]
    top_amount = total[top_name]
    print(top_name,top_amount)