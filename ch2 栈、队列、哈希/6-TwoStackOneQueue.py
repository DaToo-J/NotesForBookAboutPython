class myStack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return len(self.items) == 0

	def size(self):
		return len(self.items)

	def top(self):
		# 只返回栈顶元素
		if not self.isEmpty():
			return self.items[len(self.items) - 1]
		else:
			return None

	def pop(self):
		# 栈顶元素 弹栈
		if len(self.items) > 0:
			return self.items.pop()
		else:
			print('The stack is empty!')
			return None

	def push(self, item):
		self.items.append(item)

class Stack:
	'''
	要求：利用2个栈实现1个队列
	思想：当A要出栈时，用B保存A的出栈元素，然后再从B出栈
	'''
	def __init__(self):
		self.A = myStack()
		self.B = myStack()

	def push(self, data):
		self.A.push(data)

	def pop(self):
		if self.B.isEmpty():

			while not self.A.isEmpty():
				top = self.A.top()
				self.B.push(top)
				# 这里递归啦~~~！！！
				# 只要A不为空，就一直pop到B
				# 跳出循环时，A为空，B为A的逆序 
				self.A.pop()

		first = self.B.top()
		self.B.pop()

		return first


if __name__ == "__main__":
	s = Stack()
	s.push(4)
	print(s.A.items, s.B.items,)
	s.push(2)
	print(s.A.items, s.B.items,)
	s.push(43)
	print(s.A.items, s.B.items,)
	print(s.pop())
	print(s.A.items, s.B.items,)
	s.push(14)
	print(s.A.items, s.B.items,)
	s.push(46)
	print(s.A.items, s.B.items,)
	print(s.pop())
	print(s.A.items, s.B.items,)
	print(s.pop())
	print(s.A.items, s.B.items,)
	print(s.pop())
	print(s.A.items, s.B.items,)
