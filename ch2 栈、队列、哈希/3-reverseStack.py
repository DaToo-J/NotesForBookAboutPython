class myStack:
	'''
	模拟栈：后进先出

	'''
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

def moveBottomToTop(s):
	'''
	总体思路：
		每一次都将栈底元素移动到栈顶
		随后，在不含栈顶元素的子栈中，再将栈底元素移动到子栈栈顶
		(类似于，依次将栈底元素冒泡)

	具体执行：
		在不含栈顶元素的子栈中，将栈底元素移动到子栈栈顶
		再将子栈栈顶元素和栈顶元素进行交换 (先push top1, 再push top2)
	'''
	if s.isEmpty():
		return

	top1 = s.top()
	s.pop()

	if not s.isEmpty():
		# 一直递归调用，直到s只剩2个元素
		moveBottomToTop(s)
		# 此后，都是从下面这条语句开始执行
		# 当处理完‘只有2个元素’的子栈时，此时top2=‘子栈的栈顶’，top1=‘未处理时有3个元素的栈顶元素’
		top2 = s.top()

		# Choice 1 ：reverse
		s.pop()
		# 总是后push top2，即总是后放入‘原始的栈底元素’。
		# 等下一次递归时，还会再 top2=s.top()取出栈顶元素的
		s.push(top1)
		s.push(top2)
	else:
		s.push(top1)


		'''
		# Choice 2 ：sorting
		if top1 > top2:
			s.pop()
			s.push(top1)
			s.push(top2)
			return
	s.push(top1)
		'''




def reverseStack(s):
	if s.isEmpty():
		return

	moveBottomToTop(s)
	top = s.top()
	s.pop()
	reverseStack(s)
	s.push(top)

if __name__ == "__main__":
	s = myStack()
	s.push(4)
	s.push(2)
	s.push(43)
	s.push(14)
	s.push(46)
	print(s.items)
	reverseStack(s)
	print(s.items)
