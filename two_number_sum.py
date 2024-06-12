#Complexity Analysis : O(n^2) time | O (1) space
def twoNumberSum1(array, targetSum):
    # Write your code here.
    # Loop through each element in the array
    for i in range(len(array)):
        # Loop through each element again for the pair
        for j in range(i + 1, len(array)):
            # Check if the sum of the current pair is equal to the targetSum
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]

    return []

#Complexity Analysis : O(n) time | O(n) space
def twoNumberSum2(array, targetSum):
    # Initialize an empty dictionary to store numbers that were checked
    nums = {}
    
    # Iterate through each number in the array
    for num in array:
        # Calculate the complement of the current number
        complement = targetSum - num
        
        # Check if the complement exists in the dictionary
        if complement in nums:
            # If it exists, return the pair as a list
            return [complement, num]
        
        # Otherwise, add the current number to the dictionary
        nums[num] = True
    
    # If no pair is found, return an empty list
    return []

print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
