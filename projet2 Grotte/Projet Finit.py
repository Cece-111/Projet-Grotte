class Jeu:
    def __init__(self,nom_de_la_grotte):
        carte = open(nom_de_la_grotte)
        self.grotte = [[Case(car) for car in ligne if car != '\\n']\
                        for ligne in carte.readlines()]
        self.listeDePion=[]
        carte.close()

    def afficher(self):
        for lignes in self.grotte:
            for case in lignes:
                print(case,end='')
        print('\n')
        #print("Nombre de pion dans la grotte =", ajouter_Pion().nombrePion)
        #print('\n' * 10)

    def tour(self):
        for elem in self.listeDePion:
            elem.action()

    def demarre(self):
        self.afficher()
        while True:
            action = input('[+] pour ajouter un pion, [ ] pour faire avancer le pion, [q] pour quitter le jeu')
            if action == 'q':
                exit()
            if action == '+':
                self.ajouter_Pion()
            else:
                self.tour()

    def ajouter_Pion(self):
        nombrePion = 0
        pion = Pion(0,1,1)
        self.listeDePion.append(pion)
        nombrePion+=1
        self.grotte[0][1].arrive(pion)
        self.afficher()

class Case:
    def __init__(self,terrain):
        self.terrain = terrain
        self.occupant = None

    def __str__(self):
        if self.occupant != None:
            return str(self.occupant)
        else:
            return self.terrain

    def libre(self):
        if self.terrain != '#' and not isinstance(self.occupant,Pion):
            return True
        else:
            return False

    def depart(self):
        self.occupant = None

    def arrive(self,pion):
        self.occupant = pion


class Pion:
    def __init__(self,l,c,direction,jeu=Jeu('Grotte.txt')):
        self.l = l
        self.c = c
        self.d = direction
        self.jeu = jeu

    def __str__(self):
        if self.d == 1:
            return '>'
        elif self.d == -1:
            return '<'

    def action(self):
        if self.jeu.grotte[self.l+1][self.c].libre():
            self.jeu.grotte[self.l+1][self.c].arrive(self)
            self.jeu.grotte[self.l][self.c].depart()
            self.jeu.afficher()
            self.l+=1

        else:
            if self.jeu.grotte[self.l][self.c+self.d].libre():
                self.jeu.grotte[self.l][self.c+self.d].arrive(self)
                self.jeu.grotte[self.l][self.c].depart()
                self.jeu.afficher()
                self.c+=self.d

            elif self.jeu.grotte[self.l+1][self.c]=="O":
                #print("O a été touché !")                   ### Print de debug
                print("Vous avez gagné !")
                jeu.exit()

            else:
                self.d = -self.d
                self.jeu.afficher()

    def quitte(self):
        self.jeu.exit()


test = Jeu('Grotte.txt')
test.demarre()

