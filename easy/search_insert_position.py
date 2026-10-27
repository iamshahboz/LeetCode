'''
Given a sorted array of distinct integers and a target value, return the 
index if the target is found. If not, return the index where 
it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2 

Input: nums = [1,3,5,6], target = 2
Output: 1

'''

class Solution:
    def searchIndex(self, nums: list[int], target:int)-> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i 
        return len(nums)

print(Solution().searchIndex(nums=[1,3,5,6], target=5))

'''
How it works

* Since the array is sorted, the first index where nums[i] >= target is 
exactly where target belongs — either it’s already there (nums[i] == target), 
or everything before it is smaller and everything from here on is larger 
or equal, so this is the correct insertion point.

* If no element is >= target, it means target is larger than 
everything in the array, so it belongs at the very end: len(nums)

Trace: nums = [1,3,5,6], target = 5
* i=0: 1 >= 5? no
* i=1: 3 >= 5? no
* i=2: 5 >= 5? yes → return 2


Trace: nums = [1,3,5,6], target = 2
* i=0: 1 >= 2? no
* i=1: 3 >= 2? yes → return 1 (correct: 2 would be inserted between 1 and 3)

'''
