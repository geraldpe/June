#coding:utf-8

import random
import time
import subprocess
from colorama import init, Fore
from JUNE import June
from Sha_g import sha_g
import textstyle

init()

rep = "/"

recurq = ["hello", "helo", "hi", "hey", "Hello", "Helo", "Hi", "Hey"] #variables de mots récurants
recura = ["hello", "hi", "hey"]
hel = 0 #permet de ne pas repeter hello 2 fois
sent = []

june = June() #creation d'une instance de June
june.init_memory()

b, rep1 = 0, ""


#affichage des commandes et description de celles ci
def _help(rep1):
	if rep1 == "--help":
		print("")
		print("  --quitloop    : used to quit the loop you're in                                       ")
		print("  --quit        : used to end the program                                               ")
		print("  --help        : the command you used to come here, shows you every command            ")
		print("  --calc        : open the calculator, you must be in the apps section                  ")
		print("  --matrix      : to open the matrix,  you must be in the apps section                  ")
		print("  --wordlist    : run the Wordlist program, must be used in the hacking section         ")
		print("  --namegreak   : generate possible surnames for instagram, must be used in apps        ")
		print("")
		print("  -a            : access to the application device                                      ")
		print("  -s            : access to the simulation device                                       ")
		print("  -c            : access to the conversation                                            ")
		print("  -g            : access to the game library                                            ")
		print("  -h            : access to the hacking device                                          ")


def command(rep1):

	if rep1 == "-a --matrix":
			subprocess.call([r'..\\batchuse\\matrix.bat'])
			print("")
	elif rep1 == "-a --calc":
		subprocess.call([r'..\\batchuse\\calculatrice.bat'])
		print("")
	elif rep1 =="-a --namegreak":
		textstyle.main()


	elif rep1[:1] == "-s":
		pass
	elif rep1[:1] == "-c":
		pass
	elif rep1[:1] == "-g":
		pass


	elif rep1 == "-h --wordlist":
		subprocess.call([r'wordlistcore.bat'])
		print("")

	else:
		pass


def affichage():
	print("")
	print("") 
	print("                                                                                                                 ")
	print(Fore.RED       + "                  _________________________________________                                     ")
	print(                 "                 (____   ________________________   _______)                                    ")
	print(                 "                      | |     _   _   ___   _    | |____                                        ")
	print(                 "                 _    | |    | | | | |   \ | |   |  ____)                                       ")
	print(                 "                ( \___/ /    | |_| | | |\ \| |   | |_______                                     ")
	print(                 "                 \_____/     \_____/ |_| \___|   |_________)                                    ")
	print(                 "                                                                                                ")
	print("")
	print("")
	print(Fore.RED + "                  type something to begin the conversation                                            ")
	print(Fore.WHITE, "                                                                                                     ")
	time.sleep(0.1)
	print(" application device     : a                   games                  : g                        ")
	time.sleep(0.1)
	print(" simulation devices     : s                   hacking devices        : h                        ") 
	time.sleep(0.1)
	print(" conversation with June : c                   settings               : p                        ")
	time.sleep(0.1)
	print("") 
	print("")


f = open("../memoryy/debmess.txt", "r")  #acces à la mémoire pour voir si le message de début a déjà été dit ou non
init = f.read()
f.close()
if init == "0":
	print("")
	print("Hi, my name's June, I'm an AI and I'd really like to learn with you")
	print("")
	print("I was created to discuss with humans and to improve myself creating my own personnality ")
	f = open("../memoryy/debmess.txt", "w")
	f.write("1")
	f.close()

	print("")
	print("--------------------------------------begin----------------------------------------     ")
	print("")
else:
	pass



def main(): # main part of the program
	global rep1, b, hel

	affichage() #affichage du titre

	password = open('../memoryy/password/password.txt', "r")
	passr = password.read()
	password.close()
	endp = ""
	if passr != "":
		tryp = 1
		while endp != passr:
			rep = input("enter your password here >> ")
			endp = sha_g(rep)
			if endp == passr:
				running = True
				break
			elif tryp == 3:
				running = False
				break
			else:
				print("wrong password, try again")
				tryp += 1
	else:
		running = True

	while running: #boucle principale
		
		if rep1 == "--quitloop" and b == 1:
			print("                                                                                        ")
			print(" application device     : a                   games                  : g                ")
			print(" simulation devices     : s                   hacking devices        : h                ") 
			print(" conversation with June : c                   settings               : p                ")
			print("                                                                                        ") 
			print("                                                                                        ")
			b = 0
			rep1 = ""
		else:
			pass

		print(Fore.RED)
		rep1 = str(input(">> "))
		print(Fore.WHITE)

		command(rep1)

		if rep1 == "--help":
			_help(rep1)
		elif rep1 == "c": #convsersation avec June
			print("")
			print("                               conversation                           ")
			print("")
			print(Fore.RED)
			rep1 = str(input("c >> "))
			print(Fore.WHITE)
			while rep1 != "--quitloop":
				#débuts de conversation, conversations pre-enregistrées
				if june.memory.get(rep1, 0) == 0:
					if rep1 == "--help":
						_help(rep1)
						print(Fore.RED)
						rep1 = str(input(">> "))
						print(Fore.WHITE)
					elif rep1 == "--quitloop":
						b = 1
						break
					elif rep1 == "--quit":
						running = False
						break
					elif rep1[:1] == "--":
						print("")
						print("wrong command, try again or type --help")

					command(rep1)

					for i in range(len(recurq)):      #reconnaissance des différentes occurances de hello, hi et hey
						if hel == 1 and rep1[:len(recurq[i])] == recurq[i]:  #verifie si une occurance de hello a déjà été dite
							print("We've already said hello, haven't we?")
							hel += 1
							if rep1[:3] == "yes":
								print("Well, what's the point, then?")
								break
							else:
								break

						#ces deux bloques permettent de donner un peu plus de personnalité à June
						elif hel == 2 and rep1[:len(recurq[i])] == recurq[i]:
							print("Why do you insist?")
							hel += 1
							break
						elif hel == 3 and rep1[:len(recurq[i])] == recurq[i]:
							print("well, it's to much, I'm out")
							time.sleep(0.5)
							running = False
							rep1 = "--quitloop"
							break


						elif rep1[:len(recurq[i])] == recurq[i]:
							b = random.randint(0, 2)  #choix aléatoire d'une reponse possible pour un hello
							print(recura[b])
							hel = 1
							break
						else:
							pass
					else:
						print("")
						june.append_d(rep1)
				else:
					for k in range(len(sent)):
						if sent[k] == i:
							if hel == 0:
								print("you already said that, didn't you ?")
								print("")
								hel += 1
								break
							elif hel == 1:
								print("why do you insist with that ?")
								print("")
								hel += 1
								break
							else:
								print("good bye parrot")
								time.sleep(0.5)
								print("")
								running, rep1 = False, "--quitloop"
								break
					print("")
					print(june.memory[rep1])
					sent.append(rep1)

				print(Fore.RED)
				rep1 = str(input("c >> ")) #conversation
				print(Fore.WHITE)
		elif rep1 == "a": #applications
			print("")
			print("                               applications                           ")
			print("")
			while rep1 != "quitloop":
				if rep1 == "--help":
					_help(rep1)
				elif rep1 == "--matrix":
					subprocess.call([r'..\\batchuse\\matrix.bat'])
					print("")
				elif rep1 == "--calc":
					subprocess.call([r'..\\batchuse\\calculatrice.bat'])
					print("")
				elif rep1 == "--namegreak":
					textstyle.main
				elif rep1 == "--quit":
					running = False
					break
				elif rep1 == "--quitloop":
					b = 1
					break
				elif rep1 == "a":
					pass
				else:
					print("wrong command, try again or type --help")

				print(Fore.RED)
				rep1 = str(input("a >> "))
				print(Fore.WHITE)
		elif rep1 == "s":
			pass
		elif rep1 == "g":
			pass
		elif rep1 == "h": #outils de hacking
			print("")
			print("                               hacking                           ")
			print("")
			while rep1 != "--quitloop":
				if rep1 == "--help":
					_help(rep1)
				elif rep1 == "--quit":
					running = False
					break
				elif rep1 == "--quitloop":
					b = 1
					break
				elif rep1 == "--help":
					_help()
				elif rep1 == "--wordlist":
					subprocess.call([r'wordlistcore.bat'])
					print("")
				elif rep1 == "h":
					pass
				else:
					print("wrong command, try again or type --help")
				print(Fore.RED)
				rep1 = str(input("h >> ")) 
				print(Fore.WHITE)
		elif rep1 == "p": #paramètres
			print("")
			print("                             settings                             ")
			print("")
			print("          security : e                      statistics : s         ")
			print("")
			while rep1 != "--quitloop":
				if rep1 == "--help":
					_help(rep1)
				elif rep1 == "--quit":
					running = False
					break
				elif rep1 == "--quitloop":
					b = 1
					break
				elif rep1 == "e":
					endp == "1"
					passw = input("do you want to create a new password ? (y/n) >>")
					if passw == "y":
						password = open('../memoryy/password/password.txt', "r")
						passr = password.read()
						password.close()
						if passr != "":
							tryp = 1
							while endp != passr:
								rep = input("what was your previous password ? >> ")
								endp = sha_g(rep)
								if endp == passr:
									password = open('../memoryy/password/password.txt', "w")
									newpass = sha_g(str(input("enter your password here >> ")))
									password.write(newpass)
								elif tryp == 3:
									rep1 = "--quitloop"
									running = False
									break
								else:
									print("wrong password, try again or type --help")
									tryp += 1
						else:
							password = open('../memoryy/password/password.txt', "w")
							newpass = sha_g(str(input("enter your new password here >> ")))
							password.write(newpass)
				elif rep1 == "p":
					pass
				else:
					print("wrong command, try again or type --help")
				print(Fore.RED)
				rep1 = str(input("p >> "))
				print(Fore.WHITE)
		elif rep1 == "--quit":
			running = False
			break
		else:
			print("wrong command, try again or type --help")


if __name__ == "__main__":
	main()
