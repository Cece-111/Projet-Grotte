class Jeu:
    def init(self,nom_de_la_grotte):
        carte = open(nom_de_la_grotte)
        self.grotte = [[Case(car) for car in ligne if car != '\n']\
                        for ligne in carte.readlines()]
        pion = []
    def afficher(self):
        for lignes in self.grotte:
            for case in lignes:
                print(case,end='')

    def tour(self):
        while 0==0:
            action = input('choisir votre action')

class Pion:
    def init(self,l,c,direction,j):
        self.l = l
        self.c = c
        self.d = direction
        self.jeu = j
    def action(self):
        if tour()== '+':
            Pion(1,1,1)
    def str(self):
        if self.d == '1':
            return '>'
        else:
            return '<'


class Case:
    def init(self,terrain):
        self.terrain = terrain
    def str(self):
        return str(self.terrain)





test = Jeu('CircuitGrotte.txt')
test.afficher()
