
def is_narcissistic(n: int) -> bool:
	"""判断整数 n 是否为水仙花（阿姆斯特朗）数。支持任意位数。"""
	if n < 0:
		return False
	s = str(n)
	power = len(s)
	total = sum(int(ch) ** power for ch in s)
	return total == n


if __name__ == '__main__':
	try:
		num = int(input().strip())
	except Exception:
		print('输入错误')
	else:
		if is_narcissistic(num):
			print(f"{num} 是水仙花数")
		else:
			print(f"{num} 不是水仙花数")
