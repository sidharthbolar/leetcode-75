'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Input: root = [2,1,3]
Output: true

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Input = Tree with root 
Outoput = Boolean
Axioms = -231 <= Node.val <= 231 - 1
Assumptions = 
Approach = Binary search to check 
    if left value of child is < than parent
    if right value of child is > than parent
    Exit on first mismatch

'''


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        else:
            stack = [root]
            while (stack):
                curr = stack.pop(0)

                if (curr.left is not None) & (curr.right is not None):
                    print("here 2")
                    if curr.left.val < curr.val:
                        stack.append(curr.left)
                    else:
                        return False
                    if curr.right.val > curr.val:
                        stack.append(curr.right)
                    else:
                        return False
                else:
                    if (curr.left is None) & (curr.right is not None):
                        return False
                    if (curr.left is not None) & (curr.right is None):
                        return False
                    return True
            return True
