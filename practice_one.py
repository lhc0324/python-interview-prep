from collections import Counter


def get_k_higher(text,k = 3):
  return Counter(text.lower().split()).most_common(k)

def get_k_higher_words(text,k = 3):
  counts = {}
  for w in text.lower().split():
    counts[w] = counts.get(w,0) + 1
  return sorted(counts.items(),key=lambda x:x[1],reverse=True)[:k]
if __name__ == "__main__":
  text = "the dog the cat the bird cat"
  result = get_k_higher_words(text,3)
  print(result)