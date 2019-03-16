def quickSort(lists, left, right):
	'''
	快速排序：
		1. 找一个基准值key
		2. 从右扫描序列，找到小于key的值，放到left的位置；
		3. 从左扫描序列，找到大于key的值，放到right的位置；
		4. 直到left 和 right 相遇，此时，将key放到right的位置
			(因为right的值给了left，还没有其他小朋友去right的位置，只剩key这个倒霉蛋没有被安排)
			(此时，得到的序列分为3部分： [值小于key的无序序列] [key] [值大于key的无序序列])
			(再此时，需要递归调用本函数大人将key左右的序列分别再快排)

	图解： https://blog.csdn.net/adusts/article/details/80882649
	'''
	if left >= right:
		return lists

	key = lists[left]
	low = left
	high = right

	while left < right:

		# 从右扫描，确保右边序列都大于key
		while left < right and lists[right] >= key :
			right -= 1
		# 将right位置的值放到left，此时，left位置的值在key里；
		# right：指向不满足条件的位置，left：指向头头；
		lists[left] = lists[right]
		
		# 从左扫描，确保左边序列都小于key
		while left < right and lists[left] <= key:
			left += 1
		# 将left位置的值放到right，此时，right位置的值早就被放到上一个while里的头头里了
		lists[right] = lists[left]

	# 此时，right和left相遇了，而且还剩key这个拖油瓶没有被安置好
	# 此right非上一行的right，因为在整个大的while里，right还可以再执行第一个小while(万万没想到吧~~)
	lists[right] = key

	# 递归。 key 左右两边的序列分别快排。
	quickSort(lists, low, left-1)
	quickSort(lists, left+1, high)

	return lists


if __name__ == "__main__":
	lists = [3,6,2,5,1,4,8,1]
	print("Before sorting: ", lists)
	lists = quickSort(lists, 0, len(lists)-1)
	print("After sorting : ", lists)

	print("Finished ...")