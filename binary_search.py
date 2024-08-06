#Iterative solution
#Complexity Analysis : T O(log n) | S O(1)
def binarySearch(array, target): 
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]
        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1
    
#Recursive solution
#Complexity Analysis : T O(log n) | S O(log n)
# def binarySearch(array, target):
#     return binarySearchHelper(array, target, 0, len(array) - 1)

# def binarySearchHelper(array, target, low, high):
#     if low > high:
#         return -1
#     mid = (low + high) // 2
#     guess = array[mid]
#     if target == guess:
#         return mid
#     elif target < guess:
#         return binarySearchHelper(array, target, low, mid - 1)
#     else:
#         return binarySearchHelper(array, target, mid + 1, high)

print(binarySearch([1, 3, 5, 7, 9], 7))
