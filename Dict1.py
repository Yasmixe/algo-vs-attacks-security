import time
start_time = time.time()

dictionnaire = ["000", "001", "010", "011", "100", "101", "110", "111"]

# Mot de passe à deviner
mdp = input("donner le mot de passe : ")

# Fonction pour effectuer l'attaque par dictionnaire
def attaque_par_dictionnaire(dictionnaire, mdp):
    for mot in dictionnaire:
        if mot == mdp:
            return mot
    return None

# Appel de la fonction d'attaque par dictionnaire
resultat = attaque_par_dictionnaire(dictionnaire, mdp)

# Test final et affichage
if resultat is not None:
    print(f"Le mot de passe est : {resultat}")
else:
    print("Le mot de passe n'a pas été trouvé dans le dictionnaire.")

print("Le temps d'éxecution est de : %s secondes" % (time.time() - start_time))