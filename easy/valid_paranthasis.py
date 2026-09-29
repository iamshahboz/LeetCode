'''

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false


'''

class Solution:
    def is_valid(self, s: str) -> bool:
        pairs = ['()','[]',"{}"]
        prev_len = -1 

        while prev_len != len(s):
            prev_len = len(s)
            for p in pairs:
                s = s.replace(p, "")

        return s == ""

solution = Solution()
print(solution.is_valid("()[]{}"))   # True
print(solution.is_valid("(]"))       # False
print(solution.is_valid("([)]"))     # False
print(solution.is_valid("([])")) 


'''

How it works

How it works
Repeatedly scan for any of "()", "[]", "{}" as a substring and delete it.
Keep looping as long as the string keeps shrinking.
If nothing is left, every bracket was matched correctly.
Trace: s = "([])"


Round 1: look for "()" — not found as-is. 
Look for "[]" — found inside ([]) → remove it → "()".

Round 2: look for "()" — found → remove it → "".
String is empty → True.


Trace: s = "([)]"
Round 1: no occurrence of "()", "[]", or "{}" appears anywhere (the brackets are interleaved, 
not nested correctly).
Nothing changes → loop stops → s = "([)]" is not empty → False. Correct

'''