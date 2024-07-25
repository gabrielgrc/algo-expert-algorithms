# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# Function to remove duplicates from the linked list in place
#Complexity Analysis : T O(n) | S O(1)
def remove_duplicates(linkedList):
    currentNode = linkedList
    while currentNode is not None and currentNode.next is not None:
        if currentNode.value == currentNode.next.value:
            currentNode.next = currentNode.next.next # Skip the duplicate node
        else:
            currentNode = currentNode.next # Move to the next node

# Example usage:
# Creating a linked list with values 1 -> 1 -> 3 -> 4 -> 4 -> 4 -> 5 -> 6 -> 6
head = LinkedList(1)
head.next = LinkedList(1)
head.next.next = LinkedList(3)
head.next.next.next = LinkedList(4)
head.next.next.next.next = LinkedList(4)
head.next.next.next.next.next = LinkedList(4)
head.next.next.next.next.next.next = LinkedList(5)
head.next.next.next.next.next.next.next = LinkedList(6)
head.next.next.next.next.next.next.next.next = LinkedList(6)

# Removing duplicates
remove_duplicates(head)

# Function to iterate through the linked list and print values
def iterate_linked_list(head):
    current = head
    while current is not None:
        print(current.value) # Process the current node (e.g., print its value)
        current = current.next

# Printing the modified linked list
iterate_linked_list(head)
