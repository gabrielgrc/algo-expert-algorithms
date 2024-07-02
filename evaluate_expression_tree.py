class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Complexity Analysis : T O(n) | S O(h)
def evaluateExpressionTree(tree):
    if tree.value >= 0:
        return tree.value

    leftValue = evaluateExpressionTree(tree.left)
    rightValue = evaluateExpressionTree(tree.right)

    if tree.value == -1:
        return leftValue + rightValue
    if tree.value == -2:
        return leftValue - rightValue
    if tree.value == -3:
        return int(leftValue / rightValue)

    return leftValue * rightValue


if __name__ == "__main__":
    # Test case for the expression (((2 * 3) - 2) + (8 / 3))
    tree = BinaryTree(-1,
                      BinaryTree(-2,
                                 BinaryTree(-4, BinaryTree(2), BinaryTree(3)),
                                 BinaryTree(2)),
                      BinaryTree(-3, BinaryTree(8), BinaryTree(3)))
    print(evaluateExpressionTree(tree))  # Output: 6
