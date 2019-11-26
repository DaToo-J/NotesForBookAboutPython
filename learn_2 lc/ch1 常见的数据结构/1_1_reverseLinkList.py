#!/usr/bin/python
# -*- coding: utf-8 -*-


# 定义节点class，节点属性 = 节点数据 + 下一节点信息
class LNode:
	def __new__(self,x):
		self.data = x
		self.next = None 

# 定义翻转链表的方法，传入头节点
def Reverse(head):
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
	pre.next = nextNode 	# ⚠️：pre没有next指针，会报错，下面书上的源码也是这个意思

	# nextNode = cur.next
	# cur.next = None
	# pre = cur 
	# cur = nextNode

	print('reverse: ',pre.data,  cur.data, cur.next.data) 

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
		# cur是最后一个节点，pre是倒数第二个节点，二者之间没有指向，让cur指向倒数第二个节点
	cur.next = pre 

	# 6. 此时，head <空> 1 <- ... <- pre <- cur, 
		# head节点还没有指向，应该指向尾部节点，即cur
	head.next = cur 

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
	for i in range(1,11):
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
	Reverse(head)
	printList(head)


if __name__ == '__main__':
	main()













