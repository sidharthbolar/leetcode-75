'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
Example 1
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
'''
        merged_list = ListNode()
        res = merged_list

        while list1 and list2:
            if list1.val <= list2.val:
                merged_list.next = list1
                list1 = list1.next
            else:
                merged_list.next = list2
                list2 = list2.next
            merged_list = merged_list.next

        if list1 or list2:
            merged_list.next = list1 if list1 else list2

        return res.next