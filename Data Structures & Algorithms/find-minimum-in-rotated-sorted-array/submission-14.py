class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]: return nums[0]
        while len(nums) > 2:
            mid = int(len(nums)/2)
            if nums[mid] > nums[0]:
                nums = nums[mid:]
                continue
            if nums[mid] < nums[0]:
                nums = nums[:mid+1]
                continue
        return min(nums)