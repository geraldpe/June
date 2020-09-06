#coding:utf-8


class June:

	def __init__(self):
		#mise en place de la mémoire émotionelle
		mo = open('../memoryy/setupcurrentstate/mood.txt', "r") 
		self.mood = int(mo.read()) #le mood définira la manière que je June va avoir de répondre 
		mo.close()
		fli = open('../memoryy/setupcurrentstate/flirty.txt', "r")
		flir = fli.read()
		if flir == "False": #la variable flirty permettra de savoir si June a envie de flirter avec son interlocuteur
			self.flirty = False
		else:
			self.flirty = True
		fli.close()

		an = open('../memoryy/setupcurrentstate/angry.txt', "r")
		ang = an.read()
		if ang == "False": #la variable angry permet de savoir si June est énervée contre son interlocuteur
			self.angry = False
		else:
			self.angry = True
		an.close()
		sym = open('../memoryy/setupcurrentstate/sympathy.txt', "r")
		self.sympathy = int(sym.read()) #permet de savoir si June est amicale envers son interlocuteur
		sym.close()
		self.memory = {} #création de la mémoire

	#initialisation de la mémoire
	def init_memory(self):
		self.memory = {}
		sentences = open("../memoryy/sentences.txt", "r")
		sentl = sentences.read().splitlines()
		answers = open("../memoryy/responses.txt", "r")
		answl = answers.read().splitlines()

		for i in range(len(sentl)):
			self.memory[sentl[i]] = answl[i]

		sentences.close()
		answers.close()

	#append_d() permet d'ajouter des éléments dans la mémoire de June
	def append_d(self, rep1):

		print("I can't answer to that for now")
		print("teach me :)")
		print("")
		rep2 = str(input("what should I've answer ?  >> "))
		self.memory[rep1] = rep2
		sentences = open("../memoryy/sentences.txt", "a")
		sentences.write("\n" + str(rep1))
		sentences.close()

		answers = open("../memoryy/responses.txt", "a")
		answers.write("\n" + str(rep2))
		sentences.close()
		

if __name__ == "__main__":

	june = June()
	print(june.mood)
	print(june.flirty)
	print(june.angry)
	print(june.sympathy)
