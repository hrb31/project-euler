from pathlib import Path

## adapted method from day 18

path = Path(__file__).parent.resolve() / "triangle.txt"

triangle_2d = []

with open(path, "r") as f:
    for line in f:
        triangle_2d.append([int(value) for value in line.split()])


for row in range(len(triangle_2d) - 2, -1, -1):
  for column in range(len(triangle_2d[row])):
    num1 = triangle_2d[row + 1][column]
    num2 = triangle_2d[row + 1][column + 1]
    triangle_2d[row][column] += max(num1,num2)


print(triangle_2d[0][0])
