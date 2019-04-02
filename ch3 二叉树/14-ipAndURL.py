'''
	要求：通过 ip 反向查找 域名
	思路：
			1. 可以用字典法
			2. 也可以用Trie树实现前缀检索
				(缺点：耗费内存)
'''
class TrieTree:
	'''
	利用字典来实现trie树
	每一个字母节点表示为字典的key
	子孙节点表示为value，一直嵌套
	'''
	def __init__(self):
		self.trie = {}
		self.size = 0

	def add(self, ip, url):
		ip = ip.strip()
		t = self.trie
		for w in ip:
			if w not in t:
				t[w] = {}		# 将字母w作为key来代表节点
			t = t[w]		 	# 往树的深层进行遍历

		if ip != '':			# 结尾标志
			t[''] = url

	def search(self, ip):
		ip = ip.strip()
		t = self.trie
		for w in ip:
			if w not in t:
				return False
			t = t[w]

		if '' in t:
			return t['']

	def output(self):
		print("{" , self.printTrie(self.trie) , "}")

	def printTrie(self, t, indent=0):
		if t:
			ind = '' + '\t' * indent
			for key in t.keys():
				label = "'%s' : " % key 
				print(ind + label + "{")
				self.printTrie(t[key], indent+1)
			print(ind + ' ' * len(label) + "}")


if __name__ == "__main__":
	tree = TrieTree()
	IPs = ["10.57.11.127", "121.57.61.129", "66.125.100.103"]
	URL = ["samsung.com", "samsung.net", "google.in"]
	for i in range(3):
		tree.add(IPs[i], URL[i])
	print(tree.search(IPs[2]))
