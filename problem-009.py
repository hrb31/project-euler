## a + b + c = 1000
## a^2 + b^2 = c^2
## a^2 + b^2 = (1000-a-b)^2
## simplify, you get:
### 1000(500-a) / (1000 - a)

def calculate(a):
  b = (1000*(500-a)) / (1000 - a)
  return b

product = 0

for a in range(1,333):
  b = calculate(a)
  c = 1000 - a - b
  condition = (a + b + c == 1000) and b.is_integer() and c.is_integer()
  if condition:
    product = a * b * c


print(product)
  
  
