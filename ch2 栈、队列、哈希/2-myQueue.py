class myQueue:
	def __init__(self):
		self.arr = []
		self.front = 0	# 用于记录队列头元素的index
		self.rear = 0	# 用于记录队列尾元素的index

	def isEmpty(self):
		return self.front == self.rear

	def size(self):
		return self.rear - self.front

	def getFront(self):
		# 返回头元素
		if self.isEmpty():
			return None
		return self.arr[self.front]

	def getBack(self):
		# 返回尾元素
		if self.isEmpty():
			return None 
		return self.arr[self.rear-1]

	def deQueue(self):
		# 删除头元素，front往后挪一个位
		if self.rear > self.front:
			self.front += 1
		else:
			print('The queue is empty')

	def enQueue(self, item):
		# 插入元素，从尾巴上插append，并且rear数值也要往后挪一个
		self.arr.append(item)
		self.rear += 1

if __name__ == "__main__":
	queue = myQueue()
	queue.enQueue(1)
	queue.enQueue(2)
	queue.enQueue(2432)
	queue.enQueue(1232)
	queue.enQueue(2676)
	print(queue.arr)
	print("头元素：", queue.getFront())
	print("尾元素：", queue.getBack())