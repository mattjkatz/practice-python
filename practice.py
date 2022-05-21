# Find the sum of all the numbers in an array
def sumCalculator(ar):
  sum = 0
  for i in ar:
    sum += i
  return sum

print(sumCalculator([3, 4, 6, 2, 9]))