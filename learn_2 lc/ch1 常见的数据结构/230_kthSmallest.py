# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

说明：
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。

'''
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        '''
        改写了一下中序遍历的算法
        '''
        def midOrder(root, res):
            if root == None:
                return
            if root.left:
                midOrder(root.left, res)
            res.append(root.val)
            if root.right:
                midOrder(root.right, res)

        if root == None:
            return 
        res = []
        midOrder(root, res)
        print(res)
        return res[k-1]




    def kthSmallest(self, root: TreeNode, k: int) -> int:
        '''
        别人的题解似乎更简洁
        '''
        res = None
        def helper(root):
            nonlocal k, res
            if root.left: helper(root.left)
            k -= 1
            if k == 0: 
                res = root.val
                return 
            if root.right: helper(root.right)
        helper(root)
        return res
 