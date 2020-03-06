'''
输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。

 

示例：

给定一个链表: 1->2->3->4->5, 和 k = 2.

返回链表 4->5.

'''
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
    	'''
    	常规方法：用列表存储元素
    	'''
        if not head:
            return 

        res = []
        while head:
            res.append(head)
            head = head.next
        return res[len(res)-k:][0]


    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
    	'''
    	设置两个指针，latter和former初始都为head
    	先让former往前跳k步
    	然后latter和former同时起跳
    	当former跳到链尾时，latter就在倒数第k个节点了
    	'''
        if not head:
            return 

        latter, former = head, head
        for i in range(k):
            former = former.next 
        
        while former:
            latter, former = latter.next, former.next
        return latter