import os

def printDirectory(path):
	'''
	输入文件夹名称
	打印该文件夹里所有文件名
	'''
	for child in os.listdir(path):
		childPath = os.path.join(path, child)
		if os.path.isdir(childPath):
			# 递归！！！
			printDirectory(childPath)
		else:
			print(childPath)


path = 'E:\\001 文档\\'
# printDirectory(path)

def getAllFiles(path):
	'''
	遍历path路径下，所有文件
	'''
	for root,dirs,files in os.walk(path):
		print(root,'\n')
		# E:\001 文档\
		print(dirs,'\n')
		# root下所有文件夹
		print(files,'\n')	
		# ['learn_3 python复习.zip', 'task_1 1130归档.zip'] 
		
		for filename in files:
			name,suf = os.path.splitext(filename)
			print(name)
				# learn_3 python复习
			print(suf)
				# .zip
		break

getAllFiles(path)