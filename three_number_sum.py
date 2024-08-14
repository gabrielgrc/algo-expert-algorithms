#Complexity Analysis : Time O(n^2) | Space O(n)
def threeNumberSum(array, targetSum):
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
        leftIdx = i + 1
        rightIdx = len(array) - 1
        while leftIdx < rightIdx:
            currentSum = array[i] + array[leftIdx] + array[rightIdx]
            if currentSum == targetSum:
                triplets.append([array[i], array[leftIdx], array[rightIdx]])
                leftIdx += 1
                rightIdx -= 1
            elif currentSum < targetSum:
                leftIdx += 1
            elif currentSum > targetSum:
                rightIdx -= 1
    return triplets

#Brutal force approach
#Complexity Analysis : Time O(n^3) | Space O(n)
# def threeNumberSum(array, targetSum):
#     array.sort()
#     tripletsTargetSum = []
#     for i in range(len(array)):
#         for j in range(i + 1, len(array)):
#             for k in range(j + 1, len(array)):
#                 if array[k] + array[j] + array[i] == targetSum:
#                     tripletsTargetSum.append([array[i], array[j], array[k]])
    
#     return tripletsTargetSum

print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
