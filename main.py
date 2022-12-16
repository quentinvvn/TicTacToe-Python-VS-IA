import random


def creerGrille():
    return ['.' for i in range(3*3)]


def afficherRegles():
    print("--------------------------------------------------------------------------------")
    print("Deux joueurs posent tour à tour un rond, pour l’un, une croix, pour l’autre, dans une grille de 3 cases par 3.")
    print("Le but du jeu est d’obtenir un alignement (en ligne, colonne ou diagonale) de ses trois signes.")
    print("Contrairement à la marelle, les signes une fois posés ne sont plus déplacés.")
    print("--------------------------------------------------------------------------------")


def partie(m, difficulty):
    while (m[0] == '.' or m[1] == '.' or m[2] == '.' or m[3] == '.' or m[4] == '.' or m[5] == '.' or m[6] == '.' or m[7] == '.' or m[8] == '.'):
        if (m[0] == m[1] == m[2] == 'X' or (m[0] == m[1] == m[2] == 'O')):
            if (m[0] == 'X'):
                return True
            else:
                return False
        elif (m[3] == m[4] == m[5] == 'X' or (m[3] == m[4] == m[5] == 'O')):
            if (m[3] == 'X'):
                return True
            else:
                return False
        elif (m[6] == m[7] == m[8] == 'X' or (m[6] == m[7] == m[8] == 'O')):
            if (m[6] == 'X'):
                return True
            else:
                return False
        elif (m[0] == m[3] == m[6] == 'X' or (m[0] == m[3] == m[6] == 'O')):
            if (m[0] == 'X'):
                return True
            else:
                return False
        elif (m[1] == m[4] == m[7] == 'X' or (m[1] == m[4] == m[7] == 'O')):
            if (m[1] == 'X'):
                return True
            else:
                return False
        elif (m[2] == m[5] == m[8] == 'X' or (m[2] == m[5] == m[8] == 'O')):
            if (m[2] == 'X'):
                return True
            else:
                return False
        elif (m[0] == m[4] == m[8] == 'X' or (m[0] == m[4] == m[8] == 'O')):
            if (m[0] == 'X'):
                return True
            else:
                return False
        elif (m[6] == m[4] == m[2] == 'X' or (m[6] == m[4] == m[2] == 'O')):
            if (m[6] == 'X'):
                return True
            else:
                return False
        afficherGrille(m)
        tourJoueur(m)
        if (m[0] == '.' or m[1] == '.' or m[2] == '.' or m[3] == '.' or m[4] == '.' or m[5] == '.' or m[6] == '.' or m[7] == '.' or m[8] == '.'):
            if (difficulty == 2):
                tourOrdiIntel(m)
            elif (difficulty == 1):
                tourOrdi(m)
            else:
                tourOrdiVeryIntel(m)
    else:
        return None


def tourJoueur(m):
    Col = int(
        input("Veuillez entrer la colonne sur laquelle vous souhaitez jouer : "))
    Lign = int(input("Veuillez entrer la ligne où vous souhaitez jouer : "))
    Col -= 1
    Lign -= 1
    if (Col < 0 or Col > 2 or Lign < 0 or Lign > 2):
        print("Valeures incorrectes, la colonne et la ligne doivent être comprises entre 0 et 2")
        tourJoueur(m)
    elif (m[(3*Lign)+Col] == '.'):
        ecrireValeurGrille(m, Col, Lign, 'X')
    else:
        print("------------------------")
        print("L'espace est déjà occupé")
        print("------------------------")
        afficherGrille(m)
        tourJoueur(m)


def tourOrdi(m):
    Col = random.randint(0, 2)
    Lign = random.randint(0, 2)
    if (m[(3*Lign)+Col] == '.'):
        ecrireValeurGrille(m, Col, Lign, 'O')
    else:
        tourOrdi(m)


def tourOrdiIntel(m):
    if ((m[0] == m[1] == 'X' and m[2] == '.') or (m[1] == m[2] == 'X' and m[0] == '.') or (m[0] == m[2] == 'X' and m[1] == '.')):
        if (m[2] == '.'):
            ecrireValeurGrille(m, 2, 0, 'O')
        elif (m[1] == '.'):
            ecrireValeurGrille(m, 1, 0, 'O')
        else:
            ecrireValeurGrille(m, 0, 0, 'O')
    elif ((m[3] == m[4] == 'X' and m[5] == '.') or (m[5] == m[4] == 'X' and m[3] == '.') or (m[3] == m[5] == 'X' and m[4] == '.')):
        if (m[5] == '.'):
            ecrireValeurGrille(m, 2, 1, 'O')
        elif (m[4] == '.'):
            ecrireValeurGrille(m, 1, 1, 'O')
        else:
            ecrireValeurGrille(m, 0, 1, 'O')
    elif ((m[6] == m[7] == 'X' and m[8] == '.') or (m[7] == m[8] == 'X' and m[6] == '.') or (m[6] == m[8] == 'X' and m[7] == '.')):
        if (m[8] == '.'):
            ecrireValeurGrille(m, 2, 2, 'O')
        elif (m[7] == '.'):
            ecrireValeurGrille(m, 1, 2, 'O')
        else:
            ecrireValeurGrille(m, 0, 2, 'O')
    elif ((m[0] == m[3] == 'X' and m[6] == '.') or (m[3] == m[6] == 'X' and m[0] == '.') or (m[0] == m[6] == 'X' and m[3] == '.')):
        if (m[0] == '.'):
            ecrireValeurGrille(m, 0, 0, 'O')
        elif (m[3] == '.'):
            ecrireValeurGrille(m, 0, 1, 'O')
        else:
            ecrireValeurGrille(m, 0, 2, 'O')
    elif ((m[1] == m[4] == 'X' and m[7] == '.') or (m[4] == m[7] == 'X' and m[1] == '.') or (m[1] == m[7] == 'X' and m[4] == '.')):
        if (m[1] == '.'):
            ecrireValeurGrille(m, 1, 0, 'O')
        elif (m[4] == '.'):
            ecrireValeurGrille(m, 1, 1, 'O')
        else:
            ecrireValeurGrille(m, 1, 2, 'O')
    elif ((m[2] == m[5] == 'X' and m[7] == '.') or (m[5] == m[8] == 'X' and m[2] == '.') or (m[2] == m[8] == 'X' and m[5] == '.')):
        if (m[2] == '.'):
            ecrireValeurGrille(m, 2, 0, 'O')
        elif (m[5] == '.'):
            ecrireValeurGrille(m, 2, 1, 'O')
        else:
            ecrireValeurGrille(m, 2, 2, 'O')
    elif ((m[0] == m[4] == 'X' and m[8] == '.') or (m[4] == m[8] == 'X' and m[0] == '.') or (m[0] == m[8] == 'X' and m[4] == '.')):
        if (m[0] == '.'):
            ecrireValeurGrille(m, 0, 0, 'O')
        elif (m[4] == '.'):
            ecrireValeurGrille(m, 1, 1, 'O')
        else:
            ecrireValeurGrille(m, 2, 2, 'O')
    elif ((m[2] == m[4] == 'X' and m[6] == '.') or (m[4] == m[6] == 'X' and m[2] == '.') or (m[2] == m[6] == 'X' and m[4] == '.')):
        if (m[2] == '.'):
            ecrireValeurGrille(m, 2, 0, 'O')
        elif (m[4] == '.'):
            ecrireValeurGrille(m, 1, 1, 'O')
        else:
            ecrireValeurGrille(m, 0, 2, 'O')
    else:
        tourOrdi(m)


def tourOrdiVeryIntel(m):
    if ((m[0] == m[1] == 'O' and m[2] == '.') or (m[1] == m[2] == 'O' and m[0] == '.') or (m[0] == m[2] == 'O' and m[1] == '.')):
        if (m[2] == '.'):
            ecrireValeurGrille(m, 2, 0, 'O')
        elif (m[1] == '.'):
            ecrireValeurGrille(m, 1, 0, 'O')
        else:
            ecrireValeurGrille(m, 0, 0, 'O')
    elif ((m[3] == m[4] == 'O' and m[5] == '.') or (m[5] == m[4] == 'O' and m[3] == '.') or (m[3] == m[5] == 'O' and m[4] == '.')):
        if (m[5] == '.'):
            ecrireValeurGrille(m, 2, 1, 'O')
        elif (m[4] == '.'):
            ecrireValeurGrille(m, 1, 1, 'O')
        else:
            ecrireValeurGrille(m, 0, 1, 'O')
    elif ((m[6] == m[7] == 'O' and m[8] == '.') or (m[7] == m[8] == 'O' and m[6] == '.') or (m[6] == m[8] == 'O' and m[7] == '.')):
        if (m[8] == '.'):
            ecrireValeurGrille(m, 2, 2, 'O')
        elif (m[7] == '.'):
            ecrireValeurGrille(m, 1, 2, 'O')
        else:
            ecrireValeurGrille(m, 0, 2, 'O')
    elif ((m[0] == m[3] == 'O' and m[6] == '.') or (m[3] == m[6] == 'O' and m[0] == '.') or (m[0] == m[6] == 'O' and m[3] == '.')):
        if (m[0] == '.'):
            ecrireValeurGrille(m, 0, 0, 'O')
        elif (m[3] == '.'):
            ecrireValeurGrille(m, 0, 1, 'O')
        else:
            ecrireValeurGrille(m, 0, 2, 'O')
    elif ((m[1] == m[4] == 'O' and m[7] == '.') or (m[4] == m[7] == 'O' and m[1] == '.') or (m[1] == m[7] == 'O' and m[4] == '.')):
        if (m[1] == '.'):
            ecrireValeurGrille(m, 1, 0, 'O')
        elif (m[4] == '.'):
            ecrireValeurGrille(m, 1, 1, 'O')
        else:
            ecrireValeurGrille(m, 1, 2, 'O')
    elif ((m[2] == m[5] == 'O' and m[7] == '.') or (m[5] == m[8] == 'O' and m[2] == '.') or (m[2] == m[8] == 'O' and m[5] == '.')):
        if (m[2] == '.'):
            ecrireValeurGrille(m, 2, 0, 'O')
        elif (m[5] == '.'):
            ecrireValeurGrille(m, 2, 1, 'O')
        else:
            ecrireValeurGrille(m, 2, 2, 'O')
    elif ((m[0] == m[4] == 'O' and m[8] == '.') or (m[4] == m[8] == 'O' and m[0] == '.') or (m[0] == m[8] == 'O' and m[4] == '.')):
        if (m[0] == '.'):
            ecrireValeurGrille(m, 0, 0, 'O')
        elif (m[4] == '.'):
            ecrireValeurGrille(m, 1, 1, 'O')
        else:
            ecrireValeurGrille(m, 2, 2, 'O')
    elif ((m[2] == m[4] == 'O' and m[6] == '.') or (m[4] == m[6] == 'O' and m[2] == '.') or (m[2] == m[6] == 'O' and m[4] == '.')):
        if (m[2] == '.'):
            ecrireValeurGrille(m, 2, 0, 'O')
        elif (m[4] == '.'):
            ecrireValeurGrille(m, 1, 1, 'O')
        else:
            ecrireValeurGrille(m, 0, 2, 'O')
    else:
        tourOrdiIntel(m)


def lireValeurGrille(m, i, j):
    return m[(3*j)+i]


def ecrireValeurGrille(m, i, j, valeur):
    m[(3*j)+i] = valeur


def afficherGrille(m):
    ligne = 0
    while ligne < 3:
        colonne = 0
        while colonne < 3:
            print('|', lireValeurGrille(m, colonne, ligne), end=' | ')
            colonne = colonne+1
        print("")
        ligne = ligne+1


def main():
    m = creerGrille()
    Nom = input(
        "Bienvenue sur le jeu inconique Tic tac toe, entrez votre nom : ")
    print("Bonjour", Nom)
    print("(1) Jouer (2) Afficher les règles")
    Option = int(input("Choisissez une option : "))
    if (Option == 1):
        print("(1) Facile (2) Intermédiare (3) Difficile")
        difficulty = int(input("Choisissez une difficultée : "))
        partie(m, difficulty)
    elif (Option == 2):
        afficherRegles()
        print("(1) Oui (2) Non")
        Option = int(input("Souhaitez vous jouer maintenant ? "))
        if (Option == 1):
            print("(1) Facile (2) Intermédiare (3) Difficile")
            difficulty = int(input("Choisissez une difficultée : "))
            partie(m, difficulty)

    while True:
        if (partie(m, difficulty) == True):
            afficherGrille(m)
            print("Félications", Nom, "vous avez battu l'ordinateur !")
        elif (partie(m, difficulty) == False):
            afficherGrille(m)
            print("L'ordinateur à été plus fort que vous !")
        elif (partie(m, difficulty) == None):
            print("Égalité !")

        print("(1) Oui (2) Non")
        replay = int(input("Souhaitez vous rejouer ? "))
        if (replay == 2):
            print("Au revoir !")
            break
        print("(1) Facile (2) Intermédiare (3) Difficile")
        difficulty = int(input("Choisissez une difficultée : "))
        m = creerGrille()
        partie(m, difficulty)


main()
