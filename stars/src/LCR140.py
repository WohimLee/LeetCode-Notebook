


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next



def solution1(head: Node, k=0):
    fast = slow = head

    for i in range(k):
        fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next
    print(slow.val)

def solution2(head: Node, k=0):
    cur = head
    size = 1
    while cur.next:
        size += 1
        cur = cur.next
    
    cur = head
    for i in range(size-k):
        try:
            cur = cur.next
        except:
            continue
    print(cur.val)

if __name__ == "__main__":

    head = Node(0, Node(1, Node(2, Node(3, Node(4, Node(5))))))
    solution1(head, k=2)