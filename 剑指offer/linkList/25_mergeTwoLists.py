'''
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
限制：

'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

		'''
		1. 遇到的问题，一开始想着同时比较`l1,l2` 
		2. 但是，最后的结果回溯不到头节点，所以利用python复制的特点，让`res`和`cur`在初始化的时候就“绑定”在一起，`cur`作为指针向前移，`res`作为伪头节点，好在最后返回结果的时候返回。
		'''

        cur1, cur2 = l1, l2
        res = cur = ListNode(0)
        while cur1 and cur2:
            if cur1.val > cur2.val:
                cur.next = cur2
                cur2 = cur2.next
            else:
                cur.next = cur1
                cur1 = cur1.next
            cur = cur.next                
        cur.next = cur1 if cur1 else cur2
        return res.next