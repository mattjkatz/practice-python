# # Find the sum of all the numbers in an array

# def sumCalculator(ar):
#   sum = 0
#   for i in ar:
#     sum += i
#   return sum

# print(sumCalculator([3, 4, 6, 2, 9]))


# # Find the largest number in the array

# def largestNum(ar):
#   largest = ar[0]
#   for i in ar:
#     if (i > largest):
#       largest = i
#   return largest

# print(largestNum([5, 67, 89, 34, 12, 96, 6]))


# # Print an array reversed

# def reverseList(ar):
#   ar_reversed = []
#   i = len(ar) - 1
#   while i >= 0:
#     ar_reversed.append(ar[i])
#     i -= 1
#   return ar_reversed

# print(reverseList([2, 5, 3, 8, 11]))

# print the first 100 digits of the fibbonaci sequence

def fibbonaci():
  a = 0
  b = 1
  print(a)
  print(b)
  for i in range(1, 100):
    c = a + b
    print(c)
    a = b
    b = c

fibbonaci()
