'''
bitmap通常基于数组来实现，数组的每个元素可看成是一系列二进制数，所有元素组成更大的二进制集合；
python的整数类型为有符号类型，所以一个整数可用位数为31位
'''
import math
class Bitmap():
	def __init__(self, maxLength):
		# 计算需要多少个数组元素，向上取整
		self.size = int(math.ceil(maxLength/31))
		
		# 初始化bitmap
		self.arr = [0 for i in range(self.size)]

	def calElemIndex(self, num,):
		# 计算num在数组中的索引，向下取整(因为是从0开始)
		return int(math.floor(num / 31))

	def calBitIndex(self, num):
		# 计算num在数组元素中的位索引，和31取模
		return num % 31

	def set(self, num):
		# 置1操作，将第byteIndex位的二进制位置1, (1 << byteIndex)
		elemIndex = self.calElemIndex(num)
		byteIndex = self.calBitIndex(num)
		elem = self.arr[elemIndex] 
		self.arr[elemIndex] = elem | (1 << byteIndex)

	def clean(self, num):
		# 置0操作，将第byteIndex位的二进制位置0, (~(1 << byteIndex))
		# 和set是互反操作
		elemIndex = self.calElemIndex(num)
		byteIndex = self.calBitIndex(num)
		elem = self.arr[elemIndex] 
		self.arr[elemIndex] = elem & (~(1 << byteIndex))

	def test(self, num):
		# 判断num是否在bitmap中
		elemIndex = self.calElemIndex(num)
		byteIndex = self.calBitIndex(num)
		if self.arr[elemIndex] & (1 << byteIndex):
			return True
		return False

def sortArr(arrTest):
	'''
	将 arrTest 利用bitmap来进行排序
	'''
	maxLength = max(arrTest)
	bitmap = Bitmap(maxLength)
	afterSort = []

	for i in arrTest:
		bitmap.set(i)

	for i in range(maxLength+1):
		if bitmap.test(i):
			afterSort.append(i)

	return afterSort



if __name__ == "__main__":
	bitmap = Bitmap(87)		# 使得整个bitmap有3个元素
	bitmap.set(0)
	bitmap.set(34)			# 在第1个数组元素的第3位，用二进制表示则为 1000 (8)
	print('bitmap的数组为： ',bitmap.arr)
	print('测试 34 是否在bitmap中： ',bitmap.test(34))

	print('------------------')

	arrTest = [45, 2, 78, 35, 67, 90, 879, 0, 340, 123, 46]
	print(sortArr(arrTest))
