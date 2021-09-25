class Node:
    def __init__(self,x,y,state):
        self.posX=x
        self.posY=y
        self.state=state
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

class WorldGen:
    def __init__(self,size):
        #2W Board is in charge of handling the visual generation
        #TEST MATRIZ
        self.mtx_2WBoard=[]
        #Wrld_Size is the number of rows in the board
        self.Wrld_Size=size
        #mtx_NodeBoard is un charge of handling the node generation for the modifiable world
        self.mtx_NodeBoard=[]


    def Create2WMatrix(self):
        for i in range(self.Wrld_Size):
            a = [0]*self.Wrld_Size
            self.mtx_2WBoard.append(a)
        print(self.mtx_2WBoard)

    def CreateNodeWeb(self,W2matrix):
        matrix=W2matrix
        for i in range (0,self.Wrld_Size):
            for j in range (0,self.Wrld_Size):
                #convierte en la clase NODOS la matrix y setea las posiciones que estan
                if(matrix[i][j]==0):
                    matrix[i][j]=Node(j,i,"libre")
                else:
                    matrix[i][j]=Node(j,i,"pared")               
        #ADDWEBS           
        for i in range (0,self.Wrld_Size):
            for j in range (0,self.Wrld_Size):
                
                if(matrix[i][j].posX<self.Wrld_Size-1):
                    #Derecha
                    matrix[i][j].connectDerecha=matrix[i][j+1]
                    #izquierda
                    matrix[i][j+1].connectIzquierda=matrix[i][j]
                if(matrix[i][j].posY<self.Wrld_Size-1):
                    #Abajo
                    matrix[i][j].connectAbajo=matrix[i+1][j]
                    #Arriba
                    matrix[i+1][j].connectArriba=matrix[i][j]

                print(matrix[i][j].GetPos(),matrix[i][j].state,matrix[i][j].connectArriba,matrix[i][j].connectAbajo,matrix[i][j].connectIzquierda,matrix[i][j].connectDerecha)




