class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        max_len = 0
        start = 0

        for i, char in enumerate(s):
            if char in last_seen and last_seen[char] >= start:
                start = last_seen[char] + 1

            last_seen[char] = i
            max_len = max(max_len, i - start + 1)

        return max_len
