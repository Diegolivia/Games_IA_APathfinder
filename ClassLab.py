from config import *
import math
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
        self.Finished=False
        self.Pathing=Pathfinder(3)

    def InitPaths(self):
        self.Pathing.ConfigPath(self.GoalPos)
        self.Pathing.Map_Intention(self.ActualPos)
        pass

    def Move(self):
        aux= self.Pathing.InitPath(self.ActualPos)
        self.ActualPos = aux[0]
        self.UpdateSprite()
        
    def UpdateSprite(self):
        self.CurrSprite.x=BOARD_BORDER+self.JUMP*self.ActualPos.posX
        self.CurrSprite.y=BOARD_BORDER+self.JUMP*(BOARD_SIZE-self.ActualPos.posY-1)
        pass

    def ini_Sprites(self,img_player,img_goal,Jump,SLOT_SCALE):
        self.JUMP=Jump
        self.CurrSprite=pyglet.sprite.Sprite(img_player,
            BOARD_BORDER+Jump*self.ActualPos.posX,
            BOARD_BORDER+Jump*(BOARD_SIZE-self.ActualPos.posY-1),
            batch=Gfx_batch,
            group=GfxOrd_Players
            )
        self.CurrSprite.scale=SLOT_SCALE
        self.GoalSprite=pyglet.sprite.Sprite(img_goal,
            BOARD_BORDER+Jump*self.GoalPos.posX,
            BOARD_BORDER+Jump*(BOARD_SIZE-self.GoalPos.posY-1),
            batch=Gfx_batch,
            group=GfxOrd_Players
            )
        self.GoalSprite.scale=SLOT_SCALE
        pass
class Pathfinder:
    def __init__(self,vision):
        self.Vision=vision-1
        self.ply_PrefMove=[]
        self.path_Explored=[]
        self.path_toExplore=[]
        self.endNode=None
        pass

    def ConfigPath(self,endnode):
        self.endNode = endnode
        pass

    def Measure_distances(self,ActualPos):
        return math.sqrt(pow(abs(ActualPos.posX-self.endNode.posX),2)+pow(abs(ActualPos.posY-self.endNode.posY),2))

    def Validate_movement(self,NodePos):
        if(NodePos==None): 
            print(["WORLD BORDER"])
            return False
        print([NodePos.posX+1,NodePos.posY+1,NodePos.state])
        if(NodePos.state=="libre"):
            return True
        else:
            return False

    def ReviewMovementPreference(self,weights):
        minval=[]
        print(weights)
        while (len(minval)<2):
            for a in [ x for x in range(len(weights)) if weights[x] == min(weights)]:
                minval.append(a)
                weights[a]=9999
                print(minval)
        return minval

    def finished(self,CurrNode):
        print("Camino finalizado")
        print(str([CurrNode,self.Measure_distances(CurrNode)]))
        print("================================================================")
        return [CurrNode,self.Measure_distances(CurrNode)]

    def Map_Intention(self,startNode):
        #Se ejecuta para calcular la direccion hacia la cual el agente querra dirigirse
        #Al inicio del juego
        weights=[]
        print("======================================================")
        print("Actual Node")
        print([startNode.posX+1,startNode.posY+1,startNode.state])
        print("Next Nodes")
        for x in startNode.Next:
            if self.Validate_movement(x):
                weights.append(self.Measure_distances(x))
            else:
                weights.append(9999)
        self.ply_PrefMove=self.ReviewMovementPreference(weights)
        print("Direcciones Preferidas -> "+ str(self.ply_PrefMove))
        
    def InitPath(self,actualNode):
        self.path_toExplore=[]
        self.path_toExplore.append(actualNode)
        print("======================================================")
        print("Iniciar Bloque de pasos")
        return self.runPathing(1)

    def runPathing(self,step):
        print("======================================================")
        print("paso "+  str(step))
        act=self.path_toExplore.pop(0)
        if (act==self.endNode or step==self.Vision+1):
            return self.finished(act)
        for x in self.ply_PrefMove:
            if self.Validate_movement(act.Next[x]):
                self.path_toExplore.append(act.Next[x])
            else:
                #Si existe un movimiento no valido(Pared/Borde), se revisan el resto de ramas
                print("Pared alcanzada")
        validate=[]
        for x in self.path_toExplore:
            validate.append(self.runPathing(step+1))
        if (len(validate)==1):
            return validate[0]
        else:
            mn=[]
            for x in validate:
                mn.append(x[1])
            aux=mn.index(min(mn))
            return validate[aux]