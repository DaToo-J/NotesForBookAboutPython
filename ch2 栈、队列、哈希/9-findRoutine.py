'''
要求： 给出一堆车票信息(含起点和终点)，找出这趟旅程的路线
思路： 
		1. 利用车票信息构建一个字典
		2. 再将该字典的键值反转得到另一个字典
		3. 起点： 第一个字典的键中，没有在第二个字典的键中出现的值
		4. 从‘起点’开始摸索下去，逐个找目的地，形成一条路线
'''

def findRoutine(tickets):
	# 1. 反转 tickets 的键值
	# 2. 找到起点
	# 3. 从起点出发，遍历路径

	# 1.
	reverseTickets = dict()
	for k,v in tickets.items():
		reverseTickets[v] = k

	# 2. 
	start = None
	for k,v in tickets.items():
		if k not in reverseTickets:
			start = k
			break
	if start == None:
		print("输入的信息不合理")
		return

	# 3. 
	routine = []
	routine.append(start)
	to = tickets[start]
	while to != None:
		routine.append(to)
		to = tickets.get(to, None)

	print(' -> '.join(routine))


if __name__ == "__main__":
	tickets = dict()
	tickets["Xi'an"] = "Chengdu"
	tickets["Beijing"] = "Shanghai"
	tickets["Dalian"] = "Xi'an"
	tickets["Shanghai"] = "Dalian"
	findRoutine(tickets)

