from collections import deque
'''
要求： 
	1. 设计一个排队系统，使得每个用户都能看到自己在队列中所处的位置；
	2. 并且用户可以随时加入或退出队列；
	3. 当队列发生变化时，用户所处位置的序号能够得到及时反馈

思路：
	1. 给 User 对象增加 seq 属性记录其所处位置；
	2. 加入：从队列尾巴加入；		退出：直接从队列remove/popleft；
	3. 加入：seq正常计数+1；		退出：重新更新队列所有用户的seq
'''

class User:
	def __init__(self, id, name):
		self.id = id
		self.name = name
		self.seq = 0

	def getName(self):
		return self.name

	def setName(self, name):
		self.name = name

	def getSeq(self):
		return self.seq

	def setSeq(self, seq):
		self.seq = seq

	def getId(self):
		return self.id

	def equals(self, arg0):
		o = arg0
		return self.id == o.getId()

	def toString(self):
		return 'id:' + str(self.id) + '		name: ' + str(self.name) + '		seq: ' + str(self.seq)

class myQueue:
	def __init__(self):
		# deque ： 两端都可以进行操作的序列
		# q ： 安置用户的队列
		self.q = deque()

	def enQueue(self, u):
		# 进队列(从尾巴进入)
		u.setSeq(len(self.q)+1)		# u 入队，修改它的seq属性
		self.q.append(u)			# 同时，加入到队列 q 中


	def deQueue(self):
		# 出队列(从头出)
		self.q.popleft()
		self.updateSeq()


	def deQueueRemove(self, u):
		# 队列中的人随机离开
		self.q.remove(u)
		self.updateSeq()


	def updateSeq(self):
		# 只要有人离开就更新seq
		i = 1
		for s in self.q:
			s.setSeq(i)
			i += 1


	def printList(self):
		for u in self.q:
			print(u.toString())

if __name__ == "__main__":
	u1 = User(1, 'user1')
	u2 = User(2, 'user2')
	u3 = User(3, 'user3')
	u4 = User(4, 'user4')
	u5 = User(5, 'user5')
	queue = myQueue()
	queue.enQueue(u1)
	queue.enQueue(u2)
	queue.enQueue(u3)
	queue.enQueue(u4)
	queue.enQueue(u5)
	queue.printList()
	print()
	queue.deQueueRemove(u3)
	queue.printList()