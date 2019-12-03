# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        #94:
        二叉树的中序遍历
        要点：
            - 每遍历到子树的根节点时，判断其是否有左孩子；
                - 有，对左子树进行中序遍历(在这儿递归)
                  直到叶子结点
                - 没有或读到叶子结点，则print当前root节点
            - 再判断是否有右孩子；
                - 有，对右子树进行中序遍历(在这儿递归)

        '''
        res = []
        def printMidOrder(root):
            if root == None:
                return 
            if root.left != None :
                printMidOrder(root.left)
            res.append(root.val)
            if root.right != None:
                printMidOrder(root.right)  
        printMidOrder(root)
        print(res) 
        return res     

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        #144:
        二叉树读前序遍历：和中序遍历到思想差不多，就是将root节点print的顺序提前了
        '''
        res = []
        def printpreOrder(root):
            if root == None:
                return 
            res.append(root.val)
            if root.left != None :
                printpreOrder(root.left)
            if root.right != None:
                printpreOrder(root.right)  
        printpreOrder(root)
        print(res) 
        return res     



    def postorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        #145：
        二叉树后序遍历：同理
        '''
        res = []
        def printPostOrder(root):
            if root == None:
                return 
            if root.left != None :
                printPostOrder(root.left)
            if root.right != None:
                printPostOrder(root.right)  
            res.append(root.val)
        printPostOrder(root)
        print(res) 
        return res 