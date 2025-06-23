class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_palindrome(s):
            return s == s[::-1]
        
        def to_base(num, base):
            res = []
            while num > 0:
                res.append(str(num % base))
                num //= base
            return ''.join(res[::-1])

        def generate_palindromes(length):

            half_len = (length + 1) // 2
            start = 10**(half_len - 1)
            end = 10**half_len
            for half in range(start, end):
                half_str = str(half)
                if length % 2 == 0:
                    yield int(half_str + half_str[::-1])
                else:
                    yield int(half_str + half_str[-2::-1])

        count = 0
        result = 0
        length = 1

        while count < n:
            for num in generate_palindromes(length):
                base_k = to_base(num, k)
                if is_palindrome(base_k):
                    result += num
                    count += 1
                    if count == n:
                        return result
            length += 1
