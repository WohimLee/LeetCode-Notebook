


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

def reverse(head: Node):
    pre = None
    cur = head
    while cur:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
    return pre

def printlist(head: Node):
    cur = head
    temp = []
    while cur:
        temp.append(cur.val)
        cur = cur.next
    print(temp)


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    new_head = reverse(node1)
    printlist(new_head)
    pass
    

    
    
    pass