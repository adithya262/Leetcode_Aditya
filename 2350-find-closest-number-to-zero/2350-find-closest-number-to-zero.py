class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest=nums[0]

        for s in nums:
            if abs(s) < abs(closest):
                closest=s
        if closest <0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest

        