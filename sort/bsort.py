def bubbleSort(L):
  for j in range(len(L)):
    for i in range(len(L) - 1):
      if L[i] > L[i+1]:
        temp = L[i]
        L[i] = L[i+1]
        L[i+1] = temp
    print(L)

def bubbleSort2(L):
   swapped = True
   while swapped:
     swapped = False
     for i in range(len(L) - 1):
       if L[i] > L[i+1]:
        temp = L[i]
        L[i] = L[i+1]
        L[i+1] = temp
        swapped = True
     print(L)

def testBubbleSort():
   test1 = [1, 6, 3, 4, 5, 2]
   bubbleSort2(test1)
   print("-------- next test ------")
   test2 = [6, 1, 2, 3, 4, 5]
   bubbleSort2(test2)
   print("-------- next test ------")
   test3 = [6, 5, 4, 3, 2, 1]
   bubbleSort2(test3)

testBubbleSort()
