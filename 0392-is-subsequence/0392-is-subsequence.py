class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        S=len(s)
        T=len(t)

        if s =='': return True
        if S>T: return False

        j=0

        for char in t:
            if s[j] == char:
                if j == S-1:
                    return True
                j+=1 
        return False

        