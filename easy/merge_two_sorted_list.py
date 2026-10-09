'''
You are given the heads of two sorted linked lists list1 and list2
Merge two lists into one sorted list.
The list should be made by splicing the nodes of the first two lists 
Return the head of the merged linked list 


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = [0]
Output: [0]


'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode)-> ListNode:
        dummy = ListNode()
        tail = dummy 

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next 

            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next


        tail.next = list1 if list1 else list2

        return dummy.next


'''
How it works

tail tracks the last node we’ve attached so far; it always starts at dummy.

While both lists still have nodes:

    Compare list1.val and list2.val.
    Whichever is smaller (or equal — <= picks list1 to keep the merge stable) gets linked as tail.next.
    Advance the pointer of whichever list we just took from.
    Move tail forward to the node we just attached.

Once one list runs out, the other list is already sorted, so there’s no need to walk it node by node — just 
attach whatever remains directly: tail.next = list1 if list1 else list2.

Return dummy.next, the real head of the merged list (the dummy itself is discarded).

Trace: list1 = [1,2,4], list2 = [1,3,4]


step	    list1	        list2	compare	  attach	    tail now

1	        1→2→4	        1→3→4	1 ≤ 1	    list1’s 1	    1
2	        2→4	            1→3→4	2 > 1	    list2’s 1	    1
3	        2→4	            3→4	    2 ≤ 3	    list1’s 2	    2
4	        4	            3→4	    4 > 3	    list2’s 3	    3
5	        4	            4	    4 ≤ 4	    list1’s 4	    4
'''

    

