#查询一段文本中出现频次最高的几个数


from collections import Counter

def top_k_words(text,k = 3):
  return Counter(text.lower().split()).most_common(k)

def top_k_manual(text,k = 3):
  counts = {}
  for w in text.lower().split():
    counts[w] = counts.get(w,0) + 1
  return sorted(counts.items(),key=lambda x: x[1],reverse=True)[:k]

if __name__ == "__main__":
  text = "the cat the dog the bird cat"
  result = top_k_words(text,3)
  print(result)