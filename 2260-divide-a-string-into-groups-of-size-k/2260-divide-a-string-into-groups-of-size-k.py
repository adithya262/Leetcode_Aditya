from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result = []
        i = 0
        
        while i < len(s):
            group = s[i:i+k]
            
            if len(group) < k:
                group += fill * (k - len(group))
            
            result.append(group)
            i += k
        
        return result
