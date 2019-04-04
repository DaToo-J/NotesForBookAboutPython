def intoBinary(num):
	bit = []
	hexNum = 10
	for i in range(hexNum):
		b = num >> i 
		# b = int(num / (2 ** i))(除以2的i次方)
		c,d = divmod(b,2)
		# c,d = (a//b, a%b)(商,余)(对上一步的商求余)
		bit.append(str(d))

	return ''.join(bit[::-1])

def intoHex(num):
	hexs = ""
	remainder = 0
	while num != 0:
		# 对num模16求余，得remainder
		remainder = num % 16
		# print(remainder, num)
		if remainder < 10:
			# 加‘0’：每得到一个余都左移
			hexs = str(remainder + int('0')) + hexs
		else:
			# 将大于9的余数转成字母
			hexs = chr(remainder - 10 + ord("A")) + hexs
		num = num >> 4
	return hexs

if __name__ == "__main__":
	num1 = 44
	num2 = 36
	num3 = 63
	# print(intoBinary(num1))
	# print(intoBinary(num2))
	# print(intoBinary(num3))
	print(intoHex(num1))
	print(intoHex(num2))
	print(intoHex(num3))