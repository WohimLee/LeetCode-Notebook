

def serch(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def solution(nums, target):

    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

if __name__ == "__main__":
  
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    print(solution(nums1, target1))  # 输出: 4


    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    print(solution(nums2, target2))  # 输出: -1
