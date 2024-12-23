


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def solution(head: Node):

    cur = head
    while cur:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next

if __name__ == "__main__":
    head = Node(1, Node(1, Node(2, Node(3, Node(3)))))
    pass