from collections import deque
'''
要求：	实现LRU (Least Recently Used);
实现：	当把页面载入缓存中时，缓存已满，那么就将最近最少使用的页面踢出去。
注意：	1. 新页面载入缓存时(addPage())
			a. 该页面不存在 ： 插入队列(enQueue())
				1) 缓存已满 ： 删除队列尾巴元素(即，最近最少使用的页面)
				2) 缓存未满 ： 从队列头部插入
			b. 该页面已存在 ： 移到队首
				1) 本来就在队首 ： 不改变
				2) 本来不在队首 ： 从队列中删除它，再从头插入

		2. 哈希表：记录queue中存在的元素
'''
class LRU:
	def __init__(self, cacheSize):
		self.cacheSize = cacheSize
		self.queue = deque()
		self.hashSet = set()

	def isQueueFull(self):
		return len(self.queue) == self.cacheSize

	def enQueue(self, pageNum):
		# 插入队列： 1) 缓存已满	 2) 缓存未满
		if self.isQueueFull():
			self.hashSet.remove(self.queue[-1])
			self.queue.pop()

		#(真正插入时，缓存都不满)
		self.queue.appendleft(pageNum)
		self.hashSet.add(pageNum)


	def addPage(self, pageNum):
		# 新页面载入缓存：	a) 该页面不存在 -> enQueue()	 
		# 					b) 该页面已存在 -> 移到队首
		if pageNum not in self.hashSet:
			self.enQueue(pageNum)
		elif pageNum != self.queue[0]:
			self.queue.remove(pageNum)
			self.queue.appendleft(pageNum)

	def printQueue(self):
		while len(self.queue) > 0:
			print(self.queue.popleft())
		print()

if __name__ == "__main__":
	lru = LRU(3)
	lru.addPage(4)
	lru.addPage(2)
	lru.addPage(6)
	lru.addPage(7)
	lru.printQueue()
	lru.printQueue()

	lru.addPage(121)
	# lru.printQueue()
	lru.addPage(65)
	lru.addPage(4)
	lru.addPage(243)