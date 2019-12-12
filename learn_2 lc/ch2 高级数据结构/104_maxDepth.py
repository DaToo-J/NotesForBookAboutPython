# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    给定一个二叉树，找出其最大深度。

    二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

    说明: 叶子节点是指没有子节点的节点。

    示例：
    给定二叉树 [3,9,20,null,null,15,7]，

        3
       / \
      9  20
        /  \
       15   7
    返回它的最大深度 3 

    '''
    def maxDepth(self, root: TreeNode) -> int:
        stack = []
        res = []

        if root:
            stack.append((root, 1))
            while stack:
                cur = stack.pop()
                if cur[0].right:
                    stack.append((cur[0].right, cur[1]+1))
                if cur[0].left:
                    stack.append((cur[0].left, cur[1]+1))
                res.append(cur)
            level = [r[1] for r in res]
            return max(level)
        return 0