def checkData(valeur):  
    valeur = valeur.lstrip()  # supprime les espaces avant et apres
    if len(valeur) < 1: # verifie la taille de la chaine de car;
        return True
    else:
        return False

def saisieUser(choix):
    valeur = '' # init valeur
    while checkData(valeur):# boucle pour chercker si valeur est saisie par un user
        if choix == 1: # si on souhaite saisir le nom
            valeur = input("entrez votre nom: " )
        elif choix == 2:
            valeur = input("entrez votre prenom: ")
        else:
            valeur = input("entrez votre age: ")
            if valeur.isnumeric() == False:
                valeur = ''
    return valeur

nom = saisieUser(1)
prenom = saisieUser(2)
age = saisieUser (3)
print("Bonjour M. " + nom + " "+ prenom + " agé de "+age+"ans.")