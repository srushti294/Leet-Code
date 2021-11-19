class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        S = sum(nums)
        for i,x in enumerate(nums):
            if left_sum == S-left_sum-x:
                return i
            left_sum += x
        return -1