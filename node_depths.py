# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#This is the iterative approach
#Complexity Analysis : T O(n) | S O(h)
def nodeDepths(root):
    sumOfDepths = 0
    stack = [{"node": root, "depth": 0}]
    while len(stack) > 0:
        nodeInfo = stack.pop()
        node, depth = nodeInfo["node"], nodeInfo["depth"]
        if node is None:
            continue
        sumOfDepths += depth
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})
    return sumOfDepths

#This is the recursive approach
#Complexity Analysis : T O(n), S O(h)
def nodeDepths2(node, depth = 0):
    if node is None:
        return 0
    return depth + nodeDepths2(node.left, depth + 1) + nodeDepths2(node.right, depth + 1)

# Binary tree to test the function
root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)
root.left.left.left = BinaryTree(8)
root.left.left.right = BinaryTree(9)

# Call the nodeDepths function and print the result
print(nodeDepths(root))  
#print(nodeDepths2(root)) 
