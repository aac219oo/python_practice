'''
Given an integer x, return true if x is a palindrome, and false otherwise.
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        tmp = x
        y = 0
        if x > 0:
            while tmp:
                y = y*10 + tmp%10
                tmp = tmp//10
            return y == x
        else:
            return False
        
print(Solution().isPalindrome(234540032))