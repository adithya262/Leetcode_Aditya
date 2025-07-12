class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        for i in range(len(min(strs, key=len))):  
            char = strs[0][i]  
            for s in strs[1:]:
                if s[i] != char:
                    return strs[0][:i]
        return strs[0][:len(min(strs, key=len))]
