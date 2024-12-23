




class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse(root: Node):

    stack = [root]
    res = []

    while stack:

        cur = stack.pop()
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)

        res.append(cur.val)
    print(res)




if __name__ == "__main__":
    node2 = Node(2, Node(4), Node(5, None, Node(11)))
    node3 = Node(3, Node(6, Node(12), None), Node(7, Node(14), Node(15)))
    node1 = Node(1, node2, node3)


    traverse(node1)
    pass