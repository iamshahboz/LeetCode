'''
You are given an array of integers nums and an integer target returns an indices of the two numbers
such that they add up to the target. You may assume that each input would have exactly
one solution, and you may not use the same element twice.

Example

Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]

Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]

Example 2
Input: nums = [3, 2, 4] target = 6
Output: [1, 2]

Example 3
Input: nums = [3,3] target = 6
Output: [0, 1]
'''

# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         n = len(nums)
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]


# solution = Solution()
# result = solution.twoSum(nums=[2,7,11,15], target=9)
# print(result)

# better solution

class Solution:
    def twoSum(self, nums: list[int], target: int)-> list[int]:
        seen = {}
        for i, x in enumerate(nums):
            need = target - x
            if need in seen:
                return [seen[need], i]
            seen[x] = i 

print(Solution().twoSum([2,3,4], 6))
print(Solution().twoSum([3,3], 6))

'''
Explanation

The hash map solution rests on one idea: instead of searching for a partner
for each number, remember what you've already seen and check whether the partner is among them.

If x + y = target, then y = target - x. So when you're standing on x, 
you don't need to compare it against every other number. You only need 
to answer one question: "Have I already seen the number target - x?"

Line by line
seen = {} maps value → index. We store the index because the problem asks 
for indices, not values.

for i, x in enumerate(nums) gives the index i and value x together.

need = target - x is the complement we're looking for.

if need in seen checks whether that complement appeared earlier. If yes, we're done: its index is seen[need], and the current index is i.

seen[x] = i runs only if no match was found, so we record the current number for future elements to find.


'''



        