def select_sort(lists):
	'''
	经过第一轮比较，找到最小的数，将其和第一个元素对换位置；
	第二轮比较：除第一个元素，找剩余元素中最小的数，将其和第二个元素对换位置；
	直到最后一个元素

	外层循环：遍历每个元素的index，即该轮比较的最小值的index
	内层循环：遍历index之后每个元素，判断是否小于位于index的元素的值，并考虑是否对换位置
	'''
	count = len(lists)

	for i in range(count):
		minIndex = i 
		for j in range(i+1, count):
			if lists[minIndex] > lists[j]:
				minIndex = j
		lists[minIndex], lists[i] = lists[i], lists[minIndex]

	return lists


if __name__ == "__main__":
	lists = [3,6,2,5,1,4,8,1]
	print("Before sorting: ", lists)
	lists = select_sort(lists)
	print("After sorting : ", lists)
