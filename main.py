from personnage import Personnage
from arme import Arme

joueur1 = Personnage("Aragorn", "Guerrier", 10, 100, 15, 5)
joueur2 = Personnage("Gandalf", "Magicien", 10, 80, 5, 15)

joueur1.afficher_info()
joueur2.afficher_info()

joueur1.attaquer(joueur2)
joueur2.afficher_info()
joueur2.attaquer(joueur1)
joueur1.afficher_info()
