'''
589. N-ary Tree Preorder Traversal

Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
'''


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        stack = [root]
        result = []
        while len(stack) > 0:
            curr = stack.pop()
            if not curr: continue

            if not curr.children: continue
            l = len(curr.children)
            while l > 0:
                stack.append(curr.children[l - 1])
                l -= 1
        return result