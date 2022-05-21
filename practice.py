# # Find the sum of all the numbers in an array

# def sumCalculator(ar):
#   sum = 0
#   for i in ar:
#     sum += i
#   return sum

# print(sumCalculator([3, 4, 6, 2, 9]))


# Find the largest number in the array

def largestNum(ar):
  largest = ar[0]
  for i in ar:
    if (i > largest):
      largest = i
  return largest

print(largestNum([5, 67, 89, 34, 12, 96, 6]))
