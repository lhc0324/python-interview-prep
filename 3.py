#列表去重且保持顺序

def dedup(lst):
  return list(dict.fromkeys(lst))

def dedup_set(lst):
  seen,result = set(),[]
  for x in lst:
    if x not in seen:
      seen.add(x)
      result.append(x)
  return result