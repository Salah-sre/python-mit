# 1D version
def findPeak(intArr, low, high):
    lenght = len(intArr)
    mid = int(low + (high-low)/2)
    if (( mid == 0 or intArr[mid-1] <= intArr[mid] ) and ( mid == lenght-1 or intArr[mid] >= intArr[mid+1] )):
        return intArr[mid]
    elif (mid > 0 and intArr[mid-1] > intArr[mid]):
        findPeak(intArr, low, mid-1)
    else:
        findPeak(intArr, mid+1, high)

def findMaxInColumn(matrice, midcol, rows):
    maxIndex = 0
    for i in range(rows):
        if matrice[i][midcol] > matrice[maxIndex][midcol]:
            maxIndex = i
    print('maxIndex', maxIndex)
    return maxIndex

# n*m matrice complexity is nlog2(m)
def findPeak2D(matrice, startCol, endCol):
    rows = len(matrice)
    midcol = int(startCol + (endCol-startCol)/2)
    print('midcol', midcol)
    maxRow = findMaxInColumn(matrice, midcol, rows)
    
    if(( midcol == startCol or matrice[maxRow][midcol] >= matrice[maxRow][midcol-1] ) and ( midcol == endCol or matrice[maxRow][midcol] >= matrice[maxRow][midcol+1])):
        return matrice[maxRow][midcol]
    elif ( midcol > 0 and matrice[maxRow][midcol-1] > matrice[maxRow][midcol] ):
        return findPeak2D(matrice, 0, midcol-1)
    return findPeak2D(matrice, midcol+1, endCol);

arr=[12, 40, 49, 57, 27, 36, 10, 45, 32, 18, 6, 15, 50, 8]
print('Peak of list:', arr, ' is', findPeak(arr, 0, len(arr)))

#arr2D = [[10,8,10,10,10,8,10,10], [14,13,12,11,14,13,12,11], [15,9,11,21,15,9,11,2],[16,17,19,20,16,17,19,20]]
arr2D=[[12, 40, 49, 57, 27, 36, 10, 45, 32, 18, 6, 15, 50, 8]]
print('Peak of matrice:', arr2D, ' is', findPeak2D(arr2D, 0, len(arr2D[0])-1))
