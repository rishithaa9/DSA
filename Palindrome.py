class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        reverse = 0
        num=x
        while num > 0 :
            digit = num % 10
            reverse = reverse * 10 + digit
            num //= 10

        print(reverse)
        if x==reverse:
            return True
        return False