class Solution:
    def isPerfectSquare(self, num: int) -> bool: 
        if num==1:
            return True 
        for i in range(2,num//2+1):
            if num/i < i:
                break
            if num/i == i:
                return True
        return False