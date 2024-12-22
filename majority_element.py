#Complexity Analysis : Time O(n) | Space O(1)
def majorityElement(array):
    count = 0
    answer = None

    for value in array:
        if count == 0:
            answer = value
        if value == answer:
            count += 1
        else:
            count -= 1
    
    return answer

#Complexity Analysis : Time O(n) | Space O(1)
# def majorityElement(array):
#     answer = 0

#     for currentBit in range(32):
#         currentBitValue = 1 << currentBit
#         onesCount = 0

#         for num in array:
#             if (num & currentBitValue) != 0:
#                 onesCount += 1
        
#         if onesCount > len(array) / 2:
#             answer += currentBitValue
    
#     return answer

print(majorityElement([1, 2, 3, 2, 2, 1, 2]))
