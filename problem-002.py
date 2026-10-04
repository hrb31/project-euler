## Problem 2
## Find the sum of all even Fibonacci numbers below 4 million.


def fibonacci(n):
  if n == 1:
    return 1
  if n == 2:
    return 2

  a,b = 1,2

  for i in range(3, n+1):
    a,b = b, a+b

  return b



total = 0

for i in range(1,4000000):
  if fibonacci(i) % 2 == 0:
    total += fibonacci(i)


print(total)