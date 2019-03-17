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

if __name__ == "__main__":
	s = myStack()
	s.push(4)
	s.push(2)
	s.push(43)
	s.push(14)
	s.push(46)
	print(s.items)
	print(s.top())
	print(s.items)
	print(s.pop())
	print(s.items)