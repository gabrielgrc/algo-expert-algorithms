# This is the class of the input tree
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#Complexity analysis : T O(log(n)) balanced tree, O(n) unbalanced tree | S O(1)
def findClosestValueInBst(tree, target):
    closest = tree.value

    current_node = tree
    while current_node is not None:
        if abs(target - current_node.value) < abs(target - closest):
            closest = current_node.value

        if target < current_node.value:
            current_node = current_node.left
        elif target > current_node.value:
            current_node = current_node.right
        else:
            break

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
