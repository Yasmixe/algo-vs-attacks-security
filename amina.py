import string

"""dictionnaire = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
for i in dictionnaire:
    for j in dictionnaire:
        for k in dictionnaire:
            for x in dictionnaire:
                for y in dictionnaire:
                    f = open("fich.txt", "a")
                    f.write(str(i) + str(j) + str(k) + str(x) + str(y) + "\n")
                    f.close()"""

import string

dictionnaire = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
for i in dictionnaire:
    for j in dictionnaire:
        for k in dictionnaire:
            for x in dictionnaire:
                for y in dictionnaire:
                    f = open("fich.txt", "a")
                    f.write(str(i) + str(j) + str(k) + str(x) + str(y) + "\n")
                    f.close()
# Mot de passe à deviner
mdp = input("donner le mot de passe : ")
with open("fich.txt", "r") as fichier:
    contenu = fichier.read()
mots = contenu.split()


# Fonction pour effectuer l'attaque par dictionnaire
def attaque_par_dictionnaire(mots, mdp):
    for mot in mots:
        if mot == mdp:
            return mot
    return None


# Appel de la fonction d'attaque par dictionnaire
resultat = attaque_par_dictionnaire(mots, mdp)

# Vérification du résultat
if resultat is not None:
    print(f"Le mot de passe a été trouvé : {resultat}")
else:
    print("Le mot de passe n'a pas été trouvé dans le dictionnaire.")
