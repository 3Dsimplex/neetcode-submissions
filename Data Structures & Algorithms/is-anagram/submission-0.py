class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss, tt = {}, {}
        for let in s:
            if let in ss: ss[let] += 1
            else: ss[let] = 1
        for let in t:
            if let in tt: tt[let] += 1 
            else: tt[let] = 1
        if ss == tt: return True
        return False
        