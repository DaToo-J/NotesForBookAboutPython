'''
	要求：对二叉树进行镜像反转

	思路：遍历到非叶子节点时，将其左右子树互换
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


def printTree(root):
	'''
	先序遍历
	'''
	if root == None:
		return 
	if root.lchild != None:
		printTree(root.lchild)
	
	print(root.data, end=' ')

	if root.rchild != None:
		printTree(root.rchild)

def reverseTree(root):
	if root == None:
		return

	reverseTree(root.lchild)
	reverseTree(root.rchild)

	root.lchild, root.rchild = root.rchild, root.lchild




if __name__ == "__main__":

	arr = [1,2,3,4,5,6,7]
	# arr = [1,2,3,4,5,6,7,8,9,10]
	root = arrToTree(arr, 0, len(arr)-1)
	printTree(root)
	reverseTree(root)
	print()
	printTree(root)