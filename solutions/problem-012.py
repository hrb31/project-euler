def triangle(n):
  return n * (n + 1) // 2

def divisor_count(num):
  if num == 1:
    return 1
  total = 2
  for i in range(2, int(num**0.5)+1):
    if num % i == 0:
      if i**2 == num:
        total += 1
      else:
        total += 2
  return total

start = 100
while divisor_count(triangle(start)) <= 500:
  start += 1

print(triangle(start))

## optimised method
## triangle no. = n(n+1) / 2
## gcd(n,n+1) = 1
## d(ab) = d(a) x d(b)
## if n is even, a = n/2 and b = n+1
## if n is odd, a = n, and b = (n+1)/2
  
def triangle_divisor_count(n):
  if n % 2 == 0:
      a = n // 2
      b = n + 1
  else:
      a = n
      b = (n + 1) // 2
  return divisor_count(a) * divisor_count(b)

start = 1

while triangle_divisor_count(start) <= 500:
  start += 1

print(triangle(start))
