class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = (''.join(filter(str.isalnum,s))).lower()
        if(new_s == new_s[::-1]):
            return True
        else:
            return False