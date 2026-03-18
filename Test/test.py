
def solution(nums):

    res = []

    path = []
    used = [False] * len(nums)

    def backtrack():

        if len(path) == len(nums):
            res.append(path[:])
            return
        
        


# 判断条件是否成立，选择对应处理分支。
if __name__ == "__main__":
    # 初始化或更新变量 nums。
    nums = [1, 2, 3]

    # 四种写法可任选其一进行测试。
    # res = solution.permute(nums)
    res = solution(nums)
    # res = permute_stack(nums)

    pass
