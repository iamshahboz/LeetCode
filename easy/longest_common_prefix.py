'''

Write a function to find the longest common prefix string amongst an array of strings
If there is no common prefix, return an empty string "".

Example 1 

Input: strs = ["flower","flow", "flight"]
Output: "fl"


'''

class Solution:
    def longestCommonPrefix(self, strs:list[str]) -> str:
        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix


print(Solution().longestCommonPrefix(['apple','appstore','appendix']))


'''
How it works

prefix = strs[0] is our first guess: the entire first word.
For each remaining string s, check whether it starts with prefix.
If not, chop the last character off prefix and check again. Repeat until it matches.
If prefix becomes empty, no common prefix exists, so return "" right away.
After all strings are processed, whatever is left in prefix is common to all of them.

'''


# Better solution

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        first = strs[0]

        for i in range(len(first)):
            ch = first[i]
            for s in strs[1:]:
                if i == len(s) or s[i] != ch:
                    return first[:i]

        return first


'''
How it works

Use the first string as the reference. Its characters are the only candidates for the prefix.

For each position i, take ch = first[i] and compare it against s[i] in every other string.

Stop and return first[:i] as soon as either:
i == len(s): some string is too short to have a character at position i, or
s[i] != ch: a mismatch.

If the loop finishes without a mismatch, the entire first string 
is the prefix (e.g. ["abc", "abcd"]).

'''

