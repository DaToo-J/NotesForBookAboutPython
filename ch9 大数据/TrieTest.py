class TrieTree:
	'''
	利用字典来实现trie树
	每一个字母节点表示为字典的key
	子孙节点表示为value，一直嵌套
	'''
	def __init__(self):
		self.trie = {}
		self.size = 0

	def add(self, word):
		word = word.strip()
		t = self.trie
		for w in word:
			if w not in t:
				t[w] = {}		# 将字母w作为key来代表节点
			t = t[w]			# 往树的深层进行遍历

		if word != '':			# 结尾标志
			t[''] = ''

	def search(self, word):
		word = word.strip()
		t = self.trie
		for w in word:
			if w not in t:
				return False
			t = t[w]

		if '' in t:
			return True
		return False

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
	tree.add("hello")
	tree.add("help")
	tree.add("word")
	tree.add("world")
	tree.output()
	print(tree.search("hello"))
	print(tree.search("hell"))
	print(tree.search("help"))