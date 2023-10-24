import time

start_time = time.time()
Liste =["0", "1"]
mdp = input("Entrer le mot de passe de 3 caracteres : ")
chaine = str()

def fonction1(chaine,mdp):
    if chaine == mdp :
        print("le mot de passe est : " ,chaine)

def forcebrut() :
    for i in Liste :
        chaine = i
        fonction1(chaine,mdp)
        for i2 in Liste:
            chaine = i+i2
            fonction1(chaine,mdp)
            for i3 in Liste:
                chaine = i+i2+i3
                fonction1(chaine,mdp)

forcebrut()
print("Le temps d'éxecution est de : %s secondes" % (time.time() - start_time))

            

   
         

