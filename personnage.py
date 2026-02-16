from tabulate import tabulate

class Personnage:
    def __init__(self, nom, classe, niveau, points_de_vie, force, intelligence):
        self.nom = nom
        self.classe = classe
        self.niveau = niveau
        self.points_de_vie = points_de_vie
        self.force = force
        self.intelligence = intelligence
        self.en_vie = True

    def afficher_info(self):
        print(f"Nom: {self.nom}")
        print(f"Classe: {self.classe}")
        print(f"Niveau: {self.niveau}")
        print(f"Points de vie: {self.points_de_vie}")
        print(f"Force: {self.force}")
        print(f"Intelligence: {self.intelligence}")
        etat = "En vie" if self.en_vie else "Mort"

        table = [
            ["Nom", self.nom],
            ["Classe", self.classe],
            ["Niveau", self.niveau],
            ["Points de vie", self.points_de_vie],
            ["Force", self.force],
            ["Intelligence", self.intelligence],
            ["État", etat]
        ]

        print(tabulate(table, tablefmt="fancy_grid"))

    def attaquer(self, cible):

        print(f"{self.nom} attaque {cible.nom}!")
        degats = self.force * 2

        cible.subir_degats(degats)

    def subir_degats(self, degats):
        self.points_de_vie -= degats
        print(f"{self.nom} subit {degats} points de dégâts!")

        if self.points_de_vie <= 0:
            self.en_vie = False
            print(f"{self.nom} est mort.")

# Exemple d'utilisation
joueur1 = Personnage("Aragorn", "Guerrier", 10, 100, 15, 5)
joueur2 = Personnage("Gandalf", "Magicien", 10, 80, 5, 15)

joueur1.afficher_info()
joueur2.afficher_info()

joueur1.attaquer(joueur2)
joueur2.afficher_info()