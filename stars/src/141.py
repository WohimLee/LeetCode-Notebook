

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(head: Node):

    slow = head
    fast = head.next

    while slow != fast:
        if not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
        
    return True


if __name__ == "__main__":

    head = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)


    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2





    pass