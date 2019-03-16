def merge(left, right):
	'''
	传入 left right列表，进行合并
	'''
	i,j = 0,0
	result = []

	while  i<len(left) and j<len(right):
		# 分别比较 left 和 right 里的元素
		# 将较小的元素一个个存入result里
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1

	result += left[i:]
	result += right[j:]

	return result

def mergeSort(lists):
	'''
	传入lists，进行递归
	'''

	if len(lists) <= 1:
		return lists

	# 递归调用mergeSort 将 lists 拆分
	num = int(len(lists) / 2)
	left = mergeSort(lists[:num])
	right = mergeSort(lists[num:])

	return merge(left, right)






if __name__ == "__main__":
	lists = [3,6,2,5,1,4,8,1]
	print("Before sorting: ", lists)
	lists = mergeSort(lists)
	print("After sorting : ", lists)

	print("Finished ...")