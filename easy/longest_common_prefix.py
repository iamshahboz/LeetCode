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

