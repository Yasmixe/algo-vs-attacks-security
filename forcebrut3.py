Liste = ["a", "b","c","d","e", "f"] #["0", "1","2","3", "4","5","6", "7","8","9","A", "B","C","D", "E","F","G", "H","I","J","K", "L","M","N", "O","P","Q", "R","S","T","U", "V","W","X", "Y","Z","a", "b","c","d","e", "f","g","h", "i","j","k", "l","m","n","o", "p","q","r", "s","t","u", "v","w","x","y", "z","*","!", "@",".",",", "+","=",":","0", "-","_","-", "'","?","", "é","à","ç","#", "~","&","ù", "$","£","§", "[","]","}","{","'","|","/"]
mdp = input("Entrer le mot de passe de 5 caracteres de 0 à 9 : ")
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
                for i4 in Liste :
                    chaine = i+i2+i3+i4
                    fonction1(chaine,mdp)
                    for i5 in Liste:
                        chaine = i+i2+i3+i4+i5
                        fonction1(chaine,mdp)
                        
forcebrut()
