'''
	给定一个二叉树的根节点，复制该树
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

def createDupTree(root):
	'''
	思路：tree2的根节点 等于 tree1的根节点
		 递归调用，将左子树、右子树都复制了
	'''
	if root == None:
		return None
	dupTree = Tree()
	dupTree.data = root.data
	dupTree.lchild = createDupTree(root.lchild)
	dupTree.rchild = createDupTree(root.rchild)
	return dupTree

def printTree(root):
	if root == None:
		return 
	if root.lchild != None:
		printTree(root.lchild)
	
	print(root.data, end=' ')

	if root.rchild != None:
		printTree(root.rchild)

if __name__ == "__main__":

	arr = [1,2,3,4,5,6,7,8,9,10]
	root = arrToTree(arr, 0, len(arr)-1)
	root2 = createDupTree(root)
	printTree(root)
	print()
	printTree(root2)