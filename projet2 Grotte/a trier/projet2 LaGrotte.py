class jeu():
    def __init__(self):
        self.map=[]
    def affiche(self):
        '''
        Affiche la carte avec les positions et directions de tous les pions en jeu.
        '''
        map=["# #############\n","#             #","#####  ########","#         #   #","#  ########   #","#             O","########  #####","       #  #","       ####"]
        self.map.append(map)
        return self.map


    def tour(self):
        '''
        Fait agir chaque pion une fois et affiche le nouvel état du jeu.
        '''

    def demarre(self):
        '''
        Lance une boucle infinie en attendantdes commandes de l'utilisateur
        '''


tst=Principale()
print(tst.affiche())


class Pion:
    def __str__(self):
        if direction==1:
            pion=">"
        else:
            pion="<"

    def action(self):

    def quitte(self):






class Case:
    def __str__(self)

    def libre(self):

    def depart(self):

    def arrivee(self,pion):

