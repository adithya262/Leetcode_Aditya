class Solution(object):
    MOD = 10**9 + 7

    def precompute_factorials(self, max_n):
        fact = [1] * (max_n + 1)
        inv_fact = [1] * (max_n + 1)
        
        for i in range(1, max_n + 1):
            fact[i] = fact[i - 1] * i % self.MOD

        inv_fact[max_n] = pow(fact[max_n], self.MOD - 2, self.MOD)
        
        for i in range(max_n - 1, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % self.MOD

        return fact, inv_fact

    def nCk(self, n, k, fact, inv_fact):
        if k < 0 or k > n:
            return 0
        return fact[n] * inv_fact[k] % self.MOD * inv_fact[n - k] % self.MOD

    def countGoodArrays(self, n, m, k):
        fact, inv_fact = self.precompute_factorials(n)

        combinations = self.nCk(n - 1, k, fact, inv_fact)
        power = pow(m - 1, n - k - 1, self.MOD)

        result = m * combinations % self.MOD * power % self.MOD
        return result
