'''
Binary Tree Level Order Traversal
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Input: root = [1]
Output: [[1]]

Input: root = []
Output: []
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    if not root:
        return []

    ans = []
    q = [root]
    while q:
        length = len(q)
        ans.append([])
        for _ in range(length):
            node = q.pop(0)
            ans[-1].append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return ans