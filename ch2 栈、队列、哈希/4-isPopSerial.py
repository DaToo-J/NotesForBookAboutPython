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

def isPopSerial(push, pop):
	'''
	判断pop序列是否push序列的出栈序列
	'''

	# 1. push、 pop 不能为空
	if push == None or pop == None:
		return False

	# 2. 两个序列要等长
	pushLen = len(push)
	popLen = len(pop)
	if pushLen != popLen:
		return False

	# 3. 初始化index、设置一个空栈待push序列进栈
	pushIndex = 0
	popIndex = 0
	stack = myStack()

	while pushIndex < pushLen:
		# 4. 将push序列入栈stack，一个一个入
		stack.push(push[pushIndex])
		pushIndex += 1

		# 5. 如果stack的栈顶元素是pop序列的第一个元素，则stack出栈 ^ pop序列移到下一个元素
		while (not stack.isEmpty()) and stack.top() == pop[popIndex]:
			stack.pop()
			popIndex += 1

	# 6. 确保stack此时为空，全部出栈，且pop被遍历到最后一个元素
	return stack.isEmpty() and popIndex == popLen










if __name__ == "__main__":
	push = '12345'
	pop = '32541'
	print(isPopSerial(push, pop))
