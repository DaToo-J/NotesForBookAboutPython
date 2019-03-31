'''
	要求：20个数组，每个数组有500个元素，且排好序。求这20*500个数的前500的数
	方法：堆排序方法
	思路：
			1. 取出每个数组的第一个元素，放入heap里
			2. 删除heap的顶点，append到result里
			3. 将被删顶点的接班人，放入heap里
				(接班人：该元素所在数组的下一个元素)
			4. 直到result里的元素达到个数要求，循环截止
'''

import heapq

def getTop(data):
	row = len(data)
	col = len(data[0])
	result = [None] * col
	heap = []

	for i in range(row):
		arr1 = (None, None, None)
		# 数值，所在数组，所处index
		arr1 = (-data[i][0], i, 0)# 因为是排好序的，所以索引为0
		heapq.heappush(heap, arr1)

	for i in range(col):
		# 删除顶点, d = (顶点数值， 顶点所在数组， 顶点所处index)
		d = heapq.heappop(heap)
		# 将删除的顶点的数值放到result里面
		result[i] = -d[0]

		# 顶点元素的接班人
		arrNew = (-data[d[1]][d[2]+1], d[1], d[2]+1)
		# 插入到heap里
		heapq.heappush(heap, arrNew)

	return result




if __name__ == "__main__":
	data = [[452, 212, 78, 35], [671, 90, 79, 0], [340, 123, 46, 32],]
	print(getTop(data))