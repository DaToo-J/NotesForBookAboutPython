'''
	要求：在二叉排序树中，找到第一个大于中位数的结点

	思路：
			1. 二叉排序树：左子树都小于根节点，右子树都大于根节点
			2. 中位数 = （max + min） / 2
			3. max：二叉树的最右下角； min：二叉树的最左下角
			4. 如果结点大于中位数，则遍历右子树；反之，左子树。
'''
class Tree:
	def __init__(self):
		self.data = None
		self.lchild = None 
		self.rchild = None 

def arrToTree(arr, startIndex, endIndex):
	if endIndex >= startIndex:
		root = Tree()
		mid = int((startIndex + endIndex + 1) / 2)
		root.data = arr[mid]
		root.lchild = arrToTree(arr, startIndex, mid-1)
		root.rchild = arrToTree(arr, mid+1, endIndex)
	else:
		root = None
	return root

def getMin(root):
	# 找到min，最左下角
	if root == None:
		return root
	while root.lchild != None:
		root = root.lchild
	return root

def getMax(root):
	# 找到max，最右下角
	if root == None:
		return root
	while root.rchild != None:
		root = root.rchild
	return root

def getNode(root):
	maxNode = getMax(root)
	minNode = getMin(root)
	midNum = (maxNode.data + minNode.data) / 2
	result = None

	while root != None:
		if root.data <= midNum:
			# 如果当前结点小于中位数，则遍历右子树
			root = root.rchild
		else:
			# 否则，在左子树上遍历
			result =  root
			root = root.lchild
	return result



if __name__ == "__main__":
	arr = [1,2,3,4,5,6,7]
	root = arrToTree(arr, 0, len(arr)-1)
	print(getNode(root).data)
