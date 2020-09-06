#coding:utf-8

#--------------------------------------------initialisation----------------------------------------------------------------

#affichage titre
print("")
print("                               wordlist by ExypnoseinT2NaH                               ")
print("")
print("")
print("                                                                                         ")
print("           _____________________________________________________________________         ")
print("          (_ _ ____________ _ _ ___ _ ____ _ ___ ___ _ _ _ __ ______ ___  ______)        ")
print("            | |      __    | |/ ___ \|  __ \|  _ \  | |  \ \ /  _____) / /               ")
print("             \ \    /  \  / /| /   \ | (__) | | \ | | |   \ |  (___   | |                ")
print("              \ \  / /\ \/ / | |   | | _  _/| | | | | |    \ \____ \  | |                ")
print("               \ \/ /  \__/  | \___/ | |\ \ | |_/ | | |____ \ \   | | | |                ")
print("           _____\__/__________\_____/|_|_\ \|____/__\______)_\_\__/ | | \_               ")
print("          (________________________________________________________/  \___)              ")
print("                                                                                         ")
print("")
print("")


#création de la liste de mots clés
words = []
words.append(str(input("First name of your victim >> ")))
while words[0] == "":
	print("Enter at least a name !!")
	words[0] = str(input(">> "))
words.append(str(input("Name of your victim >> ")))
words.append(str(input("victim's city >> ")))
words.append(str(input("postal code >> ")))
rep = str(input("do your victim has children ? (y/n) >> "))
if rep == "y":
	nmbc = int(input("How many children ? >> "))
	for i in range(nmbc):
		words.append(str(input("name of the", i, "child >> ")))
		words.append(str(input("birthday of the", i, "child >> ")))
else:
	pass
rep = str(input("is there some other informations ? (y/n) >> "))
while rep == "y":
	words.append(str(input("complementary information >> ")))
	rep = str(input("is there some other informations ? (y/n) >> "))

print("")
print(words)
print("")

#initialisation des variables
words_ = []
words_1 = []
empe, empa, empi, empo = "/", "/", "/", "/"
nmbmdp = 0
birth = "0"

#nombres aléatoire ?
print("turn on random numbers --------- : 1            turn off  : 0")
nmbal = int(input(">> "))
if nmbal == 1:
	print("take just a half of theme : 1            take all of theme : 0")
	half = int(input(">> "))

#---------------------------------------------fonctions--------------------------------------------------------------------

#initialisation de la date de naissance
def get_birthday():
	global words, birth

	print("birth day : ")
	rep = str(input(">> "))
	while len(rep) > 2:
		print("the birth day lengh must be between 1 and 2 !!")
		rep = input(">> ")
	if int(rep) <= 9:
		birth += rep
	else:
		birth = str(rep)

	#mois de naissance
	print("")
	print("                             birth month        ")
	print("")
	print("             january  = 1                  july      = 7 ")
	print("             february = 2                  august    = 8 ")
	print("             march    = 3                  september = 9 ")
	print("             april    = 4                  october   = 10")
	print("             may      = 5                  november  = 11")
	print("             june     = 6                  december  = 12")

	rep = int(input(">> "))
	while rep > 12 or rep < 1:
		print("the month must be between 1 and 12 !!")
		rep = int(input(">> ")) 

	if rep == 1:                          #ajout du mois à la liste de mots
		words.append("january")
	elif rep == 2:
		words.append("february")
	elif rep == 3:
		words.append("march")
	elif rep == 4:
		words.append("april")
	elif rep == 5:
		words.append("may")
	elif rep == 6:
		words.append("june")
	elif rep == 7:
		words.append("july")
	elif rep == 8:
		words.append("august")
	elif rep == 9:
		words.append("september")
	elif rep == 10:
		words.append("october")
	elif rep == 11:
		words.append("november")
	else:
		words.append("december")

	if int(rep) <= 9:
		birth += ("0" + str(rep))
	else:
		birth += rep

	#annee de naissance
	print("year of birth (yyyy) : ")
	rep = str(input(">> "))
	while len(rep) != 4:
		print("the year lengh must be 4 !!")
		rep = str(input(">> "))
	birth += rep

#repérage de l'emplacement des lettres remplaçables
def letter_replace(liste):
	global words_, empa, empe, empi, empo

	for i in range(len(liste)):
		for k in range(len(liste[i])):
			if liste[i][k] == "e":
				empe = k
			elif liste[i][k] == "a":
				empa = k
			elif liste[i][k] == "i":
				empi = k
			elif liste[i][k] == "o":
				empo = k

		if empe != "/":   #changement des e en 3
			repl = liste[i][0:empe] + "3" + liste[i][empe+1:len(liste[i])]  
			words_.append(repl)
		else:
			pass
		if empa != "/": #changement des a en 4
			repl = liste[i][0:empa] + "4" + liste[i][empa+1:len(liste[i])]
			words_.append(repl)

			#changement des a en @
			repl = liste[i][0:empa] + "@" + liste[i][empa+1:len(liste[i])]
			words_.append(repl)
		else:
			pass
		if empi != "/": #changement des i en 1
			repl = liste[i][0:empi] + "1" + liste[i][empi+1:len(liste[i])]
			words_.append(repl)
		else:
			pass
		if empo != "/": #changement des o 0
			repl = liste[i][0:empo] + "0" + liste[i][empo+1:len(liste[i])]
			words_.append(repl)
		else:
			pass

		#réinitialisation des variables d'emplacement 
		empe, empa, empi, empo = "/", "/", "/", "/"

#inversion de mots
def invert(liste):
	global words_

	reverse = []
	for i in range(len(liste)):
		l = []
		for k in range(len(liste[i])):
			l.append(liste[i][k])
		b = len(l) - 1
		word = ""
		for k in range(len(l)):
			word += l[b]
			b -=1
		reverse.append(word)
	words_ += reverse

#addition des mots modifiés pour créer de nouveaux mots de passe potentiels
def addw(liste):
	global words_1

	for i in range(len(liste)):
		for k in range(len(liste)):
			add = liste[i] + liste[k]
			if add == liste[i] + liste[i]:
				pass
			else:
				words_1.append(add)

#ajout d'appendices répandus à la fin des mots de passe
def appendi(liste):
	for i in range(len(liste)):
		liste.append(liste[i] + "123")
		liste.append(liste[i] + "abc")
		liste.append(liste[i] + "Abc")
		liste.append("123" + liste[i])
		liste.append("abc" + liste[i])
		liste.append("Abc" + liste[i])

#generateur de suites de nombres aléatoires
def nmbalea(liste):
	nmb = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
	nmbl = []
	nmbl1 = []
	global half

	for i in range(len(nmb)):
		for k in range(len(nmb)):
			nmb_ = nmb[i] + nmb[k]
			nmbl.append(nmb_)
	for i in range(len(nmb)):
		for k in range(len(nmb)):
			for j in range(len(nmb)):
				nmb_ = nmb[i] + nmb[k] + nmb[j]
				nmbl.append(nmb_)

	#pour diviser par deux le nombre de nmbs alé
	if half == 1:
		for i in range(round(len(nmbl)/2)):
			nmbl1.append(nmbl[i])
	else:
		nmbl1 = nmbl

	#ajout des suites de nombres aux mdps générés
	for i in range(len(liste)):
		for k in range(len(nmbl1)):
			liste.append(liste[i] + nmbl1[k]) 
		for k in range(len(nmbl1)):
			liste.append(nmbl1[k] + liste[k])

	
#-------------------------------------------programme----------------------------------------------------------------------

get_birthday()
letter_replace(words) 
invert(words)
words_ += words

#coupage de mots
for i in range(len(words)):
	if len(words[i]) >= 6:
		if len(words[i]) % 2 == 0:
			a = len(words[i]) / 2
			word = words[i][:(int(a) + 1)]
		else:
			a = round(len(words[i]) / 2)
			word = words[i][:(int(a) + 1)]
		words_.append(word)
	else:
		pass

addw(words_)
appendi(words_1)

if nmbal == 1:
	nmbalea(words_1)
else:
	pass

#ajout de la date au début et à la fin des mdps
ddmmyyyy = birth
ddmmyy = birth[:4] + birth[6:]

date1 = ddmmyy
date2 = ddmmyyyy
words_2 = [date1, date2]

for i in range(len(words_1)):
	words_1.append(words_1[i] + date1)
	words_1.append(words_1[i] + date2)
	words_1.append(date1 + words_1[i])
	words_1.append(date2 + words_1[i])
words_2 += words_1
words_2 += words
words_2.append(ddmmyy[:4])
words_2.append(ddmmyy[2:4] + ddmmyy[:2])

#information dans la console sur le nombre de mots de passe générés
print("")
print("generated passwords :"+ str(len(words_2)))

password = open("passwords.txt", "a")
for i in words_2:
	password.write("\n" + str(i))
password.close()

