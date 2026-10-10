#斐波那契函数

def fib_rec(n):
  return n if n <= 1 else fib_rec(n-1) + fib_rec(n-2)

def fib_iter(n):
  a,b = 0,1
  for _ in range(n):
    a,b = b,a + b
  return a 