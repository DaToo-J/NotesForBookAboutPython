'''
	要求：逐层打印出二叉树结点
	思路：
			1. 另开一个队列，用于存放孩子结点
			2. 当一个根节点出队列时，将其孩子结点送入队列
'''
from collections import deque

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

def printTreeByLayerOrder(root):
	if root == None:
		return

	# 队列queue 用于记录待出队的结点顺序
	queue = deque()

	# 先将root这个倒霉蛋送入队
	queue.append(root)

	while len(queue) > 0:
		# root 要被抛弃咯 ~
		p = queue.popleft()
		print(p.data, end=' ,')

		# p作为根节点出队了，轮到它的左右孩子，被送入队列了
		if p.lchild != None:
			queue.append(p.lchild)
		if p.rchild != None:
			queue.append(p.rchild)


if __name__ == "__main__":
	arr = [1,2,3,4,5,6,7,8,9,10]
	root = arrToTree(arr, 0, len(arr)-1)
	printTreeByLayerOrder(root)