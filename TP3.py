from Class import *


mediatheque = Mediatheque()

def ajouter_media(mediatheque):
    a = "oui"
    while(a == "oui" or a== "OUI" or a == "o" or a=="Oui"):

        type = input("quel type de média, est-ce (livre, dvd, article ou cd) ? ") 

        titre = input("Quel est son titre ?")
        date = int(input("Quel est sa date de parution ?"))
        auteur = input("Quel est son auteur?")

        if type =="livre" or type =="Livre" or type == "LIVRE" or type=="livres" :
            editeur = input("Qui est son editeur?")
            nombre_de_pages = int(input("Combien de pages posséde-t-il ?"))
            media =Livre(titre,date,auteur,nombre_de_pages,editeur)

        elif type =="article" or type =="mag" or type == "magazine" or type=="article de magazine" :
            nom = input("Quel est le nom du magazine?")
            numero = int(input("quel est le numero du magazine ?"))
            page_debut = int(input("Il va de la page (tapez la page de debut)"))
            page_fin = int(input("à la page...(tapez la page de fin de l'article)"))
            media =Magazine(titre,date,auteur,nom,numero, page_debut, page_fin)

        else:
            duree = int(input("Quel est sa duree? "))
            if type =="cd" or type =="cds" or type == "CD" or type=="Cd" :
                nombre_de_morceaux = int(input("Combien de morceaux de musiques posséde-t-il ?"))
                media = CD(titre,date,auteur,duree,nombre_de_morceaux)
            else :
                media = DVD(titre,date,auteur,duree)

        
    
        mediatheque.ajouter_medium(media)
        a = input("voulez vous ajouter un autre média (oui ou non) ? ")

ajouter_media(mediatheque)

b = "oui"
while (b=="oui" or b=="o" or b=="Oui" or b=="OUI"):
    Choix = int(input("Que voulez vous faire ?\n 0 pour voir la liste des media disponible\n 1 pour retirer un media (titre et auteur)\n 2 pour retirer les medias d'un auteur\n 3 pour voir la liste des medias fait par le même auteur \n 4 pour emprunter un media \n 5 pour savoir combien de medias ont été emprunté\n 6 pour ajouter un ou plusieurs medias : \n")) 

    if Choix == 0 :
        mediatheque.lister_medium2()
    if Choix ==1:
        nom_retirer = input("quel est l'auteur du media à retirer ?")
        titre_retirer = input("quel est le titre du media à retirer ?")
        mediatheque.retirer_medium(nom_retirer,titre_retirer)

    if Choix ==2:
        nom_retirer = input("quel est l'auteur dont on doit retirer les creations ? ")
        mediatheque.retirer_medium_auteur(nom_retirer)

    if Choix == 3 :
        nom_auteur = input("quel est l'auteur dont on doit lister les creations ? ")
        mediatheque.lister_medium(nom_auteur)

    if Choix == 4 :
        nom_pret = input("quel est l'auteur du media à emprunter? ")
        titre_pret = input("quel est le titre du media à emprunter? ")
        votre_nom = input("quel est votre nom ? ")
        mediatheque.medium_prete(nom_pret,titre_pret, votre_nom)

    if Choix == 5 :
        print("nombre de prets :",mediatheque.compter_media_prete())

    if Choix == 6 :
        ajouter_media(mediatheque)

    b= input("voulez vous faire une autre action (oui ou non) ?")


