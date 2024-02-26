
#Classe Médium prend en argument le titre, la date de parution, et l'auteur du médium
class Medium(object):
    def __init__(self, titre, date, auteur):
        self.__titre = titre
        self.__date = date
        self.__auteur = auteur
        self.__prete ="none"

#assesseurs de la classe médium (get et set)
    def get_titre(self):
        return self.__titre
    def get_date(self):
        return self.__date
    def get_auteur(self):
        return self.__auteur
    def get_prete(self):
        return self.__prete
    def set_prete(self, nom):
        self.__prete=nom

#fonction pour afficher les atteributs commun à tous les médias
    def afficher_medium(self):
        print("titre:" , self.__titre)
        print("auteur : ", self.__auteur)
        print("date de parution:" ,self.__date)
        if(self.__prete!="none"):
            print("statut : preté à ",self.__prete)

#Classe DVD, hérite du médium, prend en attribut le titre, la date de parution, l'auteur et la durée du DVD    
class DVD(Medium):
    def __init__(self,titre,date,auteur, duree):
        super().__init__(titre, date, auteur)
        self.__duree = duree

    def get_duree(self):
        return self.__duree
    def afficher(self):
        print("**************************")
        print("Type : DVD")
        super().afficher_medium()
        print("duree: ",self.__duree,"minutes")

#Classe Livre, hérite du médium, prend en attribut le titre, la date de parution, l'auteur et le nombre de chapitre et l'édition du livre   
class Livre(Medium):
    def __init__(self,titre,date,auteur, nb_chapitres, editeur):
        super().__init__(titre, date, auteur)
        self.__nb_chapitres = nb_chapitres
        self.__editeur = editeur

    def afficher(self):
        print("**************************")
        print("Type : Livre")
        super().afficher_medium()
        print("nombre de chapitres: ",self.__nb_chapitres)
        print("editeur: ",self.__editeur)

#Classe CD, hérite du médium, prend en attribut le titre, la date de parution, l'auteur et le nombre de musiques et la durée du CD  
class CD(Medium):
    def __init__(self,titre,date,auteur, duree, nb_musiques):
        super().__init__(titre, date, auteur)
        self.__duree = duree
        self.__nb_musiques = nb_musiques

    def afficher(self):
            print("**************************")
            print("Type : CD")
            super().afficher_medium()
            print("nombre de musique: ",self.__nb_musiques)
            print("duree: ",self.__duree,"minutes")

#Classe Magazine, hérite du médium, prend en attribut le titre, la date de parution, l'auteur, les pages de l'article du magazine, plus le nom et le numero du magazine  
class Magazine(Medium):
    def __init__(self, titre, date, auteur, nom, numero, page_debut, page_fin):
       super().__init__(titre, date, auteur)
       self.__nom = nom
       self.__numero = numero
       self.__page_debut = page_debut
       self.__page_fin = page_fin

    def afficher(self):
        print("**************************")
        print("Type : Article de Magazine")
        super().afficher_medium()
        print("nom du magazine: ",self.__nom)
        print("numero de magazine : ",self.__numero)
        print("numero de page : de la page ",self.__page_debut, "à la page", self.__page_fin)

#Classe médiathèque qui utilise des objet de la classe médium et son héritage
class Mediatheque (object):
    def __init__(self):
        self.__mediums = []
        self.__mediums_prete =[]
        
    #assesseurs get de l'attribut mediums, liste de Médium
    def get_mediums(self):
        return self.__mediums
    
    #Fonction pour ajouter un médium, prend en argument un médium
    def ajouter_medium(self, medium):
        self.__mediums.append(medium)
    
    #Affiche les médiums et tous leurs attributs qui paragent le même auteur donné en argument
    def lister_medium(self, auteur):
        for medium in self.__mediums :
            if medium.get_auteur()==auteur:
                medium.afficher()

    #Affiche tous les médiums et leurs attributs
    def lister_medium2(self):
        for medium in self.__mediums :
                medium.afficher()


    #retirer tous les médiums de la mediathèque, partageant le même auteur donne en argument
    def retirer_medium_auteur(self, auteur):
        mediums_a_retirer = [] 
        for medium in self.__mediums:
            if medium.get_auteur() == auteur:
                mediums_a_retirer.append(medium)
        
        for medium in mediums_a_retirer:
            self.__mediums.remove(medium)


    #retire un médium d'après son titre et son auteur donné en argument
    def retirer_medium(self, auteur, titre):
        for medium in self.__mediums:
            if medium.get_auteur()==auteur and medium.get_titre()==titre:
                self.__mediums.remove(medium)

    #Note qu'un medium a ete emprunté et par qui
    def medium_prete(self, auteur, titre, nom):
        for medium in self.__mediums:
            if medium.get_auteur()==auteur and medium.get_titre()==titre:
                self.__mediums_prete.append(medium)
                medium.set_prete(nom)

    #compte les mediums empruntés
    def compter_media_prete(self):
        return len(self.__mediums_prete)




