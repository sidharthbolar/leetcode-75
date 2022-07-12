''''
Middle of the linkedlist
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def legthLinkedList(head, lengthLL=0):
            result = 0
            while (head):
                lengthLL += 1
                head = head.next
            return int(lengthLL / 2) + 1

        lengthLL = legthLinkedList(head)
        while (lengthLL):
            lengthLL -= 1
            print(lengthLL)

            result = head
            head = head.next
        return result
