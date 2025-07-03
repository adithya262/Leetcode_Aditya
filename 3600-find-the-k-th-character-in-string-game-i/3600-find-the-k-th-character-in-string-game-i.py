class Solution:
    def kthCharacter(self, k: int) -> str:
        def helper(k):
            if k == 1:
                return 'a'
            length = 1
            steps = 0
            while 2 * length < k:
                length *= 2
                steps += 1
            if k <= length:
                return helper(k)
            else:
                ch = helper(k - length)
              
                return chr((ord(ch) - ord('a') + 1) % 26 + ord('a'))
        
        return helper(k)
