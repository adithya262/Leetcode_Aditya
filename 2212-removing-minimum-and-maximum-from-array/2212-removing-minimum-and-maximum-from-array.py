class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)

        min_index=nums.index(min(nums))
        max_index=nums.index(max(nums))

        left=min(min_index,max_index)
        right=max(min_index,max_index)

        delete_from_front=right+1
        delete_from_end=n-left
        delete_from_both_sides=(left+1)+(n-right)

        return min(delete_from_front, delete_from_end, delete_from_both_sides)
