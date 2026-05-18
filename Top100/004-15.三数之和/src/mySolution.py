def solution(nums: list):
    # 先排序。这样后面才能利用有序性做双指针，
    # 也更方便跳过重复值，避免重复三元组。
    nums.sort()

    numElems = len(nums)

    results = []

    # 枚举三元组中的第一个数 nums[i]。
    # 剩下两个数在区间 [i+1, numElems-1] 中用双指针寻找。
    for i in range(numElems - 2):

        curValue = nums[i]

        # 第一个数去重：
        # 如果当前值和前一个值相同，那么以它开头得到的结果
        # 会和上一轮重复，直接跳过。
        if i > 0 and curValue == nums[i-1]:
            continue

        # 排序后，如果当前第一个数已经大于 0，
        # 后面的数只会更大，不可能再凑出 0。
        if curValue > 0:
            break

        # 双指针分别指向剩余区间的左右两端。
        lPointer, rPointer = i+1, numElems-1

        while lPointer < rPointer:
            # 计算当前三数之和，根据结果决定移动哪一边指针。
            sum = curValue + nums[lPointer] + nums[rPointer]
            if sum < 0:
                # 和太小，说明需要更大的数，只能左指针右移。
                lPointer += 1
            elif sum > 0:
                # 和太大，说明需要更小的数，只能右指针左移。
                rPointer -= 1
            else:
                # 找到一组满足条件的解。
                results.append([curValue, nums[lPointer], nums[rPointer]])
                lPointer += 1
                rPointer -= 1

                # 第二个数去重：
                # 如果左指针的新值和刚才用过的一样，
                # 继续右移，避免得到重复三元组。
                while lPointer < rPointer and nums[lPointer] == nums[lPointer - 1]:
                    lPointer += 1
                # 第三个数去重：
                # 如果右指针的新值和刚才用过的一样，
                # 继续左移，避免得到重复三元组。
                while lPointer < rPointer and nums[rPointer] == nums[rPointer + 1]:
                    rPointer -= 1

    return results

if __name__ == "__main__":

    nums = [-1, 0, 1, 2, -1, -4]
    print(solution(nums))
