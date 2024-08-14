#Complexity Analysis : Time O(n) | Space O(1)
def moveElementToEnd(array, toMove):
    i = 0
    j = len(array) - 1

    while i < j:
        if array[i] == toMove and array[j] != toMove:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
        elif array[i] != toMove:
            i += 1
        elif array[j] == toMove:
            j -= 1
    
    return array

# #Complexity Analysis : Time O(n) | Space O(1)
# def moveElementToEnd(array, toMove):
#     i = 0 
#     j = len(array) - 1
    
#     while i < j:
#         while i < j and array[j] == toMove:
#             j -= 1
#         if array[i] == toMove:
#             array[i], array[j] = array[j], array[i]
#         i += 1
    
#     return array

#Complexity Analysis : Time O(n) | Space O(1)
# def moveElementToEnd(array, toMove):
#     i = 0 

#     for j in range(len(array)):
#         if array[j] != toMove:
#             array[i] = array[j]
#             i += 1
    
#     for k in range(i, len(array)):
#         array[k] = toMove

#     return array

print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2))
