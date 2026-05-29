class Solution:      
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = set()
        for i in range(1, len(nums)-1):
            t = - nums[i]
            j, k = 0, len(nums) - 1
            while (j < i) and (i < k):
                while (nums[j] == nums[j+1]) and (j+1 < i):
                    j += 1
                while (nums[k] == nums[k-1]) and (i < (k-1)):
                    k -= 1
                if nums[j] + nums[k] == t:
                    ans.add((nums[j], nums[i], nums[k]))
                    j += 1
                    k -= 1
                if nums[j] + nums[k] > t:
                    k -= 1
                if nums[j] + nums[k] < t:
                    j += 1
        return [list(x) for x in ans]
                