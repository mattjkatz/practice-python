# # Find the sum of all the numbers in an array

def sumCalculator(ar):
  sum = 0
  for i in ar:
    sum += i
  return sum

# print(sumCalculator([3, 4, 6, 2, 9]))


# # Find the largest number in the array

def largestNum(ar):
  largest = ar[0]
  for i in ar:
    if (i > largest):
      largest = i
  return largest

# print(largestNum([5, 67, 89, 34, 12, 96, 6]))


# Print an array reversed

def reverseList(ar):
  ar_reversed = []
  i = len(ar) - 1
  while i >= 0:
    ar_reversed.append(ar[i])
    i -= 1
  return ar_reversed

# print(reverseList([2, 5, 3, 8, 11]))


# # print the first 100 digits of the fibbonaci sequence

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

# fibbonaci()


# # Remove duplicates from an array

def removeDuplicates(ar):
  compAr = []
  for i in ar:
    duplicate = False
    for j in compAr:
      if (i == j):
        duplicate = True
    if (duplicate == False):
      compAr.append(i)
  return compAr

# print(removeDuplicates([2, 5, 7, 3, 5, 89, 3, 1, 5]))


# # Find the two largest numbers

def twoLargestNum(ar):
  lg = ar[0]
  second_lg = lg
  for i in ar:
    if (i > lg):
      second_lg = lg
      lg = i
    elif (i > second_lg):
      second_lg = i
  print(lg)
  print(second_lg)

# twoLargestNum([2, 5, 23, 67, 8, 9, 1, 4, 34])


# return a string of a number with commas ever third digit

def numAddCommas(int):
  int_split = reverseList(list(str(int)))
  new_int = []
  if (len(int_split) > 3):
    i = len(int_split) - 1
    for j in list(str(int)):
      new_int.append(int_split[i])
      if (i % 3 == 0 and i != 0):
        new_int.append(",")
      i -= 1
    print(''.join(new_int))
  else:
    print(int)

# numAddCommas(5000/3)


# bubble sort

def bubbleSort(ar):
  ar_sorted = []
  i = 0
