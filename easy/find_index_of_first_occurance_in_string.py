'''
Given two strings needle and haystack, return the index of the 
first occurrence of needle in haystack, or -1 if needle is not part of haystack.


Example 1
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2 

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

'''

class Solution:
    def strStr(self, haystack:str, needle: str) -> int:
        n, m = len(haystack), len(needle)

        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i 
        return -1


print(Solution().strStr(haystack="sadbutsad",needle="sad"))

"""
How it works


* n is the length of haystack, m is the length of needle.
* needle can only possibly start at indices 0 through n - m — any 
later and there wouldn’t be enough characters left in haystack to fit all of needle. 
That’s why the loop runs range(n - m + 1).
* At each candidate position i, slice out m characters from haystack starting there (haystack[i:i+m]) 
and compare that slice directly to needle.
* The first position where they match is returned immediately.
* If no position ever matches, return -1.



Trace: haystack = "sadbutsad", needle = "sad"
* n = 9, m = 3, so i ranges from 0 to 6.
* i=0: haystack[0:3] = "sad" → matches needle → return 0.
"""
