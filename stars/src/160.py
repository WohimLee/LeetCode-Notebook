class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 计算链表的长度
        def getLength(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        
        # 获取两个链表的长度
        lenA = getLength(headA)
        lenB = getLength(headB)
        
        # 将两个链表的起点对齐
        while lenA > lenB:
            headA = headA.next
            lenA -= 1
        while lenB > lenA:
            headB = headB.next
            lenB -= 1
        
        # 同时向前遍历寻找相交节点
        while headA and headB:
            if headA == headB:
                return headA  # 找到相交节点
            headA = headA.next
            headB = headB.next
        
        return None  # 没有相交节点

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getLength(head: Node):
    length = 0
    cur = head
    while cur:
        cur = cur.next
        length += 1
    return length


def solution(headA: Node, headB: Node):

    lenA = getLength(headA)
    lenB = getLength(headB)
    cur_A = headA
    cur_B = headB

    while lenA > lenB:
        cur_A = cur_A.next
        lenA -= 1
    
    while lenB > lenA:
        cur_B = cur_B.next
        lenB -= 1

    while cur_A and cur_B:
        if cur_A == cur_B:
            return cur_A
        
        cur_A = cur_A.next
        cur_B = cur_B.next

    return None



if __name__ == "__main__":
    node6 = Node(6, Node(7, Node(8)))

    headA = Node(1)
    headA_2 = Node(2)
    headA.next = headA_2
    headA_2.next = node6
    
    headB = Node(3)
    headB_4 = Node(4)
    headB_5 = Node(5)
    headB.next = headB_4
    headB_4.next = headB_5
    headB_5.next = node6
    
    
    
    print(getLength(headA))
    print(getLength(headB))
    print(solution(headA, headB).val)
    pass
