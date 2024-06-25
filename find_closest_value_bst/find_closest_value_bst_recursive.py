# This is the class of the input tree
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#This is the recursive solution
#Complexity Analysis : 
#Average : T O(log(n)) | S O(log(n))
#Worst : O(n) time | O(n) space
def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float("inf"))

def findClosestValueInBstHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBstHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBstHelper(tree.right, target, closest)
    else:
        return closest

# Helper function to insert a new node with given value in BST
def insert(root, value):
    if root is None:
        return BST(value)

    if value < root.value:
        if root.left is None:
            root.left = BST(value)
        else:
            insert(root.left, value)
    else:
        if root.right is None:
            root.right = BST(value)
        else:
            insert(root.right, value)
    
    return root

# Create the root of the BST
root = BST(10)
# Insert elements
insert(root, 5)
insert(root, 2)
insert(root, 1)
insert(root, 5)
insert(root, 15)
insert(root, 13)
insert(root, 14)
insert(root, 22)

# Find the closest value to the target
target = 12
closest_value = findClosestValueInBst(root, target)

print(f"The closest value to {target} in the BST is {closest_value}")
