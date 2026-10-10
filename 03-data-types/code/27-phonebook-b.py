# 第 27 讲 · 小试牛刀：如何利用类型转换实现手机通讯录？（下）
# 本讲把 csv 通讯录转成字典、存进 json 文件，再实现查询与增删。
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(HERE, "26-demo.csv")
DB_FILE = os.path.join(HERE, "db.json")

# 1. 读取 csv，每行转成一个字典（非结构化 → 结构化）
contacts = []
with open(CSV_FILE, encoding="utf-8") as f:
    for line in f:
        name, source, tel = line.strip().split(",")
        contacts.append({"name": name, "source": source, "tel": tel})

# 2. 把字典列表保存成 json 格式的「通讯录文件」
with open(DB_FILE, "w", encoding="utf-8") as f:
    json.dump(contacts, f, ensure_ascii=False, indent=2)
print("已保存通讯录文件:", os.path.basename(DB_FILE))

# 3. 从 json 文件读回来
with open(DB_FILE, encoding="utf-8") as f:
    db = json.load(f)
print("通讯录共有", len(db), "位好友")

# 4. 查询：按姓名找到联系人
print("查询「李四」:")
for c in db:
    if c["name"] == "李四":
        print(f"  {c['name']}（{c['source']}）的电话是 {c['tel']}")

# 5. 增加一位联系人
db.append({"name": "赵六", "source": "客户", "tel": "13712345678"})
print("增加赵六后共有", len(db), "位好友")

# 6. 删除一位联系人（这里把「张三」都删掉）
db = [c for c in db if c["name"] != "张三"]
print("删除张三后共有", len(db), "位好友")

# 7. 写回文件，并打印最终通讯录
with open(DB_FILE, "w", encoding="utf-8") as f:
    json.dump(db, f, ensure_ascii=False, indent=2)
print("最终通讯录:")
for c in db:
    print(" ", c)
