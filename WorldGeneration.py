import random


class Node:
    def __init__(self, x, y, state):
        self.posX = x
        self.posY = y
        self.state = state
        self.Next = [None, None, None, None]

    def GetPos(self):
        return self.posX, self.posY

    def GetPosX(self):
        return self.posX

    def GetPosY(self):
        return self.posX

    def SetPos(self, posX, posY):
        self.posX = posX
        self.posY = posY


class Player:
    def __init__(self):
        self.ActualPos = None
        self.GoalPos = None


#NOTA: SIEMPRE LA PRIMERA POSICION ES Y, LA SEGUNDA ES X
class WorldGen:
    def __init__(self,Wsize):
        self.Wrld_Size=Wsize
        pass

    def Create2WMatrix(self):
        arr=[]
        for i in range(self.Wrld_Size):
            a = random.choices(population=[0, 1], weights=[0.9,0.1], k=self.Wrld_Size)
            arr.append(a)
        return arr

    def CreateNodeWeb(self,mtx):
        mtx_NodeBoard=[]
        for i in range(0, self.Wrld_Size):
            a=[]
            for j in range(0, self.Wrld_Size):
                # convierte en la clase NODOS la matrix y setea las posiciones que estan
                if mtx[i][j] == 0:
                    a.append(Node(j, i, "libre"))
                else:
                    a.append(Node(j, i, "pared"))
            mtx_NodeBoard.append(a)
        # ADDWEBS
        # Saves the next nodes on an array inside each node
        # 0->UP, 1->DOWN, 2->LEFT, 3->RIGHT
        for i in range(0, self.Wrld_Size):
            for j in range(0, self.Wrld_Size):
                if mtx_NodeBoard[i][j].posX < self.Wrld_Size - 1:
                    # Derecha
                    mtx_NodeBoard[i][j].Next[3] = mtx_NodeBoard[i][j + 1]
                    # izquierda
                    mtx_NodeBoard[i][j + 1].Next[2] = mtx_NodeBoard[i][j]
                if mtx_NodeBoard[i][j].posY < self.Wrld_Size - 1:
                    # Abajo
                    mtx_NodeBoard[i][j].Next[1] = mtx_NodeBoard[i + 1][j]
                    # Arriba
                    mtx_NodeBoard[i + 1][j].Next[0] = mtx_NodeBoard[i][j]
        return mtx_NodeBoard
    #NOTA: SIEMPRE LA PRIMERA POSICION ES Y, LA SEGUNDA ES X
    #ORDER DE GENERACION
    #TOPLEFT,TOPRIGHT,DOWNLEFT,DOWNRIGHT
    def GenerateCoords(self, key):
        if key == 0:
            return [
                random.randrange(0, int(self.Wrld_Size / 2)),
                random.randrange(0, int(self.Wrld_Size / 2)),
            ]
        elif key == 1:
            return [
                random.randrange(0, int(self.Wrld_Size / 2)),
                random.randrange(int(self.Wrld_Size / 2), int(self.Wrld_Size)),
            ]
        elif key == 2:
            return [
                random.randrange(int(self.Wrld_Size / 2) + 1, int(self.Wrld_Size)),
                random.randrange(0, int(self.Wrld_Size / 2)),
            ]
        else:
            return [
                random.randrange(int(self.Wrld_Size / 2) + 1, int(self.Wrld_Size)),
                random.randrange(int(self.Wrld_Size / 2) + 1, int(self.Wrld_Size)),
            ]

    # Tries to generate 1-4 players in different sectors of the board, ussualy splits the board into 4 sides and generate a player on each side
    def GeneratePlayers(self, numPlayers,mtx_2WBoard,mtx_NodeBoard):
        # Location Order -> TopLeft,DownLeft,TopRight,DownRight
        mtx_Players=[]
        for x in range(numPlayers):
            pl=Player()
            value = True
            while(value):
                aux=self.GenerateCoords(x)
                if(mtx_2WBoard[aux[0]][aux[1]]==0):
                    pl.ActualPos=mtx_NodeBoard[aux[0]][aux[1]]
                    msg="Player "+str(x)+" START has been created at "+str(aux[1]+1)+", " +str(aux[0]+1)
                    print(msg)
                    value=False
            value = True
            while(value):
                aux=self.GenerateCoords(random.randint(0,4))
                if(mtx_2WBoard[aux[0]][aux[1]]==0):
                    pl.GoalPos=mtx_NodeBoard[aux[0]][aux[1]]
                    msg="Player "+str(x)+" GOAL has been created at "+str(aux[1]+1)+", " +str(aux[0]+1)
                    print(msg)
                    value=False
            mtx_Players.append(pl)
        return mtx_Players
