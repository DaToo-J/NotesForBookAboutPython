import math

def shellSort(lists):
	'''
	希尔排序
	'''
	count = len(lists)
	step = 3
	group = math.ceil(count / step)

	while group > 0:
		for i in range(group) :
			j = i + group

			while j < count:
				# 进入单个group内，每次比较两个脚标为k j的数
				k = j - group
				key = lists[j]
				while k >= 0:
					if lists[k] > key:
						# 如果在k的值比较大，往后挪
						lists[k+group] = lists[k]
						lists[k] = key
					# 将k往前挪，确保group内小的数，往前面滚
					k -= group
				# 比较完当前的k 和 j，将j往后挪，确保group内的数都有被遍历到
				j += group

		# 更新step
		if group == math.ceil(group / step):
			break
		group = math.ceil(group / step)

	return lists




if __name__ == "__main__":
	lists = [3,6,2,5,32,1,4,324,5,5,21,8,1]
	print("Before sorting: ", lists)
	lists = shellSort(lists)
	print("After sorting : ", lists)

	print("Finished ...")