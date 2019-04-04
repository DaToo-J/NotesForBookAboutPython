'''
要求：统计数字num的二进制数的1的个数
'''
def countOne(num):
	'''
	例如：
		6(110) 
		5(101)
	  &	------
		=(100)

	思路：
		将数字num与 (num-1)求&，能将num的最后一个1去掉
		只需count会需要多少次 ‘&运算’，就能计算出有多少个1
	'''
	count = 0 
	while num > 0:
		if num != 0:
			num = num & (num-1)
		count += 1
	return count

def countOne2(num):
	'''
	思路：
		每次都判断num的最后一位是否为1(通过和1做‘&运算’)
		判断完了之后就将最后一位去掉(通过右移1位)
	'''
	count = 0 
	while num > 0:
		if (num & 1) == 1:
			count += 1
		num >>= 1

	return count 


if __name__ == "__main__":
	num1 = 44
	num2 = 36
	num3 = 63
	# print(countOne(num1))
	# print(countOne(num2))
	# print(countOne(num3))
	print(countOne2(num1))
	print(countOne2(num2))
	print(countOne2(num3))