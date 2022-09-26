class Jeu:

    def __init__(self,nom_de_la_grotte):
        carte = open(nom_de_la_grotte)
        self.grotte = [[Case(car) for car in ligne if car != '\\n']\
                        for ligne in carte.readlines()]
        self.listeDePion=[]
        self.nbPoints = 0
        carte.close()
        self.aide="\n#################################################################\n\nLe but du jeu :\tFaire sortir tout les pions de la grotte.\n\nActions :\t'+'\t\t pour ajouter un pion\n\t\t\t'ENTRER' pour faire un tour\n\t\t\t'q'\t\t pour quiter le jeu\n\n#################################################################\n"

    def afficher(self):
        for lignes in self.grotte:
            for case in lignes:
                print(case,end='')
        print('\n')
        print("Nombre de pion(s) dans la grotte =",len(self.listeDePion))
        print("Nombre de point(s) =",self.nbPoints,"\n")


    def tour(self):
        for elem in self.listeDePion:
            elem.action()

    def demarre(self):
        self.afficher()
        while 0==0:
            action = input("[+] pour ajouter un pion, [ ] pour faire avancer le pion, [q] pour quitter le jeu\naide:[ ? ]").lower()
            if action == 'q':
                print("\n\t################\n\n\tFin de la partie !")
                if self.nbPoints !=0:
                    if len(self.listeDePion)>=4:
                        print("\t\t🌟⭐⭐")
                    elif len(self.listeDePion)==3:
                        print("\t\t🌟🌟⭐")
                    elif len(self.listeDePion)==2:
                        print("\t\t🌟🌟🌟")
                else:
                    print("\n\tVous avez perdu.")
                print("\n\t################\n")
                exit()
            elif action == '+':
                self.tour()
                self.ajouter_Pion()
            elif  action == "?":
                print(self.aide)
            else:
                self.tour()

    def ajouter_Pion(self):
        pion = Pion(0,1,1,self)
        self.listeDePion.append(pion)
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
        return self.terrain != '#' and not isinstance(self.occupant,Pion)

    def sortie(self):
        return self.terrain == 'O'

    def depart(self):
        self.occupant = None

    def arrive(self,pion):
        if self.terrain != 'O':
            self.occupant = pion
        else:
            pion.quitte()

class Pion:

    def __init__(self,l,c,direction,jeu):
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
        self.jeu
        if self.jeu.grotte[self.l + 1][self.c].libre():
            self.jeu.grotte[self.l + 1][self.c].arrive(self)
            self.jeu.grotte[self.l][self.c].depart()
            self.l+=1
        else:
            if self.jeu.grotte[self.l][self.c + self.d].libre():
                self.jeu.grotte[self.l][self.c + self.d].arrive(self)
                self.jeu.grotte[self.l][self.c].depart()
                self.c+=self.d
            else:
                self.d = -self.d
        self.jeu.afficher()

    def quitte(self):
        if self.jeu.grotte[self.l][self.c+1].sortie():
            self.jeu.grotte[self.l][self.c].depart()
            self.jeu.listeDePion.remove(self)
            self.jeu.nbPoints+=1




test = Jeu('Grotte.txt')
test.demarre()