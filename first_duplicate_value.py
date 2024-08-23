#Complexity Analysis : Time O(n) | Space O(1)
def firstDuplicateValue(array):
    for value in array:
        absValue = abs(value)
        if array[absValue - 1] < 0:
            return absValue
        array[absValue - 1] *= -1
    return -1

#Complexity Analysis : Time O(n) | Space O(n)
# def firstDuplicateValue(array):
#     seen = set()
#     for value in array:
#         if value in seen:
#             return value
#         seen.add(value)
#     return -1

#Brute force approach
#Complexity Analysis : Time O(n^2) | Space O(1)
# def firstDuplicateValue(array):
#     minimumSecondIndex = len(array)
#     for i in range(len(array)):
#         value = array[i]
#         for j in range(i + 1, len(array)):
#             valueToCompare = array[j]
#             if value == valueToCompare:
#                 minimumSecondIndex = min(minimumSecondIndex, j)

#     if minimumSecondIndex == len(array):
#         return -1
    
#     return array[minimumSecondIndex]

print(firstDuplicateValue([2, 1, 5, 2, 3, 3, 4]))
