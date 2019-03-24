'''
	要求：将一个有序的数组存入到二叉树中，(该二叉树也是有序)
	思路：
			1. 找出数组的中间元素，设为根节点。
			2. 再将左右部分填入二叉树的左右子树中
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

def printTreeByMidOrder(root):
	# 中序： 左 -> 根 -> 右
	if root == None:
		return

	if root.lchild != None:
		# 先 左子树，递归调用，总会遍历到叶子结点
		# 等结束最底层的递归时，执行下一条语句，遍历那时子树的根节点
		printTreeByMidOrder(root.lchild)

	print(root.data, end=' ,')

	if root.rchild != None:
		printTreeByMidOrder(root.rchild)


if __name__ == "__main__":
	arr = [1,2,3,4,5,6,7,8,9,10]
	root = arrToTree(arr, 0, len(arr)-1)
	print(root.data)
	printTreeByMidOrder(root)