def calculate(s):
	s = "".join(s.split())
	stack, tmp = [], []
	n, op = 0, ''
	for c in range(len(s)) :
		if s[c] in  ["*", "/"]:

			if op in ["*", "/"]:
				tmp.append(n)
				tmp = cal_tmp_cc(tmp)
				print('tmp: ', tmp)

			elif tmp:
				stack += tmp
				tmp = []
				tmp.append(n)
			else: 
				tmp.append(n)

			op = s[c]
			n = 0
			tmp.append(s[c])
		elif s[c] in ["+", "-"]:
			if op in ["*", "/"]:
				tmp.append(n)
				tmp = cal_tmp_cc(tmp)
			else:
				tmp.append(n)
			op = s[c]
			tmp.append(s[c])
			n = 0
		elif "0" <= s[c] <= "9":
			n = n * 10 + int(s[c])
		print(s[c], n, op, stack, tmp)
	tmp.append(n)
	if op in ["*", "/"]:
		tmp = cal_tmp_cc(tmp)
	stack += tmp
	print(stack, tmp)
	return cal_tmp_jj(stack)


def cal_tmp_cc(tmp):
	if tmp[1] == "*":
		return [int(tmp[0]) * int(tmp[2])]
	else:
		return [int(tmp[0]) / int(tmp[2])]


def cal_tmp_jj(tmp):
	res = 0
	n = 0
	op = 1
	for t in range(len(tmp)):
		if tmp[t] == "+":
			res += n * op
			op = 1
			n = 0 
		elif tmp[t] == "-":
			res += n * op
			op = -1
			n = 0
		elif tmp[t] != "(":
			n = n * 10 + int(tmp[t])
	res += n * op
	return str(res)



s = "3+2*2" 	# 
# s = " 3+5 / 2 " 	# 5
# s = "14/3-2"	# 2
# s = "2*3*4"
res = calculate(s)
print(res)