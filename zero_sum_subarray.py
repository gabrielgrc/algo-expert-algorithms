#Complexity Analysis : Time O(n) | Space O(n)
def zeroSumSubarray(nums):
    cumulativeSumSet = set()
    currentSum = 0

    for num in nums:
        currentSum += num

        if currentSum == 0 or currentSum in cumulativeSumSet:
            return True
        
        cumulativeSumSet.add(currentSum)

    return False

print(zeroSumSubarray([-5, -5, 2, 3, -2]))
