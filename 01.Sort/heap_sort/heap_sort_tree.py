

from typing import Optional, List


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.pNode: Optional[TreeNode] = None
        self.lNode: Optional[TreeNode] = None
        self.rNode: Optional[TreeNode] = None



class Heap:
    def __init__(self, values, is_min_heap):
        self.rootNode: Optional[TreeNode] = None
        self.allNodes: List[TreeNode] = []
        self.is_min_heap = is_min_heap

        self.build_complete_tree(values)
        self.heapify()

    def build_complete_tree(self, values):

        self.allNodes = [TreeNode(value=value) for value in values]

        self.rootNode = self.allNodes[0]

        for curNodeIdx in range(1, len(self.allNodes)):
            parNodeIdx = (curNodeIdx - 1) // 2
            
            curNode = self.allNodes[curNodeIdx]
            parNode = self.allNodes[parNodeIdx]
            curNode.pNode = parNode

            if curNodeIdx % 2 == 1:
                parNode.lNode = curNode
            else:
                parNode.rNode = curNode

    def heapify(self):
        lastNodeIdx = len(self.allNodes) - 1
        lastPareIdx = (lastNodeIdx - 1) // 2

        for curNodeIdx in range(lastPareIdx, -1, -1):
            self.sift_down(self.allNodes[curNodeIdx])

    def sift_down(self, node: TreeNode):
        curNode = node
        while curNode is not None:

            bestNode = curNode

            if curNode.lNode and self.should_swap(bestValue=bestNode.value, otherValue=curNode.lNode.value):
                bestNode = curNode.lNode
            if curNode.rNode and self.should_swap(bestValue=bestNode.value, otherValue=curNode.rNode.value):
                bestNode = curNode.rNode

            if bestNode is curNode:
                return
            
            curNode.value, bestNode.value = bestNode.value, curNode.value

            curNode = bestNode

    def should_swap(self, bestValue, otherValue):
        if self.is_min_heap:
            return otherValue < bestValue
        return otherValue > bestValue

    def pop_root(self):

        topValue = self.rootNode.value
        lastNode = self.allNodes.pop()
        lastNodeParent = lastNode.pNode

        if lastNodeParent is not None:
            if lastNodeParent.lNode is lastNode:
                lastNodeParent.lNode = None
            else:
                lastNodeParent.rNode = None
        lastNode.pNode = None

        self.rootNode.value = lastNode.value
        self.sift_down(self.rootNode)
        return topValue



def heap_sort_tree(nums: List[int], reverse: bool = False) -> List[int]:
    """使用链式二叉堆（TreeNode）实现的堆排序，返回新列表。"""

    if len(nums) <= 1:
        return nums[:]

    # 升序 -> 最小堆；降序 -> 最大堆
    heap = Heap(nums, is_min_heap=not reverse)
    return [heap.pop_root() for _ in range(len(nums))]

def heap_sort_tree_asc(nums: List[int]) -> List[int]:
    return heap_sort_tree(nums, reverse=False)


def heap_sort_tree_desc(nums: List[int]) -> List[int]:
    return heap_sort_tree(nums, reverse=True)



if __name__ == "__main__":
    data = [5, 1, 8, 3, 2, 7, 4, 6, 3, 11, 5, 23]
    print("原数组:", data)
    print("树堆排升序:", heap_sort_tree_asc(data))
    print("树堆排降序:", heap_sort_tree_desc(data))
    print("Python sorted 升序:", sorted(data))
    print("Python sorted 降序:", sorted(data, reverse=True))
    print("原数组未修改:", data)