#反转字符串/判断回文


def reverse_string(s):
  return s[::-1]


def is_palindrome(s):
  cleaned = []
  for c in s:
    if c.isalnum():
      cleaned.append(c.lower())
  return cleaned == cleaned[::-1]

def is_palindromes(s):
  cleaned = []
  for c in s:
    if c.isalnum():
      cleaned.append(c)
  return cleaned == cleaned[::-1]

if __name__ == "__main__":
  s= "limiL"
  print({is_palindrome(s)})

