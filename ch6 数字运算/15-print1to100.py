'''
要求：不使用循环print出1-100
'''
def prints(n):
	if n>0 :
		prints(n-1)
		print(n, end=' ')
if __name__ == "__main__":
	prints(43)