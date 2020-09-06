#coding: utf-8

import random
import time

replacements = {
	"a":("α","4", "a"),
	"b":("β", "b"),
	"c":("c","ς"),
	"d":("d"),
	"e":("3", "ε","ξ", "e"),
	"f":("f", "ƒ"),
	"g":("g"),
	"h":("h"),
	"i":("1", "ι", "i"),
	"j":("j"),
	"k":("k", "κ"),
	"l":("|", "l"),
	"m":("m"),
	"n":("n","η"),
	"o":("0", "σ", "o"),
	"p":("p", "ρ"),
	"q":("q"),
	"r":("r"),
	"s":("s", "∫"),
	"t":("t", "τ"),
	"u":("u", "υ", "μ"),
	"v":("v"),
	"w":("w"),
	"x":("x", "χ"),
	"y":("y", "γ"),
	"z":("z") }


def change(name):
	global replacements
	namefin = ""
	for i in name:
		if i in replacements:
			namefin += replacements[i][random.randint(0, (len(replacements[i])-1))]
		else:
			namefin += i
	print(namefin)
	return namefin

def split_name(name):
	namel = []
	for i in name:
		namel.append(i)

	return namel

def main():
	name = str(input("put your name here >> "))
	print("")
	num = int(input("number of generated names >> "))
	print("")

	namel = split_name(name)

	for i in range(num):
		change(namel)
		time.sleep(0.01)


if __name__ == "__main__":
	main()