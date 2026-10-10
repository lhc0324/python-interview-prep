# Python 上机面试冲刺清单

> 目标面试：元智天宇 · Python 开发工程师 · 明天 16:00 线上（腾讯会议）
> 考察形式：面试官说"出基本 Python 开发上机题，测试基本能力"
>
> **用法**：新建一个 `practice.py`，逐题敲，不许只读。打星 = 敲不出来。明早把打星的重敲一遍。

---

## 优先级

| 优先级 | 题号 | 说明 |
|---|---|---|
| ★★★ 今晚必练 | 1、8、10、11 | 最贴近 JD，出现率最高 |
| ★★ 有余力看 | 4、5、7、12 | 能体现基础的题 |
| ★ 快速过 | 2、3、6、9 | 简单，扫一眼确认会写 |

**进度自查**

- [ ] 1. 统计词频
- [ ] 2. 反转字符串 / 回文
- [ ] 3. 列表去重保序
- [ ] 4. 两数之和
- [ ] 5. 斐波那契三种写法
- [ ] 6. 手写排序
- [ ] 7. 二分查找
- [ ] 8. 读 JSON + 过滤/排序/分组
- [ ] 9. requests 请求 + 异常
- [ ] 10. FastAPI 最小接口
- [ ] 11. SQL GROUP BY / JOIN
- [ ] 12. 给代码找错

---

## 1. 统计词频 ★★★

**题目**：给一段文本，统计词频，返回出现次数最多的前 K 个。

**思路**：遍历一遍用字典计数 → O(n)；取 TopK 用堆，O(m log k)。Python 里 `Counter.most_common()` 就是干这个的，但面试官常让你别用标准库。

```python
from collections import Counter

def top_k_words(text, k=3):
    """标准库版"""
    return Counter(text.lower().split()).most_common(k)


def top_k_manual(text, k=3):
    """手写版：面试官说'别用 Counter'时用这个"""
    counts = {}
    for w in text.lower().split():
        counts[w] = counts.get(w, 0) + 1   # 不用 counts[w]，会 KeyError
    return sorted(counts.items(), key=lambda x: x[1], reverse=True)[:k]
```

**复杂度**：时间 O(n + m log m)（m 是不同词数），空间 O(m)。

**追问准备**：
- `counts.get(w, 0)` 和 `counts[w]` 的区别
- 如果文本是几个 G 的文件怎么办 → **别 `read()` 全读进内存**，逐行读；再大就分片 + 合并

---

## 2. 反转字符串 / 判断回文 ★

```python
def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    """只保留字母数字、忽略大小写（LeetCode 125 那种）"""
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]

def is_palindrome_2p(s):
    """双指针版，不额外开数组"""
    i, j = 0, len(s) - 1
    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i, j = i + 1, j - 1
    return True
```

**考点**：切片 `[::-1]` 是新对象，O(n)；双指针省空间。回文题**容易漏掉"忽略非字母数字"**这个要求，看清题面。

---

## 3. 列表去重且保持顺序 ★

```python
def dedup(lst):
    return list(dict.fromkeys(lst))   # 3.7+ 字典有序

def dedup_set(lst):
    seen, result = set(), []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result
```

**主动说这句加分**：`list(set(lst))` 也能去重，但**顺序不保证**。

**坑**：set 要求元素可哈希，列表/字典塞不进去。

---

## 4. 两数之和 ★★

```python
def two_sum(nums, target):
    seen = {}                       # 值 -> 下标
    for i, x in enumerate(nums):
        if target - x in seen:      # 一次查表，O(1)
            return [seen[target - x], i]
        seen[x] = i
    return []
```

**思路**：边遍历边记「见过的值 → 下标」，查补数。一遍扫完 O(n)，空间 O(n)。
为什么不用双循环 → O(n²)。**变体**：如果数组已排序，可以双指针 O(1) 空间。

---

## 5. 斐波那契（三种写法）★★

```python
# ① 朴素递归 O(2^n) —— 重复计算，n=35 就卡
def fib_rec(n):
    return n if n <= 1 else fib_rec(n - 1) + fib_rec(n - 2)

# ② 循环 O(n) 时间 O(1) 空间 —— 推荐
def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# ③ 记忆化 O(n)
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_memo(n):
    return n if n <= 1 else fib_memo(n - 1) + fib_memo(n - 2)
```

**这题最能体现水平**。面试官要的就是你能说清：递归为什么慢（重复子问题，可以画个 n=5 的递归树给他看），记忆化怎么把 O(2^n) 降到 O(n)。

---

## 6. 手写排序 ★

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left  = [x for x in arr if x < pivot]
    mid   = [x for x in arr if x == pivot]   # 等于的单独放，避免死循环
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:      # 已经有序，提前退出（这个细节要说）
            break
    return arr
```

**要能说**：快排平均 O(n log n)、最坏 O(n²)、**不稳定**；冒泡 O(n²)、**稳定**。上面这版快排好写但要额外空间，面试官问「原地版」就多讲两句 partition。

---

## 7. 二分查找 ★★

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:                        # 注意是 <=
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1                      # 必须 +1，否则死循环
        else:
            right = mid - 1
    return -1
```

**两个必考细节**：`<=` 还是 `<`（right 取 `len-1` 就用 `<=`）；`mid+1` 漏了就是死循环。复杂度 O(log n)。

---

## 8. 读 JSON 文件 + 过滤/排序/分组 ★★★

```python
import json

def analyze(path):
    with open(path, "r", encoding="utf-8") as f:   # encoding 不写，Windows 上会乱码
        users = json.load(f)

    # 过滤
    adults = [u for u in users if u.get("age", 0) >= 18]
    # 排序：按年龄降序，同岁按名字升序（多级用元组）
    adults.sort(key=lambda u: (-u["age"], u["name"]))
    # 分组
    groups = {}
    for u in adults:
        groups.setdefault(u["city"], []).append(u["name"])
    return adults, groups


def safe_load(path):
    """带异常处理的版本，面试里更稳"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"文件不存在: {path}")
        return []
    except json.JSONDecodeError as e:
        print(f"JSON 格式错误: {e}")
        return []
    return data if isinstance(data, list) else []
```
de
**必讲**：`with` 自动关文件；大文件逐行读别 `read()`；`setdefault` / `defaultdict` 做分组。这题最贴近 JD 里数据处理那条，**要能顺口讲出来**。

---

## 9. requests 请求 + 解析 + 异常 ★

```python
import requests

def fetch_user(user_id):
    url = f"https://api.example.com/users/{user_id}"
    try:
        resp = requests.get(url, timeout=5)   # timeout 一定要设，不设会挂死
        resp.raise_for_status()               # 4xx/5xx 主动抛异常
        return resp.json().get("name")
    except requests.exceptions.Timeout:
        print("请求超时")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP 错误: {e}")
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
    return None
```

**三个必说点**：timeout、raise_for_status、异常分类。再补一句「批量请求会用 Session 复用连接」就够。

---

## 10. FastAPI 最小接口 ★★★

```python
from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    quantity: int = 1


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/items/{item_id}")
def get_item(item_id: int, q: Optional[str] = None):
    if item_id <= 0:
        raise HTTPException(status_code=400, detail="item_id 必须为正数")
    return {"item_id": item_id, "q": q}


@app.post("/items", status_code=201)
def create_item(item: Item):
    return {"name": item.name, "total": item.price * item.quantity}
```

启动：`uvicorn main:app --reload`

**这是你的主场，必须闭着眼写出来。** 写的时候顺口讲分层（Router / CRUD / Model），就是把你项目那套搬过来。

**追问准备**：
- 为什么用 Pydantic → 自动校验 + 自动生成文档
- 路径参数 vs 查询参数怎么分 → 路由里 `{}` 是路径；函数里有默认值的是查询
- `status_code=201` 什么时候用 → 创建资源

---

## 11. SQL：GROUP BY / JOIN ★★★

```sql
-- 每个城市的用户数，降序
SELECT city, COUNT(*) AS cnt
FROM users
GROUP BY city
ORDER BY cnt DESC;

-- 过滤聚合结果：过滤分组用 HAVING，不是 WHERE
SELECT city, COUNT(*) AS cnt, AVG(age) AS avg_age
FROM users
GROUP BY city
HAVING COUNT(*) > 1;

-- 关联：订单 + 用户名
SELECT o.id, u.name, o.amount
FROM orders o
INNER JOIN users u ON o.user_id = u.id
WHERE o.status = 'paid';

-- 左连接找"没有订单的用户"
SELECT u.name
FROM users u
LEFT JOIN orders o ON o.user_id = u.id
WHERE o.id IS NULL;
```

**必背三句**：
- **WHERE 分组前过滤行，HAVING 分组后过滤组**
- INNER JOIN 只留匹配的，LEFT JOIN 保留左表全部（右表没有填 NULL）
- `COUNT(*)` 算所有行，`COUNT(字段)` **不统计 NULL**

---

## 12. 给代码找错 ★★

这类题就这几个高频坑，看到先扫一遍。

**坑1：可变默认参数** —— 默认值只创建一次，跨调用累积

```python
def add(item, lst=[]):          # 错
    lst.append(item)
    return lst

def add(item, lst=None):        # 对
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

**坑2：闭包晚绑定**

```python
funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])     # [2, 2, 2]，不是 [0, 1, 2]

funcs = [lambda i=i: i for i in range(3)]   # 用默认参数固定当前值
```

**坑3：边遍历边删**

```python
for x in lst:
    if x % 2 == 0:
        lst.remove(x)           # 错，会跳过元素
for x in lst[:]:                # 遍历副本
    ...
```

**坑4：浅拷贝**

```python
import copy
a = [[1, 2], [3, 4]]
b = a[:]                        # 浅拷贝，内层还是同一个对象
b[0].append(99)
print(a)                        # [[1, 2, 99], [3, 4]]  a 被改了
c = copy.deepcopy(a)            # 深拷贝才安全
```

**口诀**：看到找错题，先查 **默认参数 / 可变对象 / 作用域 / 浅拷贝 / 边界下标**。

---

# 上机实操准备

## 面试前 30 分钟

- [ ] VS Code 打开、Python 解释器能跑通（先跑个 `print("ok")`）
- [ ] 字体调大（共享屏幕对方要看清楚）
- [ ] 关掉微信、QQ、多余浏览器标签
- [ ] 腾讯会议共享屏幕 → 选**「特定窗口」**，别共享整个桌面
- [ ] 手机静音、水杯放好

## 写代码时

1. **先讲思路再动手**：`"我用字典存频次，遍历一遍是 O(n)，然后排序取前 K 个"`
2. **写不出来也要把思路讲完** —— 大多数面试官认思路
3. **卡住了别沉默**，直接说卡在哪
4. **写完主动跑测试用例**：正常值 → 空值 → 边界值（单个元素、全相同）
5. 没有自动补全也照样写，基础题不需要

---

# 项目必答题（一定会问，今晚想清楚）

把项目压缩成 20 秒版本，自我介绍时就抛出来：

> FastAPI + SQLAlchemy 2.0 分层架构，17 个 RESTful 接口，JWT 鉴权、Redis 缓存、Docker 部署

**要准备的追问**：

- 为什么用 SQLAlchemy 2.0，分层是怎么切的（Router / CRUD / Model）
- Redis 缓存放了什么，怎么保证一致性
- JWT 鉴权怎么做，token 过期怎么处理
- Docker 部署了几个容器，怎么联调
- **项目里最难的一个问题是什么，你怎么解决的** ← 出现率最高，必须有准备

**运筹优化那块别硬吹**，一句话带过：

> "了解线性规划和整数规划的基本概念，工程落地这边我能配合算法同学。"

---

# 面试时顺便问 HR（之前没答的）

- "有效工作日"具体怎么算
- 转正评估的时间点和标准

---

# 备注：已知的薪资条件

- 实习：150/天，按有效工作日
- 转正：8000（岗位挂 8-13K，实际是下限），全额社保
- 150 × 21 天 ≈ 3150/月，北京租房 2000-2500 + 生活，基本月月清零
