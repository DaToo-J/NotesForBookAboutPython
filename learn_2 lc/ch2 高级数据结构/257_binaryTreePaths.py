'''
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:

输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        '''
        官方题解
        
        '''
        paths = []
        def findChildren(root, p):
            if root:
                p += str(root.val)
                if not root.left and not root.right:
                    paths.append(p)
                else:
                    p += "->"
                    findChildren(root.left, p)
                    findChildren(root.right, p)
                # return paths
        
        p = findChildren(root, '')
        return paths



class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        stack = [[root]]
        paths = []
        while stack:
            Spop = stack.pop()            # [root]
            cur = Spop[-1]                # root
            if cur: 
                if not cur.left and not cur.right:
                    paths.append(Spop)
                if cur.right:
                    t = Spop + [cur.right]
                    stack.append(t)
                if cur.left:
                    t = Spop + [cur.left]
                    stack.append(t)
        res = []
        for p in paths:
            res.append('->'.join([str(i.val) for i in p]))
        return res

class Solution:
    def binaryTreePaths(self, root):
        """
        官方题解
        """
        if not root:
            return []
        
        paths = []
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))
        
        return paths


            
