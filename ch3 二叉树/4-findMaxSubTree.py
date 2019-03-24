'''
	要求： 求二叉树的最大子树和
	思路：
			1. 分别求每个子树的和
			2. 后序遍历
			3. 当结点的值与其左右子树和的值相加大于最大值，则更新最大值
	ps : 结点上的数值可正可负；且这里要找的子树：是以某个结点层层递归到叶子节点，不是只有两个左右子树的子树。
'''
class BTree:
	def __init__(self):
		self.data = None
		self.lchild = None
		self.rchild = None


def arrToTree(arr, startIndex, endIndex):
	# 二叉树 = 根节点的data + 左子树结点 + 右子树结点
	# 找到中间元素设为根节点之后，再递归调用本函数将剩余部分填入左右子树
	if endIndex >= startIndex:
		root = BTree()
		mid = int((startIndex + endIndex + 1) / 2)
		root.data = arr[mid]
		root.lchild = arrToTree(arr, startIndex, mid-1)
		root.rchild = arrToTree(arr, mid+1, endIndex)
	else:
		root = None
	return root


class Test:
	def __init__(self):
		# 每个结点可正可负，所以先初始化一个极小的值
		self.maxSum = -2**31

	def findMaxSubTree(self, root, maxRoot):
		if root == None:
			return 0

		# 分别求左右子树的和， return回来的是 sums，子树的和！
		lmax = self.findMaxSubTree(root.lchild, maxRoot)
		rmax = self.findMaxSubTree(root.rchild, maxRoot)

		# 再将左右子树
		sums = lmax + rmax + root.data

		# 如果有和大于最大值，则更新最大值，并用 maxRoot记录该结点
		if sums > self.maxSum:
			self.maxSum = sums
			maxRoot.data = root.data

		return sums






if __name__ == "__main__":
	arr = [1,2,3,4,5,6,7,8,9,10]
	root = arrToTree(arr, 0, len(arr)-1)
	test = Test()
	maxRoot = BTree()
	test.findMaxSubTree(root, maxRoot)
	print('The sum of the tree :', test.maxSum)
	print('The root of the tree :', maxRoot.data)
