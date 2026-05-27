class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        size = [None for _ in nums]

        def calc_size(ind: int):
            if size[ind]: return size[ind]
            if ind == len(nums):
                size[ind] = 1
                return 1
            max_size = 0
            for j in range(len(nums)):
                if nums[j] == nums[ind] + 1: 
                    max_size = max(max_size, calc_size(j))
            size[ind] = max_size + 1
            return max_size + 1

    
        for i in range(len(nums)): calc_size(i)
        if size: return max(size)
        else: return 0
        