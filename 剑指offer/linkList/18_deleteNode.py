'''
面试题18. 删除链表的节点
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

返回删除后的链表的头节点。

注意：此题对比原题有改动

示例 1:

输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
'''
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        '''
        1. 依然是在`head`之前设置一个值为`None`的`pre`
        2. `pre和cur`向后移的时候：应该先移`pre`，即 `pre = cur`，再移动`cur`


        特色情况：
        1. 头节点`head`的值为`val`，则“掐头”直接返回结果
        '''
        if not head:
            return 
        if head.val == val:
            return head.next
            
        cur, pre = head, None
        while cur:
            if cur.val != val:
                pre = cur
                cur = cur.next
            else:
                pre.next = cur.next
                return head



class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        '''
        这是别人的代码
        设置了伪头节点，此后的指针没有单独存储，直接用head & head.next来代替，8错8错～～
        '''
        dummy = ListNode(0)  # 设置伪结点
        dummy.next = head
        if head.val == val: return head.next # 头结点是要删除的点，直接返回
        while head and head.next:
            if head.next.val == val:   # 找到了要删除的结点，删除
                head.next = head.next.next
            head = head.next
        return dummy.next