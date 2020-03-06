'''
寻找两个链表的相交节点
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。

'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        '''
        1. 利用集合去重的特点，先将`headA`都加进集合，当`headB`往里面填元素时，集合长度不变的话，说明遇到交点了
        '''
        if not headA or not headB: return None
        collect = set()
        while headA:
            collect.add(headA)
            headA = headA.next
        while headB:
            length1 = len(collect)
            collect.add(headB)
            if length1 == len(collect):
                return headB
            headB = headB.next
        return None


    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        '''
        将两个链表分别存放到两个栈，再利用出栈顺序的特点，判断交点
        '''
        if not headA or not headB: return None
        queueA = []
        queueB = []
        while headA:
            queueA.append(headA)
            headA = headA.next
        while headB:
            queueB.append(headB)
            headB = headB.next
        if queueB[-1] != queueA[-1]:
            return None
        while queueB and queueA and queueB[-1] == queueA[-1]:
            queueA.pop()
            res = queueB.pop()
        return res