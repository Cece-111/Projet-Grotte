import os

def clearConsole():
    os.system('cls')

class Gui:
    def __init__(self,gui):
        gui=open("gui.txt","r")
        self.gui=[[Case(caractere) for caractere in ligne if caractere!="\n"] for ligne in gui.readlines()]
        gui.close

    def affiche2(self):
        for ligne in self.gui:
            for Case in ligne:
                print(Case,end="")
            print()

    def demarre2(self):
        self.affiche2()
        keyb=str(input("Appuyez sur [ Enter ] Pour lancer le jeu / appuyez sur [ Q ]pour quitter: "))
        if keyb=='q':
            exit()
        else:
            jeu.demarre()


class Jeu:
    def __init__(self,grotte):
        carte = open("CircuitGrotte.txt","r")
        self.grotte=[[Case(caractere) for caractere in ligne if caractere!="\n"] for ligne in carte.readlines()]
        carte.close
        self.lemmings = []
        self.nb=-1

    def __str__(self,carte):
        return carte

    def affiche(self):
        for ligne in self.grotte:
            for Case in ligne:
                print(Case,end="")
            print()

    def demarre(self):
        clearConsole()
        self.affiche()
        while True:
            cmd = input()
            if cmd=="q":
                break
            elif cmd=="l":
                self.ajoute_lemming()
            else:
                self.tour()
            clearConsole()
            self.affiche()

    def tour(self):
        Lemming(int,int).action()

    def ajoute_lemming(self):
        lem=Lemming(int,int)
        self.lemmings.append(lem)
        self.nb=self.nb+1
        self.grotte[0][1].arrivee(self.lemmings[self.nb])
        clearConsole()
        self.affiche()

class Lemming:

    def __init__(self, ligne, colonne, orientation=1):
        self.jeu=jeu
        self.li=ligne
        self.col=colonne
        self.dir=orientation

    def __str__(self):
        if self.dir==1:
            return ">"
        elif self.dir==0:
            return "<"


    def action(self):
        if self.jeu.grotte[self.li][self.col+self.dir].estLibre()==True:
            ligneDestination=self.li
            while self.jeu.grotte[ligneDestination+1][self.col==0].estLibre()==False:
                ligneDestination=ligneDestination+1
            self.deplacement(ligneDestination, self.col+ self.li)
            self.li = ligneDestination
            self.col= self.col + self.dir
        else:
            self.dir= self.dir-1

    def deplacement(self, colonne, ligne):
        self.jeu.grotte[self.li][self.col].depart()
        self.jeu.grotte[ligne][colonne].arrivee(self)

    def sort(self):
        jeu.lemmings.remove(self)

class Case:
    def __init__(self, caractere):
        self.terrain = caractere
        self.lemming = None


    def __str__(self):
        if self.lemming!=None:
            return str(self.lemming)
        else:
            return self.terrain

    def __repr__(self):
        if self.lemming!=None:
            return str(self.lemming)
        else:
            return self.terrain

    def estLibre(self):
        if self.terrain!="#" and self.lemming != "0" and self.lemming !=">":
            return False
        else:
            return True

    def sortie(self):
        if self.terrain=="0":
            return True
        else:
            return False

    def depart(self):
        self.lemming= None

    def arrivee(self, lem):
        self.lemming=lem


jeu = Jeu("grotte.txt")
gui1 = Gui("gui.txt")
gui1.demarre2()