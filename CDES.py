class DES():
	def __init__(self):
		
		# Table of Position of 64 bits at initial level: Initial Permutation Table
		self.initial_perm = [58, 50, 42, 34, 26, 18, 10, 2,
						60, 52, 44, 36, 28, 20, 12, 4,
						62, 54, 46, 38, 30, 22, 14, 6,
						64, 56, 48, 40, 32, 24, 16, 8,
						57, 49, 41, 33, 25, 17, 9, 1,
						59, 51, 43, 35, 27, 19, 11, 3,
						61, 53, 45, 37, 29, 21, 13, 5,
						63, 55, 47, 39, 31, 23, 15, 7]

		# Expansion D-box Table
		self.exp_d = [32, 1 , 2 , 3 , 4 , 5 , 4 , 5,
				6 , 7 , 8 , 9 , 8 , 9 , 10, 11,
				12, 13, 12, 13, 14, 15, 16, 17,
				16, 17, 18, 19, 20, 21, 20, 21,
				22, 23, 24, 25, 24, 25, 26, 27,
				28, 29, 28, 29, 30, 31, 32, 1 ]

		# Straight Permutation Table
		self.per = [ 16, 7, 20, 21,
				29, 12, 28, 17,
				1, 15, 23, 26,
				5, 18, 31, 10,
				2, 8, 24, 14,
				32, 27, 3, 9,
				19, 13, 30, 6,
				22, 11, 4, 25 ]

		# S-box Table
		self.sbox = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
				[ 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
				[ 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
				[15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13 ]],

				[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
					[3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
					[0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
				[13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9 ]],

				[ [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
				[13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
				[13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
					[1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ]],

				[ [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
				[13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
				[10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
					[3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14] ],

				[ [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
				[14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
					[4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
				[11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ]],

				[ [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
				[10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
					[9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
					[4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13] ],

				[ [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
				[13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
					[1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
					[6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12] ],

				[ [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
					[1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
					[7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
					[2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11] ] ]

		# Final Permutation Table
		self.final_perm = [ 40, 8, 48, 16, 56, 24, 64, 32,
					39, 7, 47, 15, 55, 23, 63, 31,
					38, 6, 46, 14, 54, 22, 62, 30,
					37, 5, 45, 13, 53, 21, 61, 29,
					36, 4, 44, 12, 52, 20, 60, 28,
					35, 3, 43, 11, 51, 19, 59, 27,
					34, 2, 42, 10, 50, 18, 58, 26,
					33, 1, 41, 9, 49, 17, 57, 25 ]
		# --parity matrix
		self.keyp = [57, 49, 41, 33, 25, 17, 9,
				1, 58, 50, 42, 34, 26, 18,
				10, 2, 59, 51, 43, 35, 27,
				19, 11, 3, 60, 52, 44, 36,
				63, 55, 47, 39, 31, 23, 15,
				7, 62, 54, 46, 38, 30, 22,
				14, 6, 61, 53, 45, 37, 29,
				21, 13, 5, 28, 20, 12, 4 ]

		# by shift kam marra 1 or 2
		self.shift_table = [1, 1, 2, 2,
						2, 2, 2, 2,
						1, 2, 2, 2,
						2, 2, 2, 1 ]

		# 56-->48 matrix
		self.key_comp = [14, 17, 11, 24, 1, 5,
					3, 28, 15, 6, 21, 10,
					23, 19, 12, 4, 26, 8,
					16, 7, 27, 20, 13, 2,
					41, 52, 31, 37, 47, 55,
					30, 40, 51, 45, 33, 48,
					44, 49, 39, 56, 34, 53,
					46, 42, 50, 36, 29, 32 ]



	# Binary to decimal
	def bin2dec(self, binary):

		binary1 = binary
		decimal, i, n = 0, 0, 0
		while(binary != 0):
			dec = binary % 10
			decimal = decimal + dec * pow(2, i)
			binary = binary//10
			i += 1
		return decimal

	# Decimal to binary
	def dec2bin(self, num):
		res = bin(num).replace("0b", "")
		if(len(res)%4 != 0):
			div = len(res) / 4
			div = int(div)
			counter =(4 * (div + 1)) - len(res)
			for i in range(0, counter):
				res = '0' + res
		return res

	# Permute function
	def permute(self, k, arr, n):
		permutation = ""
		for i in range(0, n):
			permutation = permutation + k[arr[i] - 1]
		return permutation

	# Left shift
	def shift_left(self, k, nth_shifts):
		s = ""
		for i in range(nth_shifts):
			for j in range(1,len(k)):
				s = s + k[j]
			s = s + k[0]
			k = s
			s = ""
		return k

	# calculating xow of two strings of binary number a and b
	def xor(self, a, b):
		ans = ""
		for i in range(len(a)):
			if a[i] == b[i]:
				ans = ans + "0"
			else:
				ans = ans + "1"
		return ans
	def string2bin(self, a):
		x = bin(int.from_bytes(a.encode(), 'big'))
		return x

	def bin2string(self, f):
		n = int(f, 2)
		n = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
		return n

    
	def key_generation(self, k1):
		# 64-->56
		key = self.permute(k1, self.keyp, 56)
		# Splitting keys
		left = key[0:28] # rkb for RoundKeys in binary
		right = key[28:56] # rk for RoundKeys in hexadecimal
		rkb = []
		for i in range(0, 16):
			# Shifting 
			left = self.shift_left(left, self.shift_table[i])
			right = self.shift_left(right, self.shift_table[i])

			# Combination of left and right string
			combine_str = left + right

			# by-compress elkey 56-->48
			round_key = self.permute(combine_str, self.key_comp, 48)

			rkb.append(round_key)
		self.keys = rkb
	
	def rounds(self, pt, rkb):
		# Initial Permutation
		pt = self.permute(pt, self.initial_perm, 64)

		# Splitting
		left = pt[0:32]
		right = pt[32:64]
		for i in range(0, 16):
			# expanding 32-->48
			right_expanded = self.permute(right, self.exp_d, 48)

			# XOR 
			xor_x = self.xor(right_expanded, rkb[i])

			# S-boxes
			sbox_str = ""
			for j in range(0, 8):
				row = self.bin2dec(int(xor_x[j * 6] + xor_x[j * 6 + 5]))
				col = self.bin2dec(int(xor_x[j * 6 + 1] + xor_x[j * 6 + 2] + xor_x[j * 6 + 3] + xor_x[j * 6 + 4]))
				val = self.sbox[j][row][col]
				sbox_str = sbox_str + self.dec2bin(val)

			# Straight D-box
			sbox_str = self.permute(sbox_str, self.per, 32)

			# XOR
			result = self.xor(left, sbox_str)
			left = result

			# Swap
			if(i != 15):
				left, right = right, left

		# Combination
		combine = left + right

		# Final permutation
		cipher_text = self.permute(combine, self.final_perm, 64)
		return cipher_text



	def encryption(self, message):
		print("Encryption")
		List=[]
		m = 0
		flag = 0
		flagbreak = 0
		cipher_text=''
		mess = self.string2bin(message)
		mess = mess[2:]
		
		for x in range(0, 1000):
			string = ''
			for i in range(flag, flag + 64):

				if i<len(mess):
					string += mess[i]

				if i >= len(mess):
					#print("dakhal")
					string+='0'

					if len(string)== 64:
						flagbreak = 1
						break
			List.append(string)

			flag+=64
			cipher_text += self.rounds(List[m], self.keys) 
			m+=1

			if flagbreak == 1:
				break
			
		return cipher_text, (len(mess)+2)

	def decryption(self, cipher_text, length):
		print("Decryption")
		List1=[]
		text=''
		flag = 0
		flagbreak = 0
		m = 0
		rkb_rev = self.keys[::-1]
		for x in range(0, 1000):
			string = ''
			for i in range(flag, flag + 64):
			
				if i<len(cipher_text):
					string += cipher_text[i]

				if i >= len(cipher_text):
					#print("dakhal")
					string+='0'
					if len(string)== 64:
						flagbreak = 1
						break
					
			List1.append(string)

			if flagbreak == 1:
				break
			
			flag+=64
			text +=self.rounds(List1[m], rkb_rev) 
			m+=1

		text3 = '0b' + text
		text3 = text3[:length]
		plain_text = self.bin2string(text3)
		return plain_text

# def main():
# 	message = input("Enter test: ")
# 	key = "1010101010111011000010010001100000100111001101101100110011011101"
# 	desss = DES()
# 	desss.key_generation(key)
	
#     # # 64-->56
# 	# key1 = desss.permute(key, desss.keyp, 56)
# 	# # Splitting keys
# 	# left = key1[0:28] # rkb for RoundKeys in binary
# 	# right = key1[28:56] # rk for RoundKeys in hexadecimal
# 	# rkb = []
# 	# for i in range(0, 16):
# 	# 	# Shifting 
# 	# 	left = desss.shift_left(left, desss.shift_table[i])
# 	# 	right = desss.shift_left(right, desss.shift_table[i])
# 	# 	# Combination of left and right string
# 	# 	combine_str = left + right
# 	# 	# by-compress elkey 56-->48
# 	# 	round_key = desss.permute(combine_str, desss.key_comp, 48)
# 	# 	rkb.append(round_key)
# 	# desss.keys = rkb




# 	cipher, length = desss.encryption(message)
# 	print("cipher: ", cipher)
# 	print("length: ", length)
# 	plain = desss.decryption(cipher, length)
# 	print("plain: ", plain)
	
# if __name__ == "__main__":
# 	main()
	