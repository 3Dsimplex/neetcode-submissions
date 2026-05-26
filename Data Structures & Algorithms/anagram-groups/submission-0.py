from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def to_collection(word: str) -> dict:
            collection = {}
            for letter in word:
                if letter in collection: collection[letter] += 1
                else: collection[letter] = 1
            return collection

        
        total_collection = [(to_collection(word), word) 
            for word in (strs)]

        check, ans = [], []
        for c, w in total_collection:
            if c in check: ans[check.index(c)].append(w)        
            else:
                check.append(c)
                ans.append([w])
        return ans