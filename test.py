from random import seed
from  Class import *
import unittest

class Test(unittest.TestCase) :

    # Test de la classe Mediathèque
    def test_Mediatheque(self):


        media = Mediatheque()
        
        cd = CD("reborn",2013,"Taylor Swift",200,25)
        dvd = DVD("titanic", 2012, "Cameron",180)
        livre = Livre("Alice aux pays des merveilles", 1800, "Caroll",30,"livre de poche")
        livre2 = Livre("Harry potter", 1900, "Rowling",35,"Galimard")
        cd2 = CD("Le tour du monde en 80 jours", 1900, "Verne",35,5)
        livre3 = Livre("20000 lieux sous les mers", 1900,"Verne",35,"Gallimard")
        dvd3 = DVD("Michel strogoff", 1900, "Verne",35)
       
        mag1 = Magazine("science pour les ados",2001,"anonyme","science et vie",2000,3,5)
        mag = Magazine("espace",2001,"Verne","JV",2000,3,5)

        #test de la fonction ajouter_medium (on ajoute un média de chaque type)
        media.ajouter_medium(livre2)
        media.ajouter_medium(cd)
        media.ajouter_medium(dvd)
        media.ajouter_medium(mag1)
        self.assertEqual(media.get_mediums(),[livre2, cd, dvd, mag1])

        #test de la fonction retirer_medium (on retire une par une chaque type)
        media.retirer_medium("Rowling","Harry potter")
        self.assertEqual(media.get_mediums(),[cd, dvd, mag1])
        media.retirer_medium("anonyme","science pour les ados")
        self.assertEqual(media.get_mediums(),[cd, dvd])
        media.retirer_medium("Taylor Swift","reborn")
        self.assertEqual(media.get_mediums(),[dvd])
        media.retirer_medium("Cameron","titanic")
        self.assertEqual(media.get_mediums(),[])

        #test de la fonction retirer_medium auteur
        
        media.ajouter_medium(cd2)
        media.ajouter_medium(dvd3)
        media.ajouter_medium(livre)
        media.ajouter_medium(mag)
        media.ajouter_medium(livre3)


        #Le seul media qui n'est pas de Verne (j'ai inventé pour le cd, le dvd et le magazine bien sur) est le livre Alice aux pays des merveilles
        media.retirer_medium_auteur("Verne")
        self.assertEqual(media.get_mediums(),[livre])

        #On retire le dernier medium et la liste est vide
        media.retirer_medium("Caroll","Alice aux pays des merveilles")
        self.assertEqual(media.get_mediums(),[])

        media.ajouter_medium(livre)
        media.ajouter_medium(cd)
        media.ajouter_medium(dvd)
        media.ajouter_medium(mag)

        #On veut tester la fonction qui note le pret d'un media
        media.medium_prete("Caroll","Alice aux pays des merveilles","moi")
        media.medium_prete("Cameron","titanic","Maurice")
        self.assertEqual(livre.get_prete(),"moi")

        prets = media.compter_media_prete()
        self.assertEqual(prets,2)
       

# Exécution des tests
if __name__=='__main__':
    unittest.main(argv=[''],verbosity =0, exit =False)