class Jeu:
    def __init__(self,nom_de_carte):
        carte=open(nom_de_carte)
        self.grotte=[[Case(car) for car in ligne if car !='\\n'] for ligne in carte.readlines()]
        carte.close

    def affiche(self):
        for lignes in self.grotte:
            for case in lignes:
                print(case,end='')

    def tour(self):
        '''
        Fait agir chaque pion une fois et affiche le nouvel état du jeu.
        '''
        self.action()

    #def demarre(self):


class Pion:
    def __init__(self,ligne,colonne,direction=1):
        self.li=ligne
        self.col=colonne
        self.dir=direction
        self.jeu=Jeu()

    def __str__(self):
        if self.dir==1:
            return ">"
        elif self.dir==0:
            return "<"

    def action(self):
        #self.affiche()
        while True:
            self.tour()
            cmd = input("entrez une commande")
            if cmd=="q":
                break
            elif cmd=="+":
                self.ajoutePion()




    def quitte(self):
        jeu.pion.remove(self)


class Case:
    def __init__(self,t):
        self.terrain=t
        self.occupant=None

    def __str__(self):
        return self.terrain

    def libre(self):
        if self.terrain!="#" and self.terrain != "0":
            return False
        else:
            return True

    def depart(self):
        return self.occupant is None

    def arrivee(self, pion):
        self.pion=pion


k = Jeu('CircuitGrotte.txt')
k.affiche()
k2 = Pion(1,1,1)
k2.action()