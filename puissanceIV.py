#!/usr/bin/python3

from random import randint

"""
1-A ['-','-','-','-','-','-']
2-Z ['-','-','-','-','-','-']
3-E ['-','-','-','-','-','-']
4-R ['-','-','-','-','-','-']
5-T ['-','-','-','-','-','-']
6-Y ['-','-','-','-','-','-']
7-U ['-','-','-','-','-','-']
"""

##########################################################################

liste_coup = [['A','Z','E','R','T','Y','U'],['1','2','3','4','5','6','7']]
nb_col = 7
nb_lig = 6
marquage_joueur = ['R','J']

##########################################################################

def puissanceIV () : #init
    joueur = randint(0,1)
    jouer = True
    while jouer :
        joueur = (joueur+1)%2
        plateau = [0] * nb_col
        for i in range(nb_col) :
            plateau[i] = ['-'] * nb_lig
        fini = False
        affiche_avec_tableau(plateau)
        while not(fini) :
            affiche_tour(joueur)
            num_col_coup = choix_coup()
            while colonne_pleine(plateau,num_col_coup) :
                print("La colonne sélectionnée est pleine")
                num_col_coup = choix_coup()
            num_lig_coup = position_ligne(plateau,num_col_coup)
            update(joueur,plateau,num_col_coup,num_lig_coup)
            fini = terminal(joueur,plateau)
            affiche_avec_tableau(plateau)
            joueur = (joueur + 1) % 2


        np = input("Voulez faire une nouvelle partie ? ('Oui' ou 'oui' pour accepter) : ")
        if np == 'oui' or np == 'Oui' :
            jouer = True
        else :
            jouer = False

##########################################################################

def affiche_tour(joueur) :
    print("C'est au tour du joueur",end=' ')
    if joueur == 0 :
        print('rouge (R)')
    else :
        print('jaune (J)')

##########################################################################


def affiche_ligne(plateau,num_lig) :
    for i in range(nb_col) :
        print('+---',end='')
    print('+')
    for j in range(nb_col) :
        print('|',plateau[j][nb_lig-1-num_lig],end=' ')
    print('|')

##########################################################################

def affiche_sans_tableau (plateau) :
    for i in range(len(plateau[0])-1,-1,-1) :
        for j in range(len(plateau)) :
            print(plateau[j][i],end='   ')
        print()
    print()
    for i in range(len(liste_coup)) :
        for j in range(len(liste_coup[0])) :
            print(liste_coup[i][j],end='   ')
        print()

##########################################################################

def affiche_avec_tableau(plateau) :
    for lig in range(nb_lig) :
        affiche_ligne(plateau,lig)
    for i in range(nb_col) :
        print('+---',end='')
    print('+')
    for i in range(len(liste_coup)) :
        print(end='  ')
        for j in range(len(liste_coup[0])) :
            print(liste_coup[i][j],end='   ')
        print()

##########################################################################

def choix_coup() :
    coup = input('Entrez votre coup : ')
    while coup != 'A' and coup != 'Z' and coup != 'E' and coup != 'R' and coup != 'T' and coup != 'Y' and coup != 'U' and coup != '1' and coup != '2' and coup != '3' and coup != '4' and coup != '5' and coup != '6' and coup != '7' :
        print('Choix invalide ! Il ne se trouve pas dans les coups possibles')
        coup = input('Entrez votre nouveau coup : ')
    indice = 0
    while liste_coup[0][indice] != coup and liste_coup[1][indice] != coup :
        indice = indice + 1
    return indice

##########################################################################

def colonne_pleine(plateau,num_col) :
    return plateau[num_col][nb_lig-1] != '-'

##########################################################################

def position_ligne(plateau,num_col) :
    indice = 0
    while plateau[num_col][indice] != '-' :
        indice = indice + 1
    return indice

##########################################################################

def update(joueur,plateau,num_col_coup,num_lig_coup) :
    plateau[num_col_coup][num_lig_coup] = marquage_joueur[joueur]

##########################################################################

def estPleine(plateau) :
    plein = True
    col = 0
    while plein and col < nb_col :
        if plateau[col][nb_lig-1] == '-' :
            plein = False
        col = col + 1
    return plein

##########################################################################

"""
def ligne4(plateau) :
    for col in range(nb_col) :
        for lig in range(nb_lig-4) :
            if plateau[col][lig] != '-' :
                indice = 1
                gagne = True
                while gagne and indice <= 3 :
                    if plateau[col][lig] != plateau[col][lig+indice] :
                        gagne = False
                    indice = indice + 1
                if gagne :
                    return True
    return False

"""
def ligne4(plateau,joueur) :
    col = 0
    l4 = 0
    lig = 0
    while col < nb_col and l4 < 4 :
        if plateau[col][lig] == marquage_joueur[joueur] :
            l4 = l4 + 1
        else :
            l4 = 0
        lig = lig + 1
        if lig == nb_lig :
            col = col + 1
            lig = 0
            if l4 < 4 :
                l4 = 0
    return l4 == 4


##########################################################################
"""

def colonne4(plateau) :
    for lig in range(nb_lig) :
        for col in range(nb_col-4) :
            if plateau[col][lig] != '-' :
                indice = 1
                gagne = True
                while gagne and indice <= 3 :
                    if plateau[col][lig] != plateau[col+indice][lig] :
                        gagne = False
                    indice = indice + 1
                if gagne :
                    return True
    return False

"""
def colonne4(plateau,joueur) :
    col = 0
    c4 = 0
    lig = 0
    while lig < nb_lig and c4 < 4 :
        if plateau[col][lig] == marquage_joueur[joueur] :
            c4 = c4 + 1
        else :
            c4 = 0
        col = col + 1
        if col == nb_col :
            lig = lig + 1
            col = 0
            if c4 < 4 :
                c4 = 0
    return c4 == 4


##########################################################################

"""
def diagonale4(plateau) :
    for col in range(nb_col-4) :
        for lig in range(nb_lig-4) :
            if plateau[col][lig] != '-' :
                indice = 0
                gagne = True
                while gagne and indice <= 3 :
                    if plateau[col][lig] != plateau[col+indice][lig+indice] :
                        gagne = False
                    indice = indice + 1
                if gagne :
                    return True
    for col in range(4,nb_col) :
        for lig in range(nb_lig-4) :
            if plateau[col][lig] != '-' :
                indice = 0
                gagne = True
                while gagne and indice <= 3 :
                    if plateau[col][lig] != plateau[col-indice][lig+indice] :
                        gagne = False
                    indice = indice + 1
                if gagne :
                    return True
    return False

"""

def diagonale4(plateau,joueur) :
    d4 = 0
    col_dep = 0
    lig_dep = 2
    col = col_dep
    lig = lig_dep
    while (col_dep < nb_col - 4 or lig_dep < nb_lig - 1) and d4 < 4 :
        if plateau[col][lig] == marquage_joueur[joueur] :
            d4 = d4 + 1
        else :
            d4 = 0
        lig = lig - 1
        col = col + 1
        if col >= nb_col or lig < 0 :
            if lig_dep < nb_lig - 1 :
                lig_dep = lig_dep + 1
            else :
                col_dep = col_dep + 1
            col = col_dep
            lig = lig_dep
            if d4 < 4 :
                d4 = 0
    col_dep = nb_col - 1
    lig_dep = nb_lig - 4
    col = col_dep
    lig = lig_dep
    while (col_dep > 3 or lig_dep < nb_lig - 1) and d4 < 4 :
        if plateau[col][lig] == marquage_joueur[joueur] :
            d4 = d4 + 1
        else :
            d4 = 0
        lig = lig - 1
        col = col - 1
        if col < 0 or lig < 0 :
            if lig_dep < nb_lig - 1 :
                lig_dep = lig_dep + 1
            else :
                col_dep = col_dep - 1
            col = col_dep
            lig = lig_dep
            if d4 < 4 :
                d4 = 0
    return d4 == 4


##########################################################################

def gagne(joueur,plateau) :
    print('Le joueur',end=' ')
    if joueur == 0 :
        print('rouge',end=' ')
    else :
        print('jaune',end=' ')
    print('a gagné !')

##########################################################################

def terminal(joueur,plateau) :
    if ligne4(plateau,joueur) or colonne4(plateau,joueur) or diagonale4(plateau,joueur) :
        gagne(joueur,plateau)
        return True
    elif estPleine(plateau) :
        print("Le plateau est plein et personne n'a gagné !")
        return True
    else :
        return False

puissanceIV()