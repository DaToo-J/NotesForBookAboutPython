'''
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

 

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
 
'''
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return 
        
        cur, pre = head, None
        while cur:
            nxt = cur.next
            cur.next = pre 
            pre = cur
            cur = nxt
        return pre




'''
1. 在当前节点`cur` 指向前一节点之前，需要将下一节点暂存起来：`nxt = cur.next`
2. 否则，`cur.next` 指向前一节点`pre`就玩完了：`cur.next = pre`
3. `pre, cur`向后移动时的顺序也是有讲究的，先移`pre`


弯路：
1. 一开始做的时候，想着的是：`cur(1), nxt(2), tmp(3)`
2. 而不是：`None(pre), cur(1), nxt(2)`
3. 这样会陷入死循环，且不容易判断`cur.next.next`
'''