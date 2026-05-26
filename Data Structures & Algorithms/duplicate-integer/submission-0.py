class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if (not nums): return False
        start, end = min(nums), max(nums)
        checks = [0 for i in range(end - start + 1)]
        for i in nums:
            checks[i - start] += 1
            if (checks[i - start] > 1): return True 
        return False