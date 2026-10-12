# 读json文件，处理和排序

import json
with open("base_python\\students.json", encoding="utf-8") as f:
    data = json.load(f)
print(data)
print(len(data))
total_score = 0
for i in range(len(data)):
    total_score += data[i]["score"]
ave_score = total_score / len(data)
result = sorted(data, key=lambda stu: stu["score"], reverse=True)
for stu in result:
    print(stu["name"], stu["score"])
print(f"平均分：{ave_score}")
print(f"最高分：{result[0]['name']}({result[0]['score']})")

parts = []
for stu in result:
    parts.append(stu["name"] + "(" + str(stu["score"]) + ")")
print("排名: " + " > ".join(parts))
