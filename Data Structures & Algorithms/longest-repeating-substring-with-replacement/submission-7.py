class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        prev, counts, c = s[0], [], 0
        for let in s:
            if let == prev: c += 1
            else:
                counts.append((c, prev))
                prev, c = let, 1
        counts.append((c, prev))

        n = len(counts)
        if n == 1: return len(s)

        print(counts)

        def longest_from_here(let, pos, already, remaining):
            print(let, pos, already, remaining)
            c, suc = counts[pos]
            if pos == n - 1:
                if let == suc:
                    return already + c, remaining    
                else:
                    if remaining <= c: return already + remaining, 0
                    else: return already + c, remaining - c
            if suc == let: return longest_from_here(let, pos + 1, already + c, remaining)
            elif remaining < c: return already + remaining, 0
            elif remaining == c:
                suc_c, sucsuc = counts[pos + 1]
                if sucsuc == let: return already + c + suc_c, 0
                else: return already + c, 0
            else: return longest_from_here(let, pos + 1, already + c, remaining - c)

        def how_many_behind(let, pos):
            if pos == -1: return 0
            c, pred = counts[pos]
            if let == pred: return 0
            else: return c + how_many_behind(let, pos - 1)
        
        ans = 1
        for index, (_, letter) in enumerate(counts):
            temp_ans, remaining = longest_from_here(letter, index, 0, k)
            temp_ans += min(remaining, how_many_behind(letter, index - 1))
            print(letter, temp_ans)
            ans = max(temp_ans, ans)
        
        return ans
            
