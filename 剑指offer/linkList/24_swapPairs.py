'''
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.

'''

class Solution:
	'''
	1. 要用到3个指针
	2. 过程`1->2->3` (`cur->nxt->3`)到 `2->1->3`：
		* 一定要先让`1`指向`3`，即 `cur.next = nxt.next`，否则`2`指向`1`之后，就不能从`2`找到`3`了
			* 此时：`1->3` & `2->3`
		* 现在要让`2`指向`1`，即 `nxt.next = cur`
			* 此时：`1->3` & `2->1`  = `2->1->3` =  `nxt->cur->3`
		* 得到想要的顺序，就将`cur`向后移，即`cur = cur.next`
		* 但是，这样会存在问题：得到下次反转2个元素时，不能和这次反转结果连在一起，所以最开始要有一个`pre`，起到链接每次反转结果的作用，能将`1`和`4`连接


	'''
    def swapPairs(self, head: ListNode) -> ListNode:
        # if not head: return
        if not head or not head.next: return head

        cur = head
        pre = ListNode(0)
        if head.next:
            head = head.next
        while cur and cur.next:
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = cur
            pre.next = nxt
            pre = cur
            cur = cur.next
        return head
