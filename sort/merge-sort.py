# O(nlog(n)) complexity
# Merge routine : n complexity
def merge(left, right):
  result = []
  i, j = 0, 0
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      result.append(left[i])
      i = i + 1
    else:
      result.append(right[j])
      j = j + 1
  while(i < len(left)):
    result.append(left[i])
    i = i + 1
  while(j < len(right)):
    result.append(right[j])
    j = j + 1
  return result  

# Divide : log(n) complexity
def mergeSort(L):
  print(str(L))
  if len(L) < 2:
    return L[:]
  else:
    middle = len(L) // 2
    left = mergeSort(L[:middle])
    right = mergeSort(L[middle:])
    together = merge(left, right)
    print('merged', str(together))
    return together

myList = [28, 47, 20, 4, 12, 1, 30] 
myList2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]

mergeSort(myList)
print()
mergeSort(myList2)
