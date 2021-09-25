from config import *

class Engine:
    def __init__(self, Ass_List):
        self.arr_imgBank = []
        self.arr_SpriteBank = []
        self.load(Ass_List)

    def load(self,Ass_List):
        f = open(Ass_List, "r")
        for x in f:
            x=x.strip()
            self.arr_imgBank.append(pyi.load(x))
        Board = pyglet.sprite.Sprite(self.arr_imgBank[0],
                                     batch=Gfx_batch,
                                     group=GfxOrd_Background)
        print("Tablero Cargado")
        Board.scale = BACKGROUND_SCALE
        self.arr_SpriteBank.append(Board)
        for x in range(BOARD_SIZE):
            for y in range(BOARD_SIZE):
                Slot = pyglet.sprite.Sprite(self.arr_imgBank[1],
                                            BOARD_BORDER + JUMP * x,
                                            BOARD_BORDER + JUMP * y,
                                            batch=Gfx_batch,
                                            group=GfxOrd_BoardObjects)
                Slot.scale = SLOT_SCALE
                self.arr_SpriteBank.append(Slot)
        print("Sprites Cargados")