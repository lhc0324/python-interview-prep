#josn文件读写，过滤排序分组


import json
def analyze(path):
  #读josn文件
  with open(path,"r",encoding="utf-8") as f:
    users = json.load(f)
  #过滤剩成年人
  adults = []
  for u in users:
    if u.get("age",0) >= 18:
      adults.append(u)
  #排序
  adults.sort(key=lambda u:(-u["age"],u["name"]))
  #分组
  groups = {}
  for u in adults:
    groups.setdefault(u["city"],[]).append(u["name"])
  return adults,groups