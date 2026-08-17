class Solution(object):
    def isPalindrome(self, x):
        n = x
        b = 0
        while n > 0:
            digit = n % 10
            b = b * 10 + digit
            n = n // 10
        if x == b:
            return True
        else:
            return False
    