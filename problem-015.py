def factorial(n):
  total = 1
  for i in range(n,0,-1):
    total *= i
  return total


def routes(n):
  ## total routes is C(2n,n)
  numerator = factorial(2*n)
  denominator = factorial(n) * factorial((2*n)-n)
  routes = numerator // denominator
  return routes

print(routes(20))
  
