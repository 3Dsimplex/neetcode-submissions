class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = [0, 1]
        
        if len(nums) == 2: return ans
        if target % 2 == 0:
            a = target // 2
            ls = []
            for index, num in enumerate(nums):
                if a == num: ls.append(index)
            if len(ls) > 1: return ls

        goal = {}
        for index, num in enumerate(nums):
            goal[num] = target - num, index
        for index, num in enumerate(nums):
            goal_num, _ = goal[num]
            if goal_num in goal:
                _ , second_index = goal[goal_num]
                if index != second_index :
                    ans[0], ans[1] = index, second_index
                    return ans 
        