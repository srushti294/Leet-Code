class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n):
            j = i+1
            k = n-1
            while(j<k):
                sum=nums[i]+nums[j]+nums[k]
                if(sum==0):
                    if([nums[i],nums[j],nums[k]]not in ans):
                        ans.append([nums[i],nums[j],nums[k]])
                    k=k-1
                    j=j+1
                elif(sum<0):
                    j=j+1
                else:
                    k=k-1
        return ans