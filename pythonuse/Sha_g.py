#coding:utf-8

import random

def sha_g(password):
	key = "49a04ebd08453b52076b069af24c2ae2"

	def binary(a):# transformation du str mdp en chaine binaire
		b = ""
		l1 = [bin(ord(i))[2:] for i in a]
		for i in l1:
			b += str(i)
		return b

	def convhexa(compressed):# conversion de la chaine binaire en hexadécimale
		l = []
		l1 = []
		for i in range(0, len(compressed), 4):
			l.append(compressed[i] + compressed[i+1] + compressed[i+2] + compressed[i+3])
		compressed = ""
		for i in l:
			if i == "0000":
				l1.append("0")
			elif i == "0001":
				l1.append("1")
			elif i == "0010":
				l1.append("2")
			elif i == "0011":
				l1.append("3")
			elif i == "0100":
				l1.append("4")
			elif i == "0101":
				l1.append("5")
			elif i == "0110":
				l1.append("6")
			elif i == "0111":
				l1.append("7")
			elif i == "1000":
				l1.append("8")
			elif i == "1001":
				l1.append("9")
			elif i == "1010":
				l1.append("a")
			elif i == "1011":
				l1.append("b")
			elif i == "1100":
				l1.append("c")
			elif i == "1101":
				l1.append("d")
			elif i == "1110":
				l1.append("e")
			elif i == "1111":
				l1.append("f")

		for i in l1:
			compressed += i

		return compressed

	def compress(binarret, mdp, leng):# fixation de la longueur de la chaine binaire à leng bits
		compressed = ""

		def more(result, binliste, leng):
			a = 0
			while len(result) < leng and a == 0:
				for i in range(len(binliste)):
					result += binliste[i]
					if len(result) >= leng:
						a = 1
						break
					else:
						pass
			return result

		def less(result, leng):
			while len(result) > leng:
				result = result[:-1]
				if len(result) == leng:
					break
			return result

		def divide(result):
			l = [i for i in result]
			resulti = ""
			if len(result)%2 == 0:
				for i in range(0, len(result), 2):
					resulti += result[i]
			else:
				result += 0
				for i in range(0, len(result), 2):
					resulti += result[i]

			return resulti

		if compressed == "":
				compressed = binarret
		else:
			pass
		l1 = [bin(ord(i))[2:] for i in mdp]
		while len(compressed) != leng:
			if len(compressed) < leng:
				compressed = more(compressed, l1, leng)
				if len(compressed) == leng:
					break
				else:
					pass
			elif len(compressed) > leng:
				if len(compressed) >= leng*1.5:
					compressed = divide(compressed)
				else:
					compressed = less(compressed, leng)

				if len(compressed) == leng:
					break
				else:
					pass
			else:
				compressed = binarret
				break

		return compressed

	def crypt(compressed, key):# encrypte compressed avec la clé de chiffrement hexadécimale, compressed et key doivent avoir la meme len
		
		def convert(string):
			M = [i for i in string]
			M1 = []
			for i in range(len(M)):
				if M[i] == "0":
					M1.append(0)
				elif M[i] == "1":
					M1.append(1)
				elif M[i] == "2":
					M1.append(2)
				elif M[i] == "3":
					M1.append(3)
				elif M[i] == "4":
					M1.append(4)
				elif M[i] == "5":
					M1.append(5)
				elif M[i] == "6":
					M1.append(6)
				elif M[i] == "7":
					M1.append(7)
				elif M[i] == "8":
					M1.append(8)
				elif M[i] == "9":
					M1.append(9)
				elif M[i] == "a":
					M1.append(10)
				elif M[i] == "b":
					M1.append(11)
				elif M[i] == "c":
					M1.append(12)
				elif M[i] == "d":
					M1.append(13)
				elif M[i] == "e":
					M1.append(14)
				else:
					M1.append(15)
			return M1

		def addnum(key, liste):
			L1 = []
			for i in range(len(key)):
				L1.append(key[i] + liste[i])
				if L1[i] > 15:
					L1[i] -= 16
				else:
					pass
			return L1

		def reconvert(liste):
			global result 
			M1 = []
			for i in range(len(liste)):
				if liste[i] == 0:
					M1.append(0)
				elif liste[i] == 1:
					M1.append(1)
				elif liste[i] == 2:
					M1.append(2)
				elif liste[i] == 3:
					M1.append(3)
				elif liste[i] == 4:
					M1.append(4)
				elif liste[i] == 5:
					M1.append(5)
				elif liste[i] == 6:
					M1.append(6)
				elif liste[i] == 7:
					M1.append(7)
				elif liste[i] == 8:
					M1.append(8)
				elif liste[i] == 9:
					M1.append(9)
				elif liste[i] == 10:
					M1.append("a")
				elif liste[i] == 11:
					M1.append("b")
				elif liste[i] == 12:
					M1.append("c")
				elif liste[i] == 13:
					M1.append("d")
				elif liste[i] == 14:
					M1.append("e")
				else:
					M1.append("f")

			result = ""
			for i in M1:
				result += str(i)
			

		lkey = convert(key)
		lbase = convert(compressed)
		ladded = addnum(lkey, lbase)
		ladded = reconvert(ladded)

		return result

	def cutter(string, leng):# coupe une partie de la chaine
		result = ""
		a = 0
		for i in range(len(string)):
			result += string[i]
			a += 1
			if a == leng:
				break
			else:
				pass
		return result

	def keyhexa():# génération d'une chaine hexadécimale aléatoire de 32 caractères
		l = []
		lf = []
		letters = ["a", "b", "c", "d", "e", "f"]
		for i in range(128):
			a = random.randint(0, 15)
			l.append(a)
		for i in l:
			if i == 0:
				lf.append("0")
			elif i == 1:
				lf.append("1")
			elif i == 2:
				lf.append("2")
			elif i == 3:
				lf.append("3")
			elif i == 4:
				lf.append("4")
			elif i == 5:
				lf.append("5")
			elif i == 6:
				lf.append("6")
			elif i == 7:
				lf.append("7")
			elif i == 8:
				lf.append("8")
			elif i == 9:
				lf.append("9")
			elif i == 10:
				lf.append("a")
			elif i == 11:
				lf.append("b")
			elif i == 12:
				lf.append("c")
			elif i == 13:
				lf.append("d")
			elif i == 14:
				lf.append("e")
			else:
				lf.append("f")
		a = ""
		for i in lf:
			a += i
		print(a)
		return a 

	
	mdp = password

	brut = binary(mdp)
	if len(brut) < 1024:
		brut = compress(brut, mdp, 1024)
	else:
		pass
	brut = convhexa(brut)
	cutted_brut = []

	if len(brut)%32 == 0:
		a = int(len(brut)/32)
	else:
		while len(brut)%32 != 0:
			brut = brut[:-1]
			if len(brut)%32 == 0:
				a = int(len(brut)/32)
				break 
			else:
				pass

	for i in range(a):
		cutted_brut.append(cutter(brut, 32))
		brut = brut[32:]

	cutted_brut[0] = crypt(cutted_brut[0], key)

	for i in range(1, len(cutted_brut)):
		cutted_brut[i] = crypt(cutted_brut[i], cutted_brut[i-1])
		endp = cutted_brut[i]

	return endp


