class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        count = 0
        value = 0
        power = 1
        
        zeros = s.count('0')
        
        for c in reversed(s):
            if c == '1':
                if value + power <= k:
                    value += power
                    count += 1
            else:
                count += 1
            if power <= k:
                power *= 2
            else:
                pass
        
        return count
