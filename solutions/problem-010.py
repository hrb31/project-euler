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


total = 0

for i in sieve(2000000):
  total += i

print(total)
