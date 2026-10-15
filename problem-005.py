##initial solution
# Sieve of Eratosthenes could have been used for a neater solution
def is_prime(num):
  prime = True
  if num < 2:
    return False
  for i in range(2,num):
      if num % i == 0:
        prime = False
        break
  return prime

primes = []
for i in range(1,21):
  if is_prime(i):
    primes.append(i)

powers = []
for i in primes:
    exp = 0

    while i ** (exp + 1) <= 20:
        exp += 1

    powers.append(i**exp)

total = 1
for i in powers:
  total = total * i
  
print(total)

## optimised solution
def is_prime(num):
    if num < 2:
        return False

    divisor = 2
    while divisor * divisor <= num:
        if num % divisor == 0:
            return False
        divisor += 1

    return True


limit = 20
total = 1

for prime in range(2, limit + 1):
    if is_prime(prime):
        power = prime

        while power * prime <= limit:
            power *= prime

        total *= power

print(total)
