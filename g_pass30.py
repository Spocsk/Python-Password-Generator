import random
from tkinter import *

a='ABCDEFGHIJKMNLOPQRSTUVWXYZ'
b='abcefghijkmnlopqrstuvwxyz'
d='0123456789'
s='&~#{[|`^@]^$ù*;:!,?./§%µ£+°@^'


liste = []

print(''' 
  ▄████  ██▓███   ▄▄▄        ██████   ██████ 
 ██▒ ▀█▒▓██░  ██▒▒████▄    ▒██    ▒ ▒██    ▒ 
▒██░▄▄▄░▓██░ ██▓▒▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄   
░▓█  ██▓▒██▄█▓▒ ▒░██▄▄▄▄██   ▒   ██▒  ▒   ██▒
░▒▓███▀▒▒██▒ ░  ░ ▓█   ▓██▒▒██████▒▒▒██████▒▒
 ░▒   ▒ ▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░
  ░   ░ ░▒ ░       ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░
░ ░   ░ ░░         ░   ▒   ░  ░  ░  ░  ░  ░  
      ░                ░  ░      ░        ░  
                                             
                    ~3.0~
	''')

def aleatoire():
    nb = int(input('Choisissez le nombre de caractère :> '))

    mot =''

    for c in range(0,nb):
                
        x = random.randint(0, len(liste))
        if x == len(liste):
            x -= 1

        y = random.randint(0, len(liste[x]))
        if y == len(liste[x]):
            y -= 1

        mot = mot + liste[x][y]

    print('''
    ###########################
    #                         #
    # MDP : {0}               #
    #                         #
    ###########################
    
    '''.format(mot))

while True:

    ans_usr = input('''Choisir options:
    a) Maj. 
    b) Min. 
    c) Chif.
    d) Spec. 
    e) Lancer le proc. 
    f) Quit. :> 
    g) Retirer de la liste :> ''')

    if ans_usr == 'a':
        liste.append(a)
    if ans_usr == 'b':
        liste.append(b)
    if ans_usr == 'c':
        liste.append(d)
    if ans_usr == 'd':
        liste.append(s)
    if ans_usr == 'e':
        aleatoire()
    if ans_usr == 'f':
        break
    if ans_usr == 'g':
        while True:
            abc = input('''Sélectionner :> 
            a) Maj. 
            b) Min. 
            c) Chif.
            d) Spec.
            e) Sortir. :>
            ''')
            if abc == 'a':
                liste.remove()

