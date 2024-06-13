#Complexity analysis : O(n log n) time | O(n) space
def sortedSquaredArray1(array):
    if len(array) == 0:
        return []
    squared_array = [i ** 2 for i in array]
    squared_array.sort()
    return squared_array

#Complexity analysis : O (n) time | O (n) space
def sortedSquaredArray2(array):
    sortedSquares = [0 for _ in array]
    smallerValueIdx = 0
    largerValueIdx = len(array) - 1

    for idx in reversed(range(len(array))):
        smallerValue = array[smallerValueIdx]
        largerValue = array[largerValueIdx]

        if abs(smallerValue) > abs(largerValue):
            sortedSquares[idx] = smallerValue * smallerValue
            smallerValueIdx += 1
        else:
            sortedSquares[idx] = largerValue * largerValue
            largerValueIdx -= 1

    return sortedSquares
           
#print(sortedSquaredArray([1, 2, 3, 5, 6, 8, 9]))
#print(sortedSquaredArray([-2, -1]))
print(sortedSquaredArray([-7, -5, -4, 3, 6, 8, 9]))
