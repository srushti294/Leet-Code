class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxx = max(nums)
        index = nums.index(maxx)
        for i in range (len(nums)):
            if nums[i] != maxx:
                if nums[i]*2 > maxx:
                    return -1
        return index
