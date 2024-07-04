class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    #Complexity Analysis : T O(v + e) | S O(v)
    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array

# Create the graph
root = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")
h = Node("H")
i = Node("I")
j = Node("J")
k = Node("K")

root.children = [b, c, d]
b.children = [e, f]
d.children = [g, h]
f.children = [i, j]
g.children = [k]

# Perform DFS
result = []
root.depthFirstSearch(result)

print("DFS Traversal Result:", result)
