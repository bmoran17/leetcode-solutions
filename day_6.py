<<<<<<< HEAD
# 26. Remove Duplicate from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
    # Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
    #The remaining elements of nums are not important as well as the size of nums.
    # Return k.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # right pointer
        i = 1
        # left pointer
        for j in range(1, len(nums)):
            # if left pointer is different from right pointer
            if nums[j] != nums[j - 1]:
                # place diff num in position of right pointer 
                nums[i] = nums[j]
                i += 1
        return i
    
=======
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
>>>>>>> 715cab52281d27c7779ed14b4513cc9d55f88201
