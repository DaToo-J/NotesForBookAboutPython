#!/usr/bin/python
# -*- coding: utf-8 -*-


class LNode:
	def __new__(self,x):
		self.data = x
		self.next = None 

# 定义翻转链表的方法，传入头节点
def Reverse(head, pre):
	# 1. 判断链表是否为空
	if head == None or head.next == None:
		return

	# 2. 定义前驱节点pre、当前节点cur、后继节点next
	pre = None
	cur = None
	nextNode = None

	# 3. 将这三个变量滑到：head -> pre -> cur 
	cur = head.next

	pre = cur
	cur = cur.next
	pre.next = nextNode 	

	# 4. 开始翻转
	while cur.next != None:
		# 用其他变量将当前节点的下一节点 (cur.next)，另存为
		nextNode = cur.next
		# 将当前节点的上一节点，托付给cur.next指针，使得cur向前一个节点指
		cur.next = pre
		# 此时，pre <- cur, pre和cur可以往后挪了，挪完之后，pre和cur之间没有指针，所以有第五步
		pre = cur
		cur = nextNode

	# 5. 此时，head <空> 1 <- ... <- pre <空> cur, 
		# 此时，while break 的条件是 cur.next = None
		# cur是最后一个节点，pre是倒数第二个节点，二者之间没有指向，让cur指向倒数第二个节点
	cur.next = pre 

	# 6. 此时，head <空> 1 <- ... <- pre <- cur, 
		# head节点还没有指向，应该指向尾部节点，即cur
	head.next = cur 

	return cur 

def ReverseK(head, k):
	# 判断链表是否有误
	if head == None or head.next == None or k < 2:
		return

	# 初始化一些指针变量
	pre = head 
	begin = head.next
	end = None
	endNext = None

	while begin != None:
		# 设置 begin 和 end ，并把它们放到对应的位置
		end = begin
		for i in range(k-1):
			if end.next != None:
				end = end.next 
			else:
				return 

		# 翻转子链表
		endNext = end.next 	# 记录下一个滑动窗口的begin
		end.next = None 	# 不能让end的next有指向，这样循环才能跳出去，只翻转k个元素
		pre.next = Reverse(pre, begin) 	# Reverse(pre, begin) 返回的是最后一个元素
										# 和书上不一样的是，这里沿用了1_1_reverseLinkList.py的代码
										# 在reverse()函数中，数据结构是 head -> 1 -> 2 -> ...
										# 始终会有一个head指针，为了不修改reverse()代码，因此在传参的时候，需要将begin 和 head(pre)区分开
		begin.next = endNext 	# endNext记录的是下一个滑动窗口的初始节点，这里是让被翻转后的链表和剩下未翻转的建立链接
		pre = begin				# pre(head) 滑到下一个窗口的前一个节点，即begin，此时begin还未滑动
								# head -> 3 -> 2 -> 1
								# 					begin/pre
		begin = endNext		# 再设置下一次滑动窗口的begin





def printList(head):
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next

def main():
	# 定义头节点
	head = LNode()
	# 用cur 记录当前节点，构造链表时，往后滑动可以借助cur
	cur = head


	# 构造链表
	for i in range(1,13):
		# head <null> i
		# =cur <null> n
		n = LNode()
		n.data = i
		n.next = None

		# cur -> n, 给新节点指向，让它加入已有链表中
		cur.next = n 

		# cur(n), 指针cur 往后挪一下
		cur = n 


	# 翻转链表
	printList(head)
	# print('head:', head)
	ReverseK(head, 3)
	print('-------------')
	# print('head:', head)
	printList(head)


if __name__ == '__main__':
	main()













