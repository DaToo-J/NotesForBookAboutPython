'''

给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
'''
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        '''
        别人的代码
        1. 找到重复值时，进入一个`while`循环，这样之后跳出时，才能不包括这些重复的元素
        2. 之后就指针向后移动
        '''
        thead = ListNode('a')
        thead.next = head
        pre,cur = None,thead
        while cur:
            pre=cur
            cur=cur.next
            while cur and cur.next and cur.next.val == cur.val:
                t=cur.val
                while cur and cur.val==t:
                    cur=cur.next
            pre.next=cur
        return thead.next
