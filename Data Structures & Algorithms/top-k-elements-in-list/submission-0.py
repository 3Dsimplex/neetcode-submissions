class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = [num for num in nums]
        counts = [0 for i in range(2001)]
        for num in nums:
            counts[num] += 1 
        ans = []
        while len(ans) < k:
            i = 0
            for num in nums:
                if (num) in ans: continue
                if (i) in ans: i = num
                if counts[num] > counts[i]: i = num
            ans.append(i)
        return ans
