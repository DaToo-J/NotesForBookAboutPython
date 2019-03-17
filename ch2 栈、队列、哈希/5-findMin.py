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


class Stack():
	'''
	要求：用O(1)的时间复杂度求栈中最小元素
	思路：空间换时间。另开一个栈来存放最小值
	'''
	def __init__(self):
		self.elemStack = myStack()	# 正常存放
		self.minsStack = myStack()	# 存放min

	def push(self, data):
		# 如果要入栈的元素小于 minStack的栈顶元素，那么也要 压minStack栈
		self.elemStack.push(data)
		if self.minsStack.isEmpty():
			self.minsStack.push(data)
		else:
			if data < self.minsStack.top():
				self.minsStack.push(data)

	def pop(self):
		# 如果要出栈的元素等于 minStack的栈顶元素，那么也要 弹minStack栈
		topData = self.elemStack.top()
		self.elemStack.pop()
		if topData == self.mins():
			self.minsStack.pop()
		return topData

	def mins(self):
		if self.minsStack.isEmpty():
			return 2 ** 32
		else:
			# minStack的栈顶元素始终是最小值
			return self.minsStack.top()


if __name__ == "__main__":
	s = Stack()
	s.push(422)
	print(s.mins(), s.minsStack.items)
	s.push(322)
	print(s.mins(), s.minsStack.items)
	s.push(43)
	print(s.mins(), s.minsStack.items)
	s.push(14)
	print(s.mins(), s.minsStack.items)
	s.push(46)
	print(s.mins(), s.minsStack.items)
