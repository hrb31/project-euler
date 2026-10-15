def sieve(num):
  is_prime = [True] * (num + 1)
  is_prime[0] = False
  is_prime[1] = False

  for p in range(2, int(num**0.5)+1):
    if is_prime[p]:
      for multiple in range(p**2,num+1,p):
        is_prime[multiple] = False

  primes = []
  for i in range(2,num+1):
    if is_prime[i]:
      primes.append(i)
  return primes

## estimated the bound within which the number lies in using trial and error methods

max = 0

for i in range(104500,105000):
  if len(sieve(i)) == 10001:
    max = i

list = sieve(max)
print(list[len(list)-1])

## optimised method
# after estimating an upper bound (10500) the following code could be used instead

limit = 105000
primes = sieve(limit)
print(primes[10000])
