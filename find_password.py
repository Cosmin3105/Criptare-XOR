import itertools
import random

with open("Odin\input.txt", 'r') as f:
	text = f.read()

caractere = []
sir_enc = []

with open("Odin\output", 'rb') as f:
	i = 0
	while True:
		b = f.read(1)
		if not b:
			break
		c = int.from_bytes(b, byteorder='big')
		decr_p = c ^ ord(text[i])

		if decr_p not in caractere:
			caractere.append(decr_p)
		i += 1

		sir_enc.append(decr_p)
		
ls_caractere = "".join(chr(x) for x in caractere)

lg_max = 15

def find():
	for lg in range(len(caractere) + 1, lg_max + 1):
		to_add = lg - len(caractere)
		ar = [caractere] * to_add

		for prod in itertools.product(*ar):
			parola = [-1] * lg
			added_to_seed = sum(prod)
			
			random.seed(sum(caractere) + added_to_seed)
			
			good = True
			for x in sir_enc:
				r = random.randint(0, lg - 1)
				if parola[r] == -1:
					parola[r] = x
				elif parola[r] != x:
					good = False
			
			if good: 
				return parola

print("".join(chr(x) for x in find()))
