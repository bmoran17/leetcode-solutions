# 21. Merge Two Sorted Lists https://leetcode.com/problems/merge-two-sorted-lists/description/

# You are given the heads of two sorted linked lists list1 and list2.
# - Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# - Return the head of the merged linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # new node
        head = ListNode()
        # pointer
        current = head
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        # points to list with nodes/numbers still left
        current.next = list1 or list2
        return head.next
