'''

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000


For example, 2 is written as II in Roman numeral, just two ones added together. 
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, 
which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. 
There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.
'''


class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        for i in range(len(s)):
            curr = values[s[i]]
            if i + 1 < len(s) and curr < values[s[i+1]]:
                total -= curr 
            else:
                total += curr

        return total

print(Solution().romanToInt('IV'))

'''

How it works
values maps each symbol to its numeral value.
Walk through the string one character at a time.
For each symbol, look at the next one:
If the current value is smaller than the next one (like I before V), 
that's a subtraction case (IV = 4), so subtract it.

Otherwise, add it normally.
The check i + 1 < len(s) guards against looking past the end of the string on the 
last character.


Trace: s = "MCMXCIV"

i	s[i]	curr	next	curr < next?	action	total
0	M	    1000	C=100	no	+1000	1000
1	C	    100	    M=1000	yes	-100	900
2	M	    1000	X=10	no	+1000	1900
3	X	    10	    C=100	yes	-10	    1890
4	C	    100	    I=1	    no	+100	1990
5	I	    1	    V=5	    yes	-1	    1989
6	V	    5	    — (last)	n/a	+5	1994
'''

# better solution

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        total = values[s[-1]]
        for i in range(len(s) - 2, -1, -1):
            curr = values[s[i]]
            nxt = values[s[i + 1]]
            if curr < nxt:
                total -= curr
            else:
                total += curr

        return total


'''
How it works


Start by adding the value of the last character — the rightmost symbol is 
never subtracted, so it's always safe to add first.

Walk backward from the second-to-last character to the first.
For each symbol, compare it to the one after it (which you've already processed):
If it's smaller, it's a subtraction case → subtract it.
Otherwise → add it.
'''