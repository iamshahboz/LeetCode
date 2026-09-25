'''
Given an integer x, return True if x is a palindrome and False otherwise

Example 1
Input: x = 121
Output: True
Explanation: 121 reads as 121 from left to right and from right to left

Example 2
Input: x = 10 
Output: False


'''

# Common solution

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False 
        number = str(x)
        reverse = number[::-1]
        return number == reverse

print(Solution().isPalindrome(121))
print(Solution().isPalindrome(25))


# better solution

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted = 0
        while x > reverted:
            reverted = reverted * 10 + x % 10
            x //= 10

        return x == reverted or x == reverted // 10