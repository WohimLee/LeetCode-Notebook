


def majorityElement(nums):
    # 初始化候选元素和计数器
    candidate = None
    count = 0
    
    # 第一遍遍历，找到候选多数元素
    for num in nums:
        if count == 0:
            candidate = num  # 更新候选人
        count += 1 if num == candidate else -1
    return candidate



def leetcode(nums):

    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1

if __name__ == "__main__":
    nums = [2,2,1,1,1,2,2]
    majorityElement(nums)
