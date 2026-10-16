def collatz(num):
  ## returns length of collatz sequence starting at num
  length = 1
  while num >1:
    if num % 2 == 0:
      num = num / 2
      length += 1
    else:
      num = (3*num)+1
      length += 1
      

  return length

start = 1000000
length = 0
number = 0
for i in range(start,0,-1):
  if collatz(i) >= length:
    length = collatz(i)
    number = (i)



print(number)

## memoisation could be used to enhance efficiency
## optimised solution will be added
