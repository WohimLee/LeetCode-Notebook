

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right



def traverse(root: Node):
    cur:Node = root
    stack = []
    res = []
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.value)
        cur = cur.right
    pass


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    
    node1.left, node1.right = node2, node3
    node2.left, node2.right = node4, node5
    node3.left, node3.right = node6, node7
    traverse(node1)
    
    