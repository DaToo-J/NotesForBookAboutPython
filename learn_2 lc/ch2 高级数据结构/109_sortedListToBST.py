'''
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定的有序链表： [-10, -3, 0, 5, 9],

一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def findMid(head):
            mid = head
            end = head
            pre = None
            while end and end.next:
                pre = mid
                mid = mid.next
                end = end.next.next
            if pre:
                pre.next = None  

            return mid 

        def buildTree(head):
            if not head:
                return

            mid = findMid(head)
            root = TreeNode(mid.val)

            if mid == head:
                return root

            root.left = buildTree(head)
            root.right = buildTree(mid.next)

            return root
        
        return buildTree(head)