class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        if x < 0:
            return False
        elif num == num[::-1]:
            return True
        else:
            return False
        
        