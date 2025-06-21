from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = Counter(word)
        freq_list = list(freq.values())
        freq_list.sort()
        min_deletions = float('inf')
        
        for i in range(len(freq_list)):
            target_min = freq_list[i]
            deletions = 0
            for f in freq_list:
                if f < target_min:
                    deletions += f  
                elif f > target_min + k:
                    deletions += f - (target_min + k)  
            min_deletions = min(min_deletions, deletions)
        
        return min_deletions
