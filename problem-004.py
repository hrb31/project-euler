## initial solution
def is_palindrome(num):
    number = str(num)
    for i in range(len(number) // 2):
        if number[i] != number[len(number) - i - 1]:
            return False

    return True

largest = 0
num1 = 999

while num1>=100:
  for i in range(999,99,-1):
    total = num1*i
    if is_palindrome(total) and total >= largest:
      largest = total
  num1-=1
  


print(largest)

## better palindrome function
def check(num):
    number = str(num)
    return number == number[::-1]
