‘’‘
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3

’‘’
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ‘’‘
        1. `pre = cur`不能放在`if`外，因为如果有重复的值，那么`pre`是呆在原地不动的
        2. 只有`cur`每次雷打不动地往后移动
        ’‘’
        if not head: return
        cur = head
        pre = ListNode(0)
        pre.next = cur
        val = set()
        while cur:
            if cur.val not in val:
                val.add(cur.val)
                pre = cur
            else:
                pre.next = cur.next
            cur = cur.next
        return head