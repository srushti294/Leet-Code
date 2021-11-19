class Solution:
    def mySqrt(self, x: int) -> int:
        right = 2
        left = x//2
        if x<2:
            return x
        while(left<=right):
            mid = left + (right-left)//2
            if(mid*mid)<x:
                left = mid+1
            elif(mid*mid)>x:
                right = mid-1
            else:
                return mid
        return right