def bubbleSort(lists):
	'''
	冒泡排序：
		1. 两两比较，将大的数往后移；
		2. 第一轮比较后：最大的数在第n个；
		3. 再对前 n-1 个数进行两两比较；
		4. 直到只剩下一个数
	'''

	for i in range(len(lists)-1):
		# 只比较 n-1 次
		for j in range(len(lists) - i - 1):
			# 每次只比较前面无序的序列
			if lists[j] > lists[j+1]:
				lists[j], lists[j+1] = lists[j+1], lists[j]
	return lists



if __name__ == "__main__":
	lists = [3,6,2,5,1,4,8,1]
	print("Before sorting: ", lists)
	lists = bubbleSort(lists)
	print("After sorting : ", lists)

	print("Finished ...")