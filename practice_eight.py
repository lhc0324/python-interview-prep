import json

path = "users.json"
def get_json(path):
  #读json文件
  with open(path,"r",encoding="utf-8") as f:
    users = json.load(f)

  #过滤成年人
  adults = []
  for u in users:
    if u.get("age",0) >= 18:
      adults.append(u)

  #排序
  adults.sort(key=lambda u : (-u["age"],u["name"]))

  #分组
  groups = {}
  for u in adults:
    groups.setdefault(u["city"],[]).append(u["name"])
  return adults,groups

def safe_load(path):
  try:
    with open(path,"r",encoding="utf-8")as f:
      data = json.load(f)
  except FileNotFoundError:
    print(f"文件不存在：{path}")
    return []
  except json.JSONDecodeError as e:
    print(f"json格式错误:{e}") 
    return []
  return data if isinstance(data,list) else []   


if __name__ == "__main__":
  result = safe_load(path)
  print(result)



def get_user(path):
  with open(path,"r",encoding="utf-8") as f:
    users = json.load(f)
  #过滤
  adults = []
  for u in users:
    if u.get("age",0) >= 18:
      adults.append(u)
  #排序
  adults.sort(key=lambda u:(-u['age'],u["name"]))
  #分组
  groups = {}
  for u in adults:
    groups.setdefault(u["city"],[]).append(u["name"])
  return adults,groups