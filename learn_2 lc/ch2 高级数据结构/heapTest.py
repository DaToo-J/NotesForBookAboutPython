'''
#347:
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
'''
from collections import Counter
import heapq


def topK_heapq():
	'''
	heapq 的使用方法们～
	'''

	data = [5,8,3,6,8,7,2,4,6]

	# 1. 创建堆
	heapq.heapify(data)
	print(data)


	# 2. 添加元素
	heapq.heappush(data, 12)
	print(data)

	# 3. 返回最小值，data仍然是最小堆
	minData = heapq.heappop(data)
	print(data)
	print(minData)
	minData = heapq.heappop(data)
	print(data)
	print(minData)

	# 4. 弹出最小元素，压入指定元素
	minData = heapq.heapreplace(data, 11)
	print(data)
	print(minData)

	# 5. 最大、最小的n个元素
	nlarge = heapq.nlargest(4, data)
	nsmall = heapq.nsmallest(4, data)
	print(nlarge)
	print(nsmall)
	print(data)

def topK_counter():
	'''
	counter 的使用方法们～
	'''
	data = [5,8,3,6,8,7,2,5,7,4,7,6,4,6]

	# 1. 初始化
	datadict = Counter(data)
	print(datadict)
	print(datadict.get)
	# 2. 罗列counter字典里的元素
	d = list(datadict.elements())
	print(d)

	# 3. 计数器更新
	datadict.update([2,3,4,5,1])	# 添加
	print(datadict)

	datadict.subtract([3,4,5,6,7,8,9])		# 减少
	print(datadict)

	# 4. 返回topN
	print(datadict.most_common(3))

def topK_solution(nums, k):
	'''
	only use Counter method
	'''
	return [item[0] for item in Counter(nums).most_common(k)]

def topK_solution2(nums, k):
	count =  Counter(nums)
	return heapq.nlargest(k, count.keys(), key=count.get)

# topK_counter()
nums = [5, 5, 8, 8, 3, 6, 6, 6, 7, 7, 7, 2, 4, 4]
res = topK_solution(nums, 4)
res2 = topK_solution2(nums, 4)
print(res)
print(res2)

