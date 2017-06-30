# -*- coding: utf-8 -*-
import string
import argparse
from os import system, name

system('cls') if name == 'nt' else system('clear')

print """\033[32m
   _   _   _   _   _   _     _   _   _   _   _   _  
  / \ / \ / \ / \ / \ / \   / \ / \ / \ / \ / \ / \ 
 ( S | w | i | t | c | h ) ( C | i | p | h | e | r )
  \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/ 
                                           By Lord13
                                                v1.0
####################################################\033[0;0m
"""

def encriptar(word, key):
	letters = list(string.ascii_lowercase)
	a = 1

	for i in key.lower():
		letters.remove(i)
		if a == 1:
			letters.insert(0, i)
			a = 2
		else:
			letters.append(i)
			a = 1
		lista = []
	
	for i in word:
		if not i.isalpha(): lista.append(i);continue
		lista.append(letters[string.ascii_lowercase.index(i.lower())]) if i.islower() else lista.append(letters[string.ascii_lowercase.index(i.lower())].upper())

	return ''.join(lista)

def decriptar(word, key):
	letters = list(string.ascii_lowercase)

	a = 1

	for i in key.lower():
		letters.remove(i)
		if a == 1:
			letters.insert(0, i)
			a = 2
		else:
			letters.append(i)
			a = 1
		lista = []
	
	for i in word:
		if not i.isalpha(): lista.append(i);continue
		lista.append(string.ascii_lowercase[letters.index(i.lower())]) if i.islower() else lista.append(string.ascii_lowercase[letters.index(i.lower())].upper())

	return ''.join(lista)


def arg_parse_analysis():
    argparse2 = argparse.ArgumentParser(
        description="""Criptografa ou descriptografa uma string. \033[47m\033[31m\033[1mOBS.\033[0;0m: Espacos, numeros e caracteres especiais nao sao (des)criptografados."""
        )
    argparse2.add_argument('-e', '--encrypt', action="store_true", help="criptografa uma string", dest="encrypt_or_decrypt")
    argparse2.add_argument('-d', '--decrypt', action="store_false", help="descriptografa uma string", dest="encrypt_or_decrypt")
    argparse2.add_argument('-w', '--word', action="store", dest="word", help='string a ser (des)criptografada', required=True)
    argparse2.add_argument('-k', '--key', action="store", dest="key", help='chave (DEVE ser usada para ambos os casos)', required=True)
    parser = argparse2.parse_args()
    word = parser.word
    decrypt_or_encrypt = parser.encrypt_or_decrypt
    key = parser.key
    return word, decrypt_or_encrypt, key

word, decrypt_or_encrypt, key = arg_parse_analysis()

if decrypt_or_encrypt is True:
	retorno = encriptar(word, key)
	print """\033[31m
    [*]{0}[*]
       Criptografado: {1}
    [*]{0}[*]
	\033[0;0m
	""".format('+'.center(len(retorno) + 20, '+'), retorno)
else:
    retorno = decriptar(word, key)
    print """\033[33m
    [*]{0}[*]
       Descriptografado: {1}
    [*]{0}[*]
	\033[0;0m""".format('+'.center(len(retorno) + 20, '+'), retorno)