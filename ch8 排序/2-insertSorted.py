def insert_sorted(lists):
	'''
	一组记录分为： 有序序列 + 无序序列
	分别遍历无序序列的元素，将其插入到有序序列中

	[有序序列:  ... ,lists[j]]   [key, ... , 无序序列]
	'''
	count = len(lists)

	for i in range(1,count):
		key = lists[i]
			# key: 无序序列中第一个元素
		j = i - 1
			# lists[j]: 有序序列中最后一个元素

		while j >= 0:
			if lists[j] > key :
				# 如果 lists[j] <= key，就直接追加到有序序列尾巴上
				# 否则，lists[j] 和 key 对换位置，再遍历有序序列前面的元素，调整顺序
				lists[j+1] = lists[j]
				lists[j] = key
			j -= 1
			
	return lists



if __name__ == "__main__":
	lists = [3,6,2,5,1,4,8,1]
	print("Before sorting: ", lists)
	lists = insert_sorted(lists)
	print("After sorting : ", lists)

	print("Finished ...")