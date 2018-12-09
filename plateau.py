__authors__ = "Ajoutez les noms des membres de votre équipe!"
__date__ = "Ajoutez la date de remise"

"""
Ce fichier permet de...(complétez la description de ce que
ce fichier est supposé faire !
"""

from case import Case
from random import randrange, choice


class Plateau:

    """
    Classe modélisant le plateau du jeu Tic-Tac-Toe.

    Attributes:
        cases (dictionary): Dictionnaire de cases. La clé est une position (ligne, colonne),
                            et la valeur est une instance de la classe Case.
    """

    def __init__(self):
        """
        Méthode spéciale initialisant un nouveau plateau contenant les 9 cases du jeu.
        """

        # Dictionnaire de cases.
        # La clé est une position (ligne, colonne), et la valeur est une instance de la classe Case.
        self.cases = {}

        self.difficulte = None

        # Appel d'une méthode qui initialise un plateau contenant des cases vides.
        self.initialiser()

    def initialiser(self):
        """
        Méthode fournie permettant d'initialiser le plateau avec des cases vides (contenant des espaces).
        """

        # Vider le dictionnaire (pratique si on veut recommencer le jeu).
        self.cases.clear()
        # Parcourir le dictionnaire et mettre des objets de la classe Case.
        # dont l'attribut "contenu" serait un espace (" ").
        for i in range(0, 3):
            for j in range(0, 3):
                self.cases[i,j] = Case(" ")

    def __str__(self):
        """Méthode spéciale fournie indiquant à Python comment représenter une instance de Plateau
        sous la forme d'une chaîne de caractères. Permet donc d'afficher le plateau du jeu
        à l'écran en faisant par exemple:
        p1 = Plateau()
        print(p1)
        Donc, lorsque vous affichez un objet, Python invoque automatiquement la méthode __str__
        Voici un exemple d'affichage:
         +-0-+-1-+-2-+
        0|   | X | X |
         +---+---+---+
        1| O | O | X |
         +---+---+---+
        2|   |   | O |
         +---+---+---+

        Returns:
            string: Retourne la chaîne de caractères à afficher.
        """
        s = " +-0-+-1-+-2-+\n"
        for i in range(0, 3):
            s += str(i)+ "| "
            for j in range(0, 3):
                s += self.cases[(i,j)].contenu + " | "
            if i<=1:
                s += "\n +---+---+---+\n"
            else:
                s += "\n +---+---+---+"
        return s

    def non_plein(self):
        """
        Retourne si le plateau n'est pas encore plein.
        Il y a donc encore des cases vides (contenant des espaces et non des "X" ou des "O").

        Returns:
            bool: True si le plateau n'est pas plein, False autrement.
        """
        return any(case.est_vide() for case in self.cases.values())

    def position_valide(self, ligne, colonne):
        """
        Vérifie si une position est valide pour jouer.
        La position ne doit pas être occupée.
        Il faut utiliser la méthode est_vide() de la classe Case.

        Args:
            ligne (int): Le numéro de la ligne dans le plateau du jeu.
            colonne (int): Le numéro de la colonne dans le plateau du jeu.

        Returns:
            bool: True si la position est valide, False autrement.
        """
        assert isinstance(ligne, int), "Plateau: ligne doit être un entier."
        assert isinstance(colonne, int), "Plateau: colonne doit être un entier."

        if(ligne not in range(0,3) or colonne not in range(0,3)):
            return False
        return self.cases[ligne,colonne].est_vide()

    def selectionner_case(self, ligne, colonne, pion):
        """
        Permet de modifier le contenu de la case
        qui a les coordonnées (ligne,colonne) dans le plateau du jeu
        en utilisant la valeur de la variable pion.

        Args:
            ligne (int): Le numéro de la ligne dans le plateau du jeu.
            colonne (int): Le numéro de la colonne dans le plateau du jeu.
            pion (string): Une chaîne de caractères ("X" ou "O").
        """
        assert isinstance(ligne, int), "Plateau: ligne doit être un entier."
        assert isinstance(colonne, int), "Plateau: colonne doit être un entier."
        assert isinstance(pion, str), "Plateau: pion doit être une chaîne de caractères."
        assert pion in ["O", "X"], "Plateau: pion doit être 'O' ou 'X'."

        self.cases[ligne,colonne] = Case(pion)


    def est_gagnant(self, pion):
        """
        Permet de vérifier si un joueur a gagné le jeu.
        Il faut vérifier toutes les lignes, colonnes et diagonales du plateau.

        Args:
            pion (string): La forme du pion utilisé par le joueur en question ("X" ou "O").

        Returns:
            bool: True si le joueur a gagné, False autrement.
        """

        assert isinstance(pion, str), "Plateau: pion doit être une chaîne de caractères."
        assert pion in ["O", "X"], "Plateau: pion doit être 'O' ou 'X'."

        regles_vic = [[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)],
                      [(0,0),(1,0),(2,0)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)],
                      [(0,0),(1,1),(2,2)],[(0,2),(1,1),(2,0)]]
        return any(all(self.cases[j].est_pion(pion) for j in regle) for regle in regles_vic)

    def choisir_prochaine_case(self, pion):
        """
        Permet de retourner les coordonnées (ligne, colonne) de la case que l'ordinateur
        peut choisir afin de jouer contre un autre joueur qui est normalement une personne.
        Ce choix doit se faire en fonction de la configuration actuelle du plateau.
        L'algorithme que vous allez concevoir permettant de faire jouer l'ordinateur
        n'a pas besoin d'être optimal. Cela permettra à l'adversaire de gagner de temps en temps.
        Il faut par contre essayer de mettre le pion de l'ordinateur dans une ligne, une colonne
        ou une diagonale contenant deux pions de l'adversaire pour que ce dernier ne gagne pas facilement.
        Il faut aussi essayer de mettre le pion de l'ordinateur dans une ligne, une colonne
        ou une diagonale contenant deux pions de l'ordinateur pour que ce dernier puisse gagner.
        Vous pouvez utiliser ici la fonction randrange() du module random.
        Par exemple: randrange(1,10) vous retourne une valeur entre 1 et 9 au hasard.

        Args:
            pion (string): La forme du pion de l'adversaire de l'ordinateur ("X" ou "O").

        Returns:
            (int,int): Une paire d'entiers représentant les coordonnées de la case choisie.
        """
        assert isinstance(pion, str), "Plateau: pion doit être une chaîne de caractères."
        assert pion in ["O", "X"], "Plateau: pion doit être 'O' ou 'X'."

        if (self.difficulte==2):
            bot = MinMaxBot()
            return bot.play(self.cases, pion)

        test=False

        while(not test):
            ligne= randrange(0,3)
            column= randrange(0,3)
            if(self.position_valide(ligne,column)):
                test=True
        #check if Pc can win
		#check line
        for x in range(0,2) :
           # I think mehoush 9a3ed y checki fel tie 

                liste_vic_line =[[' ',pion,pion],[pion,' ',pion],[pion,pion,' ']]
                for i in range(0,3):

                    for k,l in enumerate(liste_vic_line) :
                       test = True
                       for j in range(0,3) :
                           if(l[j] != self.cases[i,j].contenu):
                               test=False
                       if test:
                            return i,k
                test=True
                #check column
                for i in range(0,3):

                    for k,l in enumerate(liste_vic_line) :
                        test = True
                        for j in range(0,3) :
                            if(l[j]!=self.cases[j,i].contenu):
                                test=False
                        if test:
                            return k,i
                test=True
                #check Diagonal_gauche

                for k,l in enumerate(liste_vic_line):
                    test = True
                    for j in range(0,3) :

                        if(l[j]!=self.cases[j,j].contenu):
                            test=False
                    if test:
                        return k,k
                test=True
                #check Diagonal_droite
                for k,l in enumerate(liste_vic_line):
                    test = True
                    for j in range(0,3) :
                        if(l[j]!=self.cases[j,2-j].contenu):
                            test=False
                    if test:
                        return k,k

                test = True
                pion = 'X' if pion=='O' else 'O'

        return(ligne,column)

X = 'X'
O = 'O'
Empty = ' '

regles_vic = ([0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6])

gameboard_conversion = {0:(0,0),1:(0,1),2:(0,2),3:(1,0),4:(1,1),5:(1,2),6:(2,0),7:(2,1),8:(2,2)}

def GetOpponent(car):
    if car is X: return O
    return X

def GetAvailableMoves(GameBoard):
    a=[Item for Item, Value in enumerate(GameBoard) if Value is Empty]
    return a


def ConvertGameBoard(GameBoard):
    newGameBoard = []
    for i in range(0, 3):
        for j in range(0, 3):
            newGameBoard.append(GameBoard[i, j].contenu)
    return newGameBoard

class MinMaxBot:
    def __init__(self):
        self.GameBoard = None
        self.pion = None
        self.Opponent = None
        self.GameEnded = False
        self.base_score = None

    def play(self, GameBoard, Char):
        # reinitialize this turn properties
        self.GameBoard = ConvertGameBoard(GameBoard)
        self.pion = Char
        self.Opponent = GetOpponent(Char)
        Least = -9999
        BestPlay = []
        self.base_score = len(GetAvailableMoves(self.GameBoard))
        if self.base_score is 9:
            return gameboard_conversion[4]
        for Move in GetAvailableMoves(self.GameBoard):
            self.select_case(Move, Char)
            Value = self.meilleur_coup(GetOpponent(Char), -(self.base_score + 1), self.base_score + 1, 0)
            self.select_case(Move, Empty)
            if Value > Least:
                Least = Value
                BestPlay = [Move]
            elif Value == Least:
                BestPlay.append(Move)
        return gameboard_conversion[choice(BestPlay)]

    def a_gagne(self):
        for Char in ('X', 'O'):
            Moves = [Move for Move, Value in enumerate(self.GameBoard) if Value == Char]
            for WinningState in regles_vic:
                winner = True
                for Move in WinningState:
                    if Move not in Moves:
                        winner = False
                if winner:
                    if Char is self.pion:
                        self.GameEnded = True
                        return self.pion
                    elif Char is self.Opponent:
                        self.GameEnded = True
                        return self.Opponent
        Items = len([Item for Item, Value in enumerate(self.GameBoard) if Value!=Empty])
        if Items is 9:
            self.GameEnded = True
            return 'Draw'
        return None


    def select_case(self, position, pion):
        self.GameBoard[position] = pion

    # this algorithm use minimax algorithm with alpha beta pruning
    def meilleur_coup(self, pion, lower_bound, upper_bound, depth=0):
        winner = self.a_gagne()
        if self.GameEnded:
            if winner is self.pion:
                return self.base_score-depth
            elif winner is self.Opponent:
                return depth-self.base_score
            elif winner is 'Draw':
                return 0
        for coup in GetAvailableMoves(self.GameBoard):
            self.select_case(coup, pion)
            Value = self.meilleur_coup(GetOpponent(pion), lower_bound, upper_bound, depth + 1)
            self.select_case(coup, Empty)
            if pion == self.pion:
                if Value > lower_bound:
                    lower_bound = Value
                if lower_bound >= upper_bound:
                    return upper_bound
            else:
                if Value < upper_bound:
                    upper_bound = Value
                if upper_bound <= lower_bound:
                    return lower_bound
        if pion == self.pion:
            return lower_bound
        else:
            return upper_bound

















