import random
class Node:
    def __init__(self,x,y,state):
        self.posX=x
        self.posY=y
        self.state=state
        self.Next=[None,None,None,None]
        self.connectDerecha=None
        self.connectIzquierda=None
        self.connectArriba=None
        self.connectAbajo=None
       
    def GetPos(self):
        return self.posX,self.posY

    def GetPosX(self):
        return self.posX

    def GetPosY(self):
        return self.posX

    def SetPos(self,posX,posY):
        self.posX=posX
        self.posY=posY

class Player:
    def __init__(self):
        self.ActualPos=None
        self.GoalPos=None

class WorldGen:
    def __init__(self,size):
        #2W Board is in charge of handling the visual generation
        #TEST MATRIZ
        self.mtx_2WBoard=[]
        #Wrld_Size is the number of rows in the board
        self.Wrld_Size=size
        #mtx_NodeBoard is un charge of handling the node generation for the modifiable world
        self.mtx_NodeBoard=[]
        self.Create2WMatrix()
        self.CreateNodeWeb(self.mtx_2WBoard)

    def Create2WMatrix(self):
        for i in range(self.Wrld_Size):
            a=random.choices(
                population=[0,1],
                weights=[0.9,0.1],
                k=self.Wrld_Size
            )
            self.mtx_2WBoard.append(a)
        print(self.mtx_2WBoard)

    def CreateNodeWeb(self,board):
        matrix=board
        for i in range (0,self.Wrld_Size):
            for j in range (0,self.Wrld_Size):
                #convierte en la clase NODOS la matrix y setea las posiciones que estan
                if(matrix[i][j]==0):
                    matrix[i][j]=Node(j,i,"libre")
                else:
                    matrix[i][j]=Node(j,i,"pared")               
        #ADDWEBS           
        #Saves the next nodes on an array inside each node
        #0->UP, 1->DOWN, 2->LEFT, 3->RIGHT
        for i in range (0,self.Wrld_Size):
            for j in range (0,self.Wrld_Size):
                if(matrix[i][j].posX<self.Wrld_Size-1):
                    #Derecha
                    matrix[i][j].Next[3]=matrix[i][j+1]
                    #izquierda
                    matrix[i][j+1].Next[2]=matrix[i][j]
                if(matrix[i][j].posY<self.Wrld_Size-1):
                    #Abajo
                    matrix[i][j].Next[1]=matrix[i+1][j]
                    #Arriba
                    matrix[i+1][j].Next[0]=matrix[i][j]
        self.mtx_NodeBoard=matrix
        del(matrix)
        print(self.mtx_2WBoard)
        print(self.mtx_NodeBoard)
    #Tries to generate 1-4 players in different sectors of the board, ussualy splits the board into 4 sides and generate a player on each side
    def GeneratePlayers(self,numPlayers):
        
        pass



data = WorldGen(5)