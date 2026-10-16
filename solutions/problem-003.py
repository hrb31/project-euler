## initial solution
def is_prime(num):
  prime = True
  if num < 2:
    return False
  for i in range(2,num):
      if num % i == 0:
        prime = False
        break
  return prime
        
num = 600851475143
factors = []

divisor = 2

while divisor**2 <= num:
  if num % divisor == 0 and is_prime(divisor):
    factors.append(divisor)

  divisor +=1
  
print(factors[len(factors)-1])


## optimised solution
# removed is_prime() function
num = 600851475143
divisor = 2
largest_factor = None

while divisor * divisor <= num:
    while num % divisor == 0:
        largest_factor = divisor
        num //= divisor

    divisor += 1

if num > 1:
    largest_factor = num

print(largest_factor)
