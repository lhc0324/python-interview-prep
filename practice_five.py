def fib(n):
  return n if n <= 1 else fib(n-1) + fib(n-2)

def fib_two(n):
  a,b = 0,1
  for i in range(n):
    a,b = b,a+b
  return a