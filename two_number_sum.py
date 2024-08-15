#Complexity Analysis : Time O(n) | Space O(n)
def twoNumberSum(array, targetSum):
    nums = {}
    
    for num in array:
        complement = targetSum - num
        if complement in nums:
            return [complement, num]
        nums[num] = True
    
    return []
    
#Brutal Force approach
#Complexity Analysis : Time O(n^2) | Space O(1) 
# def twoNumberSum(array, targetSum):
#     for i in range(len(array)):
#         for j in range(i + 1, len(array)):
#             if array[i] + array[j] == targetSum:
#                 return [array[i], array[j]]

#     return []

#Complexity Analysis : Time O(nlog(n)) | Space O(1)
# def twoNumberSum(array, targetSum):
#     array.sort()
#     left = 0
#     right = len(array) - 1

#     while left < right:
#         if array[left] + array[right] == targetSum:
#             return [array[left], array[right]]
#         elif array[left] + array[right] < targetSum:
#             left += 1
#         elif array[left] + array[right] > targetSum:
#             right -=1
    
#     return []

print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
