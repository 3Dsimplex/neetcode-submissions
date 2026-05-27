class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums) - 1

        left, right = [1], [1]
        for i in range(l + 1):
            left.append(nums[i] * left[-1])
            right.append(nums[l-i] * right[-1])
        
        return [left[i] * right[l - i] for i in range(l + 1)]


