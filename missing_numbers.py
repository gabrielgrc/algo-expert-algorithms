#Complexity Analysis : Time O(n) | Space O(1)
def missingNumbers(nums):
    total = sum(range(1, len(nums) + 3))
    for num in nums:
        total -= num

    averageMissingValue = total // 2
    foundFirstHalf = 0
    foundSecondHalf = 0

    for num in nums:
        if num <= averageMissingValue:
            foundFirstHalf += num
        else:
            foundSecondHalf += num

    expectedFirstHalf = sum(range(1, averageMissingValue + 1))
    expectedSecondHalf = sum(range(averageMissingValue + 1, len(nums) + 3))

    return [expectedFirstHalf - foundFirstHalf, expectedSecondHalf - foundSecondHalf]

#Complexity Analysis : Time O(n) | Space O(n)
# def missingNumbers(nums):
#     includedNums = set(nums)

#     solution = []
#     for num in range(1, len(nums) + 3):
#         if not num in includedNums:
#             solution.append(num)

#     return solution
    

print(missingNumbers([1, 4, 3]))
