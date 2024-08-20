#Complexity Analysis : Time O(n) | Space O(n)
def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]

    leftRunningProduct = 1
    for i in range(len(array)):
        products[i] = leftRunningProduct
        leftRunningProduct *= array[i]

    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        products[i] *= rightRunningProduct
        rightRunningProduct *= array[i]

    return products

#Complexity Analysis : Time O(n) | Space O(n)
# def arrayOfProducts(array):
#     products = [1 for _ in range(len(array))]
#     leftProducts = [1 for _ in range(len(array))]
#     rightProducts = [1 for _ in range(len(array))]
    
#     leftRunningProduct = 1
#     for i in range(len(array)):
#         leftProducts[i] = leftRunningProduct
#         leftRunningProduct *= array[i]

#     rightRunningProduct = 1
#     for i in reversed(range(len(array))):
#         rightProducts[i] = rightRunningProduct
#         rightRunningProduct *= array[i]

#     for i in range(len(array)):
#         products[i] = leftProducts[i] * rightProducts[i]

#     return products

#Brute force approach
#Complexity Analysis : Time O(n^2) | Space O(n)
# def arrayOfProducts(array):
#     products = []

#     for i in range(len(array)):
#         runningProduct = 1
#         for j in range(len(array)):
#             if i != j:
#                 runningProduct *= array[j]
#         products.append(runningProduct)

#     return products

print(arrayOfProducts([5, 1, 4, 2]))
