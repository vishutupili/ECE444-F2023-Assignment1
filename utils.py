class Utils:
	def reversed(num):
		reversed_num = 0
		is_neg = False
		if type(num) == int:
			# check if the number is negative
			is_neg = False
			if num < 0:
				num *= -1
				is_neg = True
			# while loop to reverse number
			while num > 0:
				curr = num % 10
				reversed_num = (reversed_num * 10) + curr
				num = num // 10
		else: 
			return None

		if is_neg:
			reversed_num *= -1
		return reversed_num
		
	def formatter(num):
		# use existing python functions to convert to binary and octal format
		if type(num) == int:
			binary_num = bin(num)
			octal_num = oct(num)
		else:
			return None, None
		return binary_num, octal_num
