# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def middleNode(self, linkedList):
        slowNode = linkedList
        fastNode = linkedList

        while fastNode is not None and fastNode.next is not None:
            slowNode = slowNode.next
            fastNode = fastNode.next.next
        
        return slowNode

# Helper function to create a linked list from a list and return the head
def createLinkedList(linkedList):
    if not linkedList:
        return None
    head = LinkedList(linkedList[0])
    currentNode = head
    for value in linkedList[1:]:
        currentNode.next = LinkedList(value)
        currentNode = currentNode.next
    return head

# Helper function to print the linked list from a given node
def printLinkedList(linkedList):
    currentNode = linkedList
    while currentNode:
        print(currentNode.value, end=" -> ")
        currentNode = currentNode.next
    print("None")

# Create a linked list from a list
linkedListValues = [2, 7, 3, 5]
head = createLinkedList(linkedListValues)

# Find and print the middle node
solution = Solution()
middleNode = solution.middleNode(head)

# Print the result
print("The middle node value is :", middleNode.value)
print("The linked list starting from the middle node is :")
printLinkedList(middleNode)
