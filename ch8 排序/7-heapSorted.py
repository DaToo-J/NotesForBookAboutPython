def adjustHeap(lists, i, size):
	'''
	该函数使得以i为顶点的heap为‘大顶堆’
	'''
	lchild = 2 * i + 1
	rchild = 2 * i + 2
	maxs = i

	if i < size / 2:
		# 找出值最大的index，存到maxs
		if lchild < size and lists[lchild] > lists[maxs]:
			maxs = lchild
		if rchild < size and lists[rchild] > lists[maxs]:
			maxs = rchild

		# 既然都找到maxs脚标，那么就一定要它在顶点上咯，赋值给 i
		if maxs != i:
			lists[maxs], lists[i] = lists[i], lists[maxs]
			adjustHeap(lists, maxs, size)

def buildHeap(lists, size):
	for i in range(0, int(size/2))[::-1]:
		adjustHeap(lists, i, size)

def heapSort(lists):
	size = len(lists)
	buildHeap(lists, size)
	print("\nThe lists has been build as a heap: ", lists,'\n')

	for i in range(0, size)[::-1]:
		# 此时的lists，最大值一定在0处，所以将其搞到lists尾巴上
		lists[0], lists[i] = lists[i], lists[0]
		# 但是调整后，lists不一定是头元素为max，所以需要再调整一下
		# 使得最大值在头头上(因为此时的最大值一定在‘以0为顶点、深度为1的树’中，不然就不能满足大顶堆)
		adjustHeap(lists, 0, i)



if __name__ == "__main__":
	lists = [3,6,2,5,1,4,8,1]
	print("Before sorting: ", lists)
	heapSort(lists)
	print("After sorting : ", lists)

	print("\nFinished ...")