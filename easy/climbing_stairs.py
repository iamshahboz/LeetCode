'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps


Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev, curr = 1, 2          # ways(1), ways(2)
        for _ in range(3, n + 1):
            prev, curr = curr, prev + curr

        return curr

'''How it works

* prev is ways(k-2) and curr is ways(k-1), starting at k = 3.
* Each iteration computes the next value prev + curr, then shifts: the old curr becomes prev, and the new sum becomes curr.
* After the loop, curr holds ways(n).


Trace:        n = 5
k	    prev	    curr (before)	    new sum	                prev, curr after
3	    1	            2	                3	                    2, 3
4	    2	            3	                5	                    3, 5
5	    3	            5	                8	                    5, 8


Return 8.

'''
