'''
	要求：输入一个整数，找到结点和为该整数的路径。
			其中，路径为根节点到叶子结点的路径
	思路：遍历所有路径，查看和是否为给定的整数。用先序遍历。
'''
class Tree:
	def __init__(self):
		self.data = None
		self.lchild = None 
		self.rchild = None 

def arrToTree(arr, startIndex, endIndex):
	# 二叉树 = 根节点的data + 左子树结点 + 右子树结点
	# 找到中间元素设为根节点之后，再递归调用本函数将剩余部分填入左右子树
	if endIndex >= startIndex:
		root = Tree()
		mid = int((startIndex + endIndex + 1) / 2)
		root.data = arr[mid]
		root.lchild = arrToTree(arr, startIndex, mid-1)
		root.rchild = arrToTree(arr, mid+1, endIndex)
	else:
		root = None
	return root

def findRoad(root, num, sums, node):
	sums += root.data
	node.append(root.data)

	if (root.lchild == None) and (root.rchild == None) and (sums == num):
		# 遍历到叶子节点，且sums为给定整数，则print
		print(node)

	if root.lchild != None:
		findRoad(root.lchild, num, sums, node)
	if root.rchild != None:
		findRoad(root.rchild, num, sums, node)

	# 遍历到叶子节点，且sums不为给定整数，则将最后一个节点删除
	sums -= node[-1]
	node.remove(node[-1])


if __name__ == "__main__":

	arr = [1,2,3,4,5,6,7,8,9,10]
	root = arrToTree(arr, 0, len(arr)-1)
	node = []
	findRoad(root,18, 0, node)
